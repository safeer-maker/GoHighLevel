"""
05_products_and_coupons.py — Provision Sunrise Wellness products & coupons

Idempotent: existing products (matched by name or SKU) are skipped.

Products endpoint:  POST /products/                (GHL v2 API)
Prices endpoint:    POST /products/{productId}/price
Coupons endpoint:   POST /payments/coupon          (may be blocked on some plans)
"""

import json
import sys
from pathlib import Path

from config import GHL_LOCATION_ID, print_config_summary
from ghl_client import GHLAPIError, GHLAPIBlocked, client, logger

DATA_FILE = Path(__file__).parent / "data" / "products.json"


def load_spec() -> dict:
    with open(DATA_FILE) as f:
        return json.load(f)


def fetch_existing_products() -> list:
    try:
        data = client.get("/products/", params={"locationId": GHL_LOCATION_ID, "limit": 100})
        if isinstance(data, dict):
            return data.get("products", []) or data.get("data", []) or []
        return data if isinstance(data, list) else []
    except GHLAPIError as e:
        logger.error(f"Failed to list products: {e}")
        return []


def fetch_existing_coupons() -> list:
    try:
        data = client.get("/payments/coupon/list", params={"locationId": GHL_LOCATION_ID, "limit": 100})
        if isinstance(data, dict):
            return data.get("data", []) or data.get("coupons", []) or []
        return data if isinstance(data, list) else []
    except GHLAPIError as e:
        logger.debug(f"Coupon list failed ({e}); attempting alternate endpoint.")
        try:
            data = client.get("/payments/coupons", params={"locationId": GHL_LOCATION_ID})
            if isinstance(data, dict):
                return data.get("coupons", []) or data.get("data", []) or []
            return data if isinstance(data, list) else []
        except GHLAPIError:
            return []


def create_product(product_spec: dict) -> tuple:
    """Create a product. Returns (product_dict, "created"|"failed"|"blocked")."""
    payload = {
        "name": product_spec["name"],
        "description": product_spec.get("description", ""),
        "productType": product_spec.get("productType", "SERVICE"),
        "locationId": GHL_LOCATION_ID,
    }
    sku = product_spec.get("sku")
    if sku:
        payload["sku"] = sku

    try:
        resp = client.post("/products/", json=payload)
        product = resp.get("product", resp)
        return product, "created"
    except GHLAPIBlocked as e:
        return {}, f"blocked: {e.message}"
    except GHLAPIError as e:
        return {}, f"failed: {e}"


def create_price(product_id: str, price_spec: dict) -> bool:
    """Attach a price to a product."""
    payload = {
        "name": price_spec.get("name", "Default"),
        "type": price_spec.get("type", "one_time"),
        "currency": price_spec.get("currency", "USD"),
        "amount": price_spec["amount"],
        "locationId": GHL_LOCATION_ID,
    }
    if "recurring" in price_spec:
        payload["recurring"] = price_spec["recurring"]

    try:
        client.post(f"/products/{product_id}/price", json=payload)
        return True
    except GHLAPIError as e:
        logger.error(f"  Price create failed for product {product_id}: {e}")
        return False


def create_coupon(coupon_spec: dict) -> str:
    """Create a coupon. Returns status string."""
    payload = {
        "altId": GHL_LOCATION_ID,
        "altType": "location",
        "name": coupon_spec["name"],
        "code": coupon_spec["code"],
        "discountType": coupon_spec["discountType"],
        "discountValue": coupon_spec["discountValue"],
    }
    try:
        client.post("/payments/coupon", json=payload)
        return "created"
    except GHLAPIBlocked as e:
        return f"blocked: {e.message}"
    except GHLAPIError as e:
        return f"failed: {e}"


def main():
    print("=" * 70)
    print("05 — Products & Coupons Provisioning")
    print("=" * 70)
    print_config_summary()
    print()

    spec = load_spec()
    target_products = spec["products"]
    target_coupons = spec["coupons"]
    logger.info(f"Loaded {len(target_products)} products and {len(target_coupons)} coupons from spec.")

    # ---- Products ----
    existing_products = fetch_existing_products()
    existing_by_sku = {p.get("sku"): p for p in existing_products if p.get("sku")}
    existing_by_name = {p.get("name"): p for p in existing_products if p.get("name")}
    logger.info(f"Fetched {len(existing_products)} existing products from GHL.")

    p_created, p_skipped, p_failed = 0, 0, 0
    p_failed_items, p_manual = [], []

    for prod_spec in target_products:
        sku = prod_spec.get("sku")
        name = prod_spec["name"]
        existing = existing_by_sku.get(sku) or existing_by_name.get(name)

        if existing:
            logger.debug(f"  SKIP   {sku or name}  (exists)")
            p_skipped += 1
            continue

        logger.info(f"  CREATE {sku or name}")
        product, status = create_product(prod_spec)
        if status == "created":
            p_created += 1
            product_id = product.get("id") or product.get("_id")
            # Add prices
            for price_spec in prod_spec.get("prices", []):
                if product_id:
                    if create_price(product_id, price_spec):
                        logger.info(f"    + price ${price_spec['amount'] / 100:.2f} ({price_spec.get('type', 'one_time')})")
        elif status.startswith("blocked"):
            p_manual.append((name, status))
            logger.warning(f"  ⚠️  {name}: {status}")
        else:
            p_failed += 1
            p_failed_items.append((name, status))
            logger.error(f"  ❌ {name}: {status}")

    # ---- Coupons ----
    print()
    existing_coupons = fetch_existing_coupons()
    existing_codes = {c.get("code") for c in existing_coupons if c.get("code")}
    logger.info(f"Fetched {len(existing_coupons)} existing coupons from GHL.")

    c_created, c_skipped, c_failed = 0, 0, 0
    c_manual = []

    for coup_spec in target_coupons:
        code = coup_spec["code"]
        if code in existing_codes:
            logger.debug(f"  SKIP   coupon {code}  (exists)")
            c_skipped += 1
            continue

        logger.info(f"  CREATE coupon {code}")
        status = create_coupon(coup_spec)
        if status == "created":
            c_created += 1
        elif status.startswith("blocked"):
            c_manual.append((code, coup_spec, status))
            logger.warning(f"  ⚠️  coupon {code}: {status}")
        else:
            c_failed += 1
            logger.error(f"  ❌ coupon {code}: {status}")

    # ---- Report ----
    print()
    print("=" * 70)
    logger.info(f"PRODUCTS: {p_created} created, {p_skipped} skipped, {p_failed} failed, {len(p_manual)} manual.")
    logger.info(f"COUPONS:  {c_created} created, {c_skipped} skipped, {c_failed} failed, {len(c_manual)} manual.")

    if p_manual:
        print()
        logger.warning("⚠️  PRODUCTS REQUIRING MANUAL CREATION:")
        for name, reason in p_manual:
            print(f"  - {name}  ({reason})")
        print()
        print("  📋 MANUAL: Payments > Products > + Add Product")

    if c_manual:
        print()
        logger.warning("⚠️  COUPONS REQUIRING MANUAL CREATION (Payments > Coupons > + Add):")
        for code, coup, reason in c_manual:
            print(f"  - {code} — {coup['name']}")
            print(f"      Discount: {coup['discountType']} {coup['discountValue']}{'%' if coup['discountType'] == 'percentage' else ' (cents)'}")
            print(f"      Notes: {coup.get('notes', '')}")

    print("=" * 70)
    failed_total = p_failed + c_failed
    sys.exit(0 if failed_total == 0 else 1)


if __name__ == "__main__":
    main()
