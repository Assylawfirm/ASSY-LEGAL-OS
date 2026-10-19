#!/usr/bin/env python3
"""Fail closed: check the committed public research index without approving citations."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
data=json.loads((ROOT/"research_index_v13.json").read_text(encoding="utf-8"))
assert data["schema"]=="assy-law-index.v13"
assert data["as_of"]=="2026-10-19"
articles=data["articles"]
assert len(articles)==238, f"Expected 238 index entries; found {len(articles)}"
ids=[a["article_id"] for a in articles]
numbers=[a["number"] for a in articles]
assert len(set(ids))==len(ids),"Duplicate article identifiers"
assert len(set(numbers))==len(numbers),"Duplicate article numbers"
assert {str(n) for n in range(1,232)} <= set(numbers)
assert all(a["citation_approved"] is False for a in articles),"Unreviewed law text may not be citable"
assert all(a["text"] is None for a in articles),"No official text has been verified yet"
assert all(c["citation_approved"] is False and c["primary_verified"] is False for c in data["cases"])
assert all(a["status"]=="repealed_research" for a in articles if a["number"] in ("30","153"))
assert len(data["cases"])==5
html=(ROOT/"index.html").read_text(encoding="utf-8")
assert 'research_index_v13.json' in html
assert "citation_approved" in (ROOT/"research_index_v13.json").read_text(encoding="utf-8")
print("PASS: 238 article indexes, 5 provisional cases, no citation approvals, linked HTML.")
