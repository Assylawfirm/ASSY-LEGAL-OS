#!/usr/bin/env python3
"""ASSY LEGAL OS – export research-only legal records.
Usage: python export_verified_data.py advocacy_law_audit.sqlite advocacy_research.json
"""
import sqlite3, json, sys
from pathlib import Path

TABLES = ("sources", "articles", "amendments", "audit_findings", "precedents", "procedural_defenses")

def export_database(database):
    connection = sqlite3.connect(f"file:{Path(database).resolve()}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    records = {table: [dict(row) for row in connection.execute(f"SELECT * FROM {table}")] for table in TABLES}
    connection.close()
    for article in records["articles"]:
        article["citation_approved"] = False
        article["approval_state"] = "awaiting_official_gazette_collation"
    for precedent in records["precedents"]:
        precedent["citation_approved"] = False
        precedent["approval_state"] = "awaiting_primary_court_decision"
    return {"schema": "assy.advocacy-law.research.v1", "as_of": "2026-10-19",
            "notice": "UNVERIFIED RESEARCH MATERIAL — NOT FOR AUTOMATED COURT CITATION",
            "records": records}

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: export_verified_data.py DATABASE.sqlite OUTPUT.json")
    output = export_database(sys.argv[1])
    Path(sys.argv[2]).write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print({table:len(rows) for table,rows in output["records"].items()})
