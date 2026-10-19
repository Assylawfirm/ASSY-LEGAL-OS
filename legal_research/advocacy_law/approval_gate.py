"""Fail-closed legal citation approval gate for ASSY LEGAL OS.

Records are untrusted inputs; only independently reviewed primary-source evidence
can be approved. This module does not grant reviewer authority or sign records.
"""
import hashlib
import re
from datetime import date

APPROVED = "VERIFIED_CITABLE"
SHA256_RE = re.compile(r"^[a-f0-9]{64}$")

class ApprovalError(ValueError):
    pass

def validate_approval(record, source_bytes=None):
    """Return sanitized approved record, or raise ApprovalError.

    source_bytes: actual official source file bytes, supplied by an authorized
    ingestion process. A claimed digest alone is NOT sufficient.
    """
    if not isinstance(record, dict):
        raise ApprovalError("invalid record")
    reasons = []
    required = ("record_id", "record_type", "primary_source_type",
                "primary_source_url", "official_reference", "source_sha256",
                "source_page", "exact_text", "effective_date",
                "reviewer_id", "reviewer_role", "reviewed_at",
                "amendments_checked", "conflicts_open", "human_approval")
    for key in required:
        if key not in record or record[key] is None or record[key] == "":
            reasons.append("missing " + key)
    if record.get("record_type") not in ("legislation", "judgment"):
        reasons.append("unsupported record type")
    if record.get("primary_source_type") not in ("official_gazette", "official_court"):
        reasons.append("unverified source type")
    if record.get("conflicts_open") is not False:
        reasons.append("open or unknown source conflicts")
    if record.get("amendments_checked") is not True:
        reasons.append("amendment review missing")
    if record.get("human_approval") is not True:
        reasons.append("explicit human approval missing")
    if record.get("citation_approved") is True:
        reasons.append("input must not pre-approve itself")
    digest = record.get("source_sha256")
    if not isinstance(digest, str) or not SHA256_RE.fullmatch(digest):
        reasons.append("invalid SHA256")
    if not isinstance(source_bytes, bytes) or not source_bytes:
        reasons.append("original source bytes missing")
    elif isinstance(digest, str) and hashlib.sha256(source_bytes).hexdigest() != digest:
        reasons.append("source SHA256 mismatch")
    for field in ("record_id", "official_reference", "primary_source_url", "reviewer_id", "reviewer_role", "exact_text"):
        if not isinstance(record.get(field), str) or not record[field].strip():
            reasons.append("invalid " + field)
    url = record.get("primary_source_url")
    if not isinstance(url, str) or not url.startswith("https://"):
        reasons.append("primary source HTTPS URL required")
    page = record.get("source_page")
    if not isinstance(page, int) or isinstance(page, bool) or page < 1:
        reasons.append("invalid source page")
    for field in ("effective_date", "reviewed_at"):
        value = record.get(field)
        try:
            date.fromisoformat(value)
        except (TypeError, ValueError):
            reasons.append("invalid " + field)
    if reasons:
        raise ApprovalError("; ".join(dict.fromkeys(reasons)))
    return {**record, "approval_state": APPROVED, "citation_approved": True}
