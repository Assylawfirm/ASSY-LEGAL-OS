"""Authorized review workflow with hash-chained append-only audit events.

A prototype, not a tamper-proof ledger: deployment must restrict file/database
writes and authenticate identities with a trusted identity provider.
"""
import hashlib
import json
from datetime import datetime, timezone
from approval_gate import validate_approval, ApprovalError

ALLOWED_ROLES = frozenset({"legal_reviewer", "supervising_lawyer"})
GENESIS = "0" * 64

def canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))

def authenticate_actor(actor, trusted_roles):
    if not isinstance(actor, str) or not actor or actor not in trusted_roles:
        raise PermissionError("Unknown actor")
    if trusted_roles[actor] not in ALLOWED_ROLES:
        raise PermissionError("Reviewer role required")
    return trusted_roles[actor]

def audit_event(events, actor, action, record_id, detail):
    prev = events[-1]["event_hash"] if events else GENESIS
    event = {"sequence":len(events)+1, "utc":datetime.now(timezone.utc).isoformat(),
             "actor":actor, "action":action, "record_id":record_id,
             "detail":detail, "previous_hash":prev}
    event["event_hash"] = hashlib.sha256(canonical(event).encode("utf-8")).hexdigest()
    events.append(event)
    return event

def verify_chain(events):
    previous = GENESIS
    for number, event in enumerate(events, 1):
        if event.get("sequence") != number or event.get("previous_hash") != previous:
            return False
        payload = {k:v for k,v in event.items() if k != "event_hash"}
        digest = hashlib.sha256(canonical(payload).encode("utf-8")).hexdigest()
        if digest != event.get("event_hash"):
            return False
        previous = digest
    return True

def review_decision(record, source_bytes, actor, trusted_roles, events, requested_action):
    """Record accepted/denied decisions; caller controls persistent storage.

    The permissions map must come from a trusted server or identity connector;
    never from user-provided request JSON.
    """
    role = authenticate_actor(actor, trusted_roles)
    if not verify_chain(events):
        raise ApprovalError("Audit chain tampering or corruption detected")
    if requested_action not in {"approve", "reject"}:
        raise ValueError("Invalid action")
    if not isinstance(record, dict) or not record.get("record_id"):
        raise ApprovalError("Record identifier missing")
    if requested_action == "reject":
        audit_event(events, actor, "REJECT", record["record_id"], "Reviewer rejected proposed approval")
        return {"record_id":record["record_id"],"approval_state":"REJECTED", "citation_approved":False}
    candidate={**record, "reviewer_id":actor, "reviewer_role":role}
    try:
        approved=validate_approval(candidate,source_bytes)
    except ApprovalError as error:
        audit_event(events, actor, "DENY", record["record_id"], str(error))
        return {"record_id":record["record_id"],"approval_state":"RESEARCH_ONLY", "citation_approved":False,
                "denial_reason":str(error)}
    audit_event(events, actor, "APPROVE", record["record_id"], approved["source_sha256"])
    return approved
