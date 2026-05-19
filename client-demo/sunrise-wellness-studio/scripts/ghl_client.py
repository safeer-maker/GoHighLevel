"""
Sunrise Wellness Studio — GHL HTTP Client

Thin wrapper around `requests` providing:
  - Auth (Bearer + Version header) via config.get_headers()
  - Logging (Python logging module, redacts auth headers)
  - Retry/backoff for 429 (rate limit) and 5xx (server error)
  - Dry-run mode (mutating calls log instead of fire)
  - Auto-pagination for list endpoints
  - find_or_create() idempotency helper

All provisioning scripts should use GHLClient — never call requests directly.
"""

import logging
import sys
import time
from typing import Any, Callable, Dict, List, Optional, Tuple

import requests

from config import (
    DRY_RUN,
    GHL_BASE_URL,
    GHL_LOCATION_ID,
    LOG_LEVEL,
    RATE_LIMIT_DELAY,
    get_headers,
)


# --- Logging setup ---------------------------------------------------------

logger = logging.getLogger("sunrise.ghl")
if not logger.handlers:
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    ))
    logger.addHandler(handler)
logger.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))


# --- Exceptions ------------------------------------------------------------

class GHLAPIError(Exception):
    """Raised when GHL returns an error we can't recover from."""

    def __init__(self, status: int, message: str, url: str = "", body: Any = None):
        self.status = status
        self.message = message
        self.url = url
        self.body = body
        super().__init__(f"[{status}] {url} — {message}")


class GHLAPIBlocked(GHLAPIError):
    """Raised when the API doesn't support this operation (403/404 on a documented endpoint).
    Scripts should catch this and emit a manual UI fallback message."""


# --- The client ------------------------------------------------------------

