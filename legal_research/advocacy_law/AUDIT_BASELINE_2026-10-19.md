# ASSY LEGAL OS — Advocacy Law Audit (Egypt)
 
Audit baseline dated 2026-10-19. **Research-stage only: not an authoritative consolidated statute and not cleared for litigation.**

## Verified legislative facts
- Act 17/1983 is the foundation; see https://manshurat.org/node/29059
- Amendments index: Acts 227/1984, 98/1992, 10/2002, 197/2008, 147/2019: https://manshurat.org/node/29059/relations
- Act 147/2019 published 2019-08-07 and **effective 2019-10-01** under article 6: https://www.laweg.net/framePlain.aspx?ItemID=114435&NID=141378&Type=6&action=ViewActivePages
- Act 147/2019 repealed **article 30**, **article 136 paragraph two only**, and **article 153** under article 4.
- It substituted the following provisions: 13(1,3);14(1);24;51(1);99(1,2);103;128;129;131;135-bis(3);143;144;152;156-bis;187;196(2).
- It added article 13-bis, article 50-bis, paragraphs to articles 51 and 62, and articles 230–231.
- Article 50-bis in the reproduced official-gazette text references 40 and 50. **Do not silently change the cross-reference to 49**; investigate original legislative printing/corrigenda.
- The bar website consolidated text is labeled last amended as of July 8, 2020: https://egyls.com/قانون-المحاماة/

## Rectifications of earlier study
1. Article 153 had been described as operative: incorrect; repealed in 2019.
2. Article 136 was discussed without noting its second paragraph repeal.
3. Do not use 2019-08-08 as the effective date of Act 147/2019.
4. Articles 1–231 have only initial summaries, not completed gazette-level collation or comprehensive case-law verification.
5. Distinguish historical sums/fees from currently enforceable amounts.
6. Never cite a case unless case number, court, date, dispositive text and publication/source have been checked.

## Data model, ready for integration
Tables: `sources`, `articles`, `amendments`, `audit_findings`, `precedents`; FTS5 article search. SQLite prototype and exports supplied with the chat deliverable. Records without verified complete text have `full_text=NULL` and an explicit review status.

## Human review gate
Prior to judicial or client reliance, collate each article against its official gazette version, chain later amendments and authoritative judicial decisions, and sign off each record. No invented verbatim text.

## Integration status
This repository document is the first actual GitHub integration artifact. The offline SQLite prototype remains a separate downloadable deliverable until deliberately imported into the application's runtime.
