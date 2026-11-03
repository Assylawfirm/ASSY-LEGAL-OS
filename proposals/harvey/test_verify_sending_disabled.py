"""Offline tests for pilot config gate; fake YAML only, no network/email."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

GATE = Path(__file__).with_name("verify_sending_disabled.py")
SAFE = """channels:
  email:
    enabled: false
    require_approval: true
    max_daily_sends: 0
  linkedin:
    enabled: false
"""

class GateTests(unittest.TestCase):
    def check(self, base=SAFE, local=None):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "harvey.yaml").write_text(base, encoding="utf-8")
            if local is not None:
                (root / "harvey.local.yaml").write_text(local, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(GATE), str(root)],
                text=True, capture_output=True, check=False,
            )

    def test_safe_passes(self):
        self.assertEqual(self.check().returncode, 0)

    def test_email_enabled_blocked(self):
        self.assertNotEqual(self.check(SAFE.replace("enabled: false", "enabled: true", 1)).returncode, 0)

    def test_approval_disabled_blocked(self):
        self.assertNotEqual(self.check(SAFE.replace("require_approval: true", "require_approval: false")).returncode, 0)

    def test_daily_limit_positive_blocked(self):
        self.assertNotEqual(self.check(SAFE.replace("max_daily_sends: 0", "max_daily_sends: 1")).returncode, 0)

    def test_linkedin_enabled_blocked(self):
        self.assertNotEqual(self.check(SAFE.replace("  linkedin:\n    enabled: false", "  linkedin:\n    enabled: true")).returncode, 0)

    def test_local_override_blocked(self):
        self.assertNotEqual(self.check(local=SAFE.replace("max_daily_sends: 0", "max_daily_sends: 5")).returncode, 0)

    def test_malformed_yaml_blocked(self):
        self.assertNotEqual(self.check("channels: [broken").returncode, 0)

if __name__ == "__main__":
    unittest.main()
