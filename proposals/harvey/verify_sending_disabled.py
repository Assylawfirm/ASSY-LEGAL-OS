#!/usr/bin/env python3
"""Fail closed if Harvey effective config would allow outbound mail.
Uses only Python standard library for the static checks. Requires PyYAML for parsing.
No network calls, credentials, or email.
"""
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    sys.exit("BLOCKED: PyYAML missing; install reviewed dependencies first")

root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
local = root / "harvey.local.yaml"
base = root / "harvey.yaml"
path = local if local.exists() else base
if not path.exists():
    sys.exit("BLOCKED: no Harvey config")
config = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
email = ((config.get("channels") or {}).get("email") or {})
checks = {
    "email channel disabled": email.get("enabled") is False,
    "manual approval required": email.get("require_approval") is True,
    "daily sends zero": email.get("max_daily_sends") == 0,
    "LinkedIn disabled": ((config.get("channels") or {}).get("linkedin") or {}).get("enabled") is False,
}
for name, ok in checks.items():
    print(("PASS" if ok else "BLOCK") + ": " + name)
if not all(checks.values()):
    sys.exit("BLOCKED: do not run Harvey until all checks pass")
print("STATIC CONFIG CHECK PASS — this does not prove runtime cannot send.")