class GHLClient:
    """HTTP client for the GHL v2 API.

    Usage:
        client = GHLClient()
        existing = client.get_paginated("/locations/{loc}/customValues", item_key="customValues")
        new = client.post("/locations/{loc}/customValues", json={"name": "...", "value": "..."})
    """

    MAX_RETRIES = 4
    RETRY_BACKOFF_BASE = 1.5  # seconds; doubles each retry

    def __init__(self, base_url: str = GHL_BASE_URL, location_id: str = GHL_LOCATION_ID):
        self.base_url = base_url.rstrip("/")
        self.location_id = location_id
        self.dry_run = DRY_RUN
        # Counters for end-of-run reporting
        self.counters = {"created": 0, "updated": 0, "skipped": 0, "failed": 0}

    # --- Internals --------------------------------------------------------

    def _url(self, path: str) -> str:
        """Resolve a path with {loc} placeholder to a full URL."""
        path = path.replace("{loc}", self.location_id).replace("{location_id}", self.location_id)
        if not path.startswith("/"):
            path = "/" + path
        return f"{self.base_url}{path}"

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        is_mutation: bool = False,
        retries: int = MAX_RETRIES,
    ) -> requests.Response:
        """Internal: perform a request with logging, retry, and rate limiting."""
        url = self._url(path)

        if is_mutation and self.dry_run:
            logger.info(f"[DRY-RUN] {method} {url}")
            if json is not None:
                logger.debug(f"  payload: {json}")
            # Return a fake response with 200 OK and empty body
            return _DryRunResponse(method, url, json)

        attempt = 0
        while True:
            attempt += 1
            try:
                start = time.time()
                resp = requests.request(
                    method=method,
                    url=url,
                    headers=get_headers(),
                    params=params,
                    json=json,
                    timeout=30,
                )
                latency_ms = int((time.time() - start) * 1000)
                logger.debug(f"{method} {url} -> {resp.status_code} ({latency_ms}ms)")

                # Success
                if 200 <= resp.status_code < 300:
                    # Polite delay between calls
                    if RATE_LIMIT_DELAY > 0 and is_mutation:
                        time.sleep(RATE_LIMIT_DELAY)
                    return resp

                # Rate limited
                if resp.status_code == 429 and attempt < retries:
                    retry_after = float(resp.headers.get("Retry-After", self.RETRY_BACKOFF_BASE ** attempt))
                    logger.warning(f"429 rate-limited. Sleeping {retry_after:.1f}s before retry {attempt}/{retries}.")
                    time.sleep(retry_after)
                    continue

                # Server error
                if 500 <= resp.status_code < 600 and attempt < retries:
                    backoff = self.RETRY_BACKOFF_BASE ** attempt
                    logger.warning(f"{resp.status_code} server error. Backoff {backoff:.1f}s, retry {attempt}/{retries}.")
                    time.sleep(backoff)
                    continue

                # Non-retryable
                body_preview = resp.text[:300] if resp.text else ""
                if resp.status_code == 401:
                    raise GHLAPIError(401, "Unauthorized — check GHL_API_KEY in .env", url, body_preview)
                if resp.status_code == 403:
                    raise GHLAPIBlocked(403, "Forbidden — API access not enabled or endpoint not allowed for this plan", url, body_preview)
                if resp.status_code == 404:
                    raise GHLAPIError(404, "Not Found", url, body_preview)
                raise GHLAPIError(resp.status_code, body_preview or "Unknown error", url, body_preview)

            except requests.exceptions.RequestException as e:
                if attempt < retries:
                    backoff = self.RETRY_BACKOFF_BASE ** attempt
                    logger.warning(f"Network error: {e}. Backoff {backoff:.1f}s, retry {attempt}/{retries}.")
                    time.sleep(backoff)
                    continue
                raise GHLAPIError(0, f"Network error after {retries} attempts: {e}", url)

    # --- Public methods ---------------------------------------------------

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """GET request. Returns parsed JSON dict."""
        resp = self._request("GET", path, params=params, is_mutation=False)
        return resp.json() if resp.text else {}

    def post(self, path: str, json: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST request (mutating). Returns parsed JSON dict."""
        resp = self._request("POST", path, json=json, is_mutation=True)
        return resp.json() if resp.text else {}

    def put(self, path: str, json: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """PUT request (mutating). Returns parsed JSON dict."""
        resp = self._request("PUT", path, json=json, is_mutation=True)
        return resp.json() if resp.text else {}

    def delete(self, path: str) -> Dict[str, Any]:
        """DELETE request (mutating). Returns parsed JSON dict."""
        resp = self._request("DELETE", path, is_mutation=True)
        return resp.json() if resp.text else {}

    def get_paginated(
        self,
        path: str,
        *,
        item_key: str,
        params: Optional[Dict[str, Any]] = None,
        limit: int = 100,
        max_pages: int = 100,
    ) -> List[Dict[str, Any]]:
        """GET with auto-pagination. Returns a flat list from `item_key` across all pages.

        Tries common pagination patterns:
          1. ?limit=N&offset=M  (used by /contacts/, /opportunities/)
          2. ?limit=N&startAfter=... (cursor-based)
          3. Single-page (no pagination)
        """
        params = dict(params or {})
        params.setdefault("locationId", self.location_id)
        params["limit"] = limit

        all_items: List[Dict[str, Any]] = []
        offset = 0
        page = 0

        while page < max_pages:
            page += 1
            params["offset"] = offset
            try:
                data = self.get(path, params=params)
            except GHLAPIError as e:
                # If pagination param is rejected, fall back to single GET
                if e.status == 400 and "offset" in params:
                    params.pop("offset", None)
                    data = self.get(path, params=params)
                else:
                    raise

            items = data.get(item_key, []) if isinstance(data, dict) else []
            if not isinstance(items, list):
                items = []
            all_items.extend(items)

            if len(items) < limit:
                break
            offset += limit

        return all_items

    def find_or_create(
        self,
        list_path: str,
        item_key: str,
        match_key: str,
        match_value: Any,
        create_path: str,
        create_payload: Dict[str, Any],
        existing: Optional[List[Dict[str, Any]]] = None,
    ) -> Tuple[Dict[str, Any], str]:
        """Idempotency helper.

        1. Fetch all existing items from list_path (or use provided list).
        2. Find one matching match_key == match_value.
        3. If found: return (item, "skipped").
        4. If not found: POST create_payload to create_path. Return (new_item, "created").

        Returns: (item_dict, status) where status is "created" | "skipped" | "failed".
        """
        if existing is None:
            existing = self.get_paginated(list_path, item_key=item_key)

        for item in existing:
            if item.get(match_key) == match_value:
                self.counters["skipped"] += 1
                return item, "skipped"

        try:
            new_item = self.post(create_path, json=create_payload)
            self.counters["created"] += 1
            return new_item, "created"
        except GHLAPIError as e:
            self.counters["failed"] += 1
            logger.error(f"Failed to create {match_value}: {e}")
            return {}, "failed"

    def print_summary(self, label: str = "Summary"):
        """Print end-of-run counters."""
        c = self.counters
        logger.info(
            f"{label}: {c['created']} created, {c['updated']} updated, "
            f"{c['skipped']} skipped, {c['failed']} failed"
        )


# --- Dry-run fake response -------------------------------------------------

class _DryRunResponse:
    """Stand-in for a real Response when DRY_RUN is enabled."""

    def __init__(self, method: str, url: str, payload: Any):
        self.status_code = 200
        self._payload = payload or {}
        self.text = '{"dry_run": true}'
        self.headers: Dict[str, str] = {}
        # Fake an ID for chained logic
        self._payload = {"id": "dry-run-id", "dryRun": True, **(payload or {})}

    def json(self) -> Dict[str, Any]:
        return self._payload


# --- Convenience: a default client other scripts can import ---------------

client = GHLClient()


# --- Smoke test (run this file directly to verify connection) -------------

def smoke_test() -> bool:
    """Verify API connectivity and credentials. Returns True on success."""
    logger.info("Running smoke test against GHL API…")
    try:
        # Cheapest possible endpoint: list 1 contact
        resp = client.get("/contacts/", params={"locationId": GHL_LOCATION_ID, "limit": 1})
        contacts = resp.get("contacts", [])
        logger.info(f"Connection OK. Account has at least {len(contacts)} contact(s) visible.")
        return True
    except GHLAPIError as e:
        logger.error(f"Smoke test FAILED: {e}")
        if e.status == 401:
            logger.error("  → Your GHL_API_KEY is invalid or expired.")
        elif e.status == 403:
            logger.error("  → API access not enabled for this sub-account.")
            logger.error("  → Ask your agency admin to enable API access, or create a Private App.")
        return False


if __name__ == "__main__":
    from config import print_config_summary

    print("=" * 70)
    print("Sunrise Wellness Provisioning — Configuration")
    print("=" * 70)
    print_config_summary()
    print("=" * 70)
    ok = smoke_test()
    sys.exit(0 if ok else 1)
