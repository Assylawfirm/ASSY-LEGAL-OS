#!/usr/bin/env python3
"""Run: python -m unittest discover -s legal_research/advocacy_law -p 'test_*.py'
Set ASSY_ADVOCACY_DB to local SQLite path.
"""
import os,unittest
from pathlib import Path
from export_verified_data import export_database

class LegalIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        db=os.environ.get("ASSY_ADVOCACY_DB")
        if not db or not Path(db).is_file():
            raise unittest.SkipTest("Set ASSY_ADVOCACY_DB to a real local SQLite database")
        cls.records=export_database(db)["records"]
    def test_approval_gate(self):
        self.assertTrue(all(not r["citation_approved"] for t in ("articles","precedents") for r in self.records[t]))
    def test_empty_full_text_not_citable(self):
        self.assertTrue(all(not r.get("full_text") for r in self.records["articles"]))
    def test_ids_unique(self):
        for table,key in (("articles","article_id"),("precedents","id"),("procedural_defenses","id")):
            values=[r[key] for r in self.records[table]]
            self.assertEqual(len(values),len(set(values)))
    def test_2019_effective_date(self):
        rows=[x for x in self.records["amendments"] if x["act"]=="147/2019"]
        self.assertTrue(rows)
        self.assertTrue(all(x["effective_date"]=="2019-10-01" for x in rows))
if __name__=="__main__":unittest.main()
