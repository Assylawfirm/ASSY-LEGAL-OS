# SOURCE COLLATION QUEUE — BATCH 16 (2026-10-19)
## Read-only legal research ledger; human approval required

### Legal authority
Law 147/2019, Egyptian Official Gazette issue 31 bis (W), dated 7 August 2019. Published text reproduction:
https://www.laweg.net/framePlain.aspx?ItemID=114435&NID=141378&Type=6&action=ViewActivePages
This is **not** itself an authenticated facsimile of the Official Gazette.

### Priority validation tickets
|Ticket|Target|Observed evidence|Blocking requirement|Status|
|---|---|---|---|---|
|COL-001|Law 147/2019 commencement|Article 6 in Gazette transcription states **2019-10-01**; another paid database metadata shows 2019-08-08|Obtain official Gazette scanned page and verify article six|SOURCE_CONFLICT|
|COL-002|Article 50-bis cross-reference|Gazette transcription says **(40, 50)**; independent consolidated transcription says **(49, 50)**|Visually inspect the Official Gazette as issued, plus any authentic corrigendum|SOURCE_CONFLICT|
|COL-003|Article 136 paragraph 2|Article 4 abolishes **only paragraph 2**|Check Gazette; retain all other paragraphs separately|WAITING_GAZETTE|
|COL-004|Article 30|Article 4 expressly repeals article|Check original Gazette image, record commencement|WAITING_GAZETTE|
|COL-005|Article 153|Article 4 expressly repeals article|Check original Gazette image, record commencement|WAITING_GAZETTE|
|COL-006|2019 Article 51|First paragraph replaced; second paragraph added|Compare original amendment and all subsequent legislation|WAITING_GAZETTE|
|COL-007|2019 Articles 230 and 231|Academy inserted by Article 3 of Law 147/2019|Compare official images, investigate post-2019 changes and operational rules|WAITING_GAZETTE|

### Source comparison
- Transcription labelled official Gazette: https://www.laweg.net/framePlain.aspx?ItemID=114435&NID=141378&Type=6&action=ViewActivePages
- Article 50-bis '(49,50)' in private consolidated text: https://lawhub.info/eg/?p=383
- Article 50-bis '(40,50)' appears in bar association commentary: https://egyls.com/ومضة-قانون-52-الْكِيَان-الْمُقَدَّس/
- Metadata discrepancy (2019-08-08): https://www.eastlaws.com/legislation-full-text/ar/egypt/law/07-08-2019/no-147?id=1948863&sub=9663869&type=1

### Binding use restriction
Until primary official image review, each legislative record retains full_text=null and citation_approved=false. Record text, amendment chain, official gazette issue/date/page, verifier and approval timestamp before flipping approval.

### Change management
Append-only source references and issue notes. Do not overwrite historically applicable versions of a statute. Store distinction among publication, law commencement and operational implementation dates.
