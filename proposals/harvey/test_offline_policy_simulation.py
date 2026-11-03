"""Offline fail-closed policy simulation. Never imports or starts Harvey."""
import dataclasses
import unittest

@dataclasses.dataclass(frozen=True)
class SyntheticLead:
    email: str
    consent: bool = False

class DeniedNetwork:
    def __init__(self):
        self.attempts = []
    def send(self, recipient, body):
        self.attempts.append((recipient, body))
        raise AssertionError("OUTBOUND_NETWORK_DENIED")

class PilotGate:
    def __init__(self, transport, *, enabled=False, daily_limit=0, require_approval=True):
        self.transport = transport
        self.enabled = enabled
        self.daily_limit = daily_limit
        self.require_approval = require_approval
        self.sent = 0
    def submit(self, lead, body, approved=False):
        if not self.enabled or self.daily_limit <= self.sent:
            return "BLOCKED"
        if self.require_approval and not approved:
            return "BLOCKED"
        if not lead.consent:
            return "BLOCKED"
        return self.transport.send(lead.email, body)

class TestOfflinePilotPolicy(unittest.TestCase):
    def setUp(self):
        self.network = DeniedNetwork()
        self.lead = SyntheticLead("synthetic@example.invalid")
    def test_default_never_calls_transport(self):
        gate = PilotGate(self.network)
        self.assertEqual(gate.submit(self.lead, "synthetic"), "BLOCKED")
        self.assertEqual(self.network.attempts, [])
    def test_approval_cannot_override_disabled(self):
        gate = PilotGate(self.network)
        self.assertEqual(gate.submit(self.lead, "synthetic", approved=True), "BLOCKED")
        self.assertEqual(self.network.attempts, [])
    def test_positive_daily_limit_cannot_override_disabled(self):
        gate = PilotGate(self.network, daily_limit=100)
        self.assertEqual(gate.submit(self.lead, "synthetic", approved=True), "BLOCKED")
        self.assertEqual(self.network.attempts, [])
    def test_missing_approval_blocked(self):
        gate = PilotGate(self.network, enabled=True, daily_limit=1)
        self.assertEqual(gate.submit(self.lead, "synthetic"), "BLOCKED")
        self.assertEqual(self.network.attempts, [])
    def test_missing_consent_blocked(self):
        gate = PilotGate(self.network, enabled=True, daily_limit=1)
        self.assertEqual(gate.submit(self.lead, "synthetic", approved=True), "BLOCKED")
        self.assertEqual(self.network.attempts, [])
    def test_network_denied_even_when_all_checks_bypassed(self):
        gate = PilotGate(self.network, enabled=True, daily_limit=1)
        lead = SyntheticLead("synthetic@example.invalid", consent=True)
        with self.assertRaisesRegex(AssertionError, "OUTBOUND_NETWORK_DENIED"):
            gate.submit(lead, "synthetic", approved=True)
        self.assertEqual(len(self.network.attempts), 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
