"""
Sunrise Wellness Studio — Provisioning Configuration

Loads credentials and runtime flags from a local `.env` file (see `.env.example`).
Validates that required vars are set; fails loud on import if missing.

Required env vars:
    GHL_API_KEY        — Your sub-account API key (Sub-account > Settings > Business Profile > API Key)
    GHL_LOCATION_ID    — Your sub-account location ID (Sub-account URL contains it: /location/{LOCATION_ID}/...)

Optional env vars:
    GHL_BASE_URL       — Default: https://services.leadconnectorhq.com  (GHL v2 API)
    GHL_API_VERSION    — Default: 2021-07-28
    LOG_LEVEL          — Default: INFO  (DEBUG | INFO | WARNING | ERROR)
    DRY_RUN            — Default: false  (true = print intended mutations without executing)
    RATE_LIMIT_DELAY   — Default: 0.2  (seconds between API calls — be polite to GHL)
"""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv

# Load .env from the same directory as this file
ENV_PATH = Path(__file__).parent / ".env"
load_dotenv(ENV_PATH)

# --- Required ---
GHL_API_KEY = os.getenv("GHL_API_KEY", "").strip()
GHL_LOCATION_ID = os.getenv("GHL_LOCATION_ID", "").strip()

# --- Optional with defaults ---
GHL_BASE_URL = os.getenv("GHL_BASE_URL", "https://services.leadconnectorhq.com").rstrip("/")
GHL_API_VERSION = os.getenv("GHL_API_VERSION", "2021-07-28")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
DRY_RUN = os.getenv("DRY_RUN", "false").lower() in ("true", "1", "yes")
RATE_LIMIT_DELAY = float(os.getenv("RATE_LIMIT_DELAY", "0.2"))


def _validate():
    """Validate required env vars are present. Called automatically on import."""
    missing = []
    if not GHL_API_KEY or GHL_API_KEY.startswith("your-"):
        missing.append("GHL_API_KEY")
    if not GHL_LOCATION_ID or GHL_LOCATION_ID.startswith("your-"):
        missing.append("GHL_LOCATION_ID")

    if missing:
        print("=" * 70, file=sys.stderr)
        print("ERROR: Missing required environment variables:", file=sys.stderr)
        for var in missing:
            print(f"  - {var}", file=sys.stderr)
        print("", file=sys.stderr)
        print(f"Fix: create a `.env` file at {ENV_PATH}", file=sys.stderr)
        print(f"Copy `.env.example` and fill in your sandbox sub-account credentials.", file=sys.stderr)
        print("=" * 70, file=sys.stderr)
        sys.exit(1)


def get_headers():
    """Standard headers for GHL v2 API requests."""
    return {
        "Authorization": f"Bearer {GHL_API_KEY}",
        "Content-Type": "application/json",
        "Version": GHL_API_VERSION,
        "Accept": "application/json",
    }


def redact_key(value: str) -> str:
    """Mask the API key for safe logging."""
    if not value or len(value) < 8:
        return "***"
    return value[:4] + "..." + value[-4:]


def print_config_summary():
    """Print non-sensitive config for confirmation. Never prints the API key."""
    print(f"GHL Base URL:    {GHL_BASE_URL}")
    print(f"GHL API Version: {GHL_API_VERSION}")
    print(f"Location ID:     {redact_key(GHL_LOCATION_ID)}")
    print(f"API Key:         {redact_key(GHL_API_KEY)}")
    print(f"Log Level:       {LOG_LEVEL}")
    print(f"Dry Run:         {DRY_RUN}")
    print(f"Rate Limit:      {RATE_LIMIT_DELAY}s between calls")


# Validate on import — fail fast
_validate()
