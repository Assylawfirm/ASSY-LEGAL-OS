# ASSY-SA-ESTATE-2026-001 — محضر حصر وجرد تركة شامل

- **Jurisdiction:** Saudi Arabia (KSA)
- **Knowledge status:** APPROVED AS KNOWLEDGE BASELINE / REVIEW ONLY
- **Version:** 1.0
- **Approval date:** 2026-11-18
- **Classification:** Estate / inheritance inventory template
- **Source:** User-approved Arabic Word document, `محضر_حصر_وجرد_تركة_شامل.docx` (conversation attachment, not stored in this public repository)
- **SHA-256:** `74dfc9890a9b6204a4ac69b06db038b94dab0fb9c1823c67aa69b00e5c0295cc`
- **File structure observed:** 12 numbered sections, 22 tables.
- **Owner:** ASSY LAW FIRM / مستشارك الشخصي في السعودية
- **Confidentiality:** Public-safe template metadata only. No deceased-person, heir, account or client records here.

## Scope (verified from the document)
1. بيانات المتوفى والمحضر
2. ضوابط الجرد والتوثيق
3. الفهرس الرئيسي للفئات: A cash/accounts/deposits; B property; C chattels/vehicles; D securities; E companies; F receivables; G employment/insurance entitlements; H digital/IP; I foreign assets; J co-owned/disputed/later-discovered assets.
4. البطاقة التفصيلية للأصل
5. الديون والالتزامات
6. الوصايا والاستحقاقات الخاصة والتحفظات
7. المخاطبات والاستعلامات
8. حركة الأموال والتسليم والاستلام
9. المكتشف لاحقًا والتعديلات
10. الملخص المالي
11. المرفقات
12. الإقرار والتوقيعات

## Data model registration proposal
See `estate-inventory.template-record.v1.json` for a structured, import-ready metadata record. This is **NOT** evidence of a database INSERT or a deployed schema. Do not create new database tables or perform migrations before identifying and reviewing the production schema, access control and backups.

## Controls and acceptance
- A single case-specific copy must be created per deceased person with unique matter identifier.
- No PII or credentials in GitHub (especially this PUBLIC repository).
- Reviewer must validate legal basis, ownership evidence, liability offsets, and applicable current Saudi norms.
- Distinguish not-found / not-verified from verified nonexistence.
- Restrict case details and attachments to authorized roles; preserve append-only audit and version history.
- **PRE-PRODUCTION / NO-GO** for deployment, merge to main, live database writing, automated client processing, and publication.
- Evidence for actual database registration: connection target, schema/table, transaction identifier, record ID, and read-back proof. None exists yet.

## Change control
This is a documentary proposal on a review branch. Human approval, security/legal review, successful tests, a verified recovery path and separate production authorization are required before merge or deployment.
