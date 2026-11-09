# Consolidation, Quality and Release Matrix / مصفوفة التجميع والجودة والإصدار
Directive: ASLOS-LANG-AR-EN-001 | 2026-11-09 | STATUS: PLANNED, NOT RELEASED

| System / النظام | Required actions / المطلوب | Acceptance evidence / دليل القبول | Status |
|---|---|---|---|
| ASSY LEGAL OS | bilingual UI/API-facing text, legal templates, source-controlled termbase / واجهات ونماذج ومعجم | file inventory + QA logs | PENDING |
| Sovereign Archive Organizer | bilingual metadata, document indexing and retrieval without modifying originals / وصف ثنائي اللغة مع حفظ الأصول | fixtures + regression tests | PENDING |
| Government Service Registry | bilingual service names, authoritative sources, no double count / خدمات موثقة بلا تكرار | source audit + service reconciliations | PENDING |
| E-Court PRJ-028 | court vocabulary, filing labels, procedural validation / مصطلحات التقاضي | legal sign-off | PENDING |
| Digital Front Door PRJ-005 | bilingual site navigation, contact, intake disclosures / الموقع والاستقبال | accessibility + live-site audit | PENDING |
| Identity PRJ-004 | brand-locked translated descriptions / الهوية الموحدة | brand owner approval | PENDING |
| Directory PRJ-036 | bilingual professional listings / الدليل المهني | validation of names and professional titles | PENDING |
| Knowledge base | parallel AR/EN fields, Arabic-original supremacy / أساس معرفي ثنائي | traceability + bilingual semantic review | PENDING |
| Media and sales | bilingual scripts, captions, offers, fee clarity / التسويق والمبيعات | approved content samples | PENDING |
| Git/GitHub/CI | review branch, PR checks, branch protection / حوكمة الأكواد | passing CI + peer review | PENDING |
| Codex and other AI agents | governed prompt/config templates, source citation and language QA / تعليمات الوكلاء | controlled tests, logs, human review | PENDING |
| External sites/apps | permissioned audit and release / مراجعة المواقع المتصلة | access proof + screenshots + smoke tests | PENDING |

## Gate sequence / تسلسل الاعتماد
G0 ASSET INVENTORY / جرد الأصول
G1 SOURCE PROVENANCE / إثبات المصادر
G2 TERMINOLOGY & TRANSLATION / تدقيق المصطلحات والترجمة
G3 CODE + RTL/LTR + SECURITY TESTS / اختبارات الكود والواجهات والأمان
G4 INTEGRATION + UAT / التكامل والقبول
G5 HUMAN LEGAL, EDITORIAL AND BRAND SIGN-OFF / الاعتماد البشري
G6 DEPLOYMENT READINESS / جاهزية النشر
G7 COMMERCIAL READINESS / الجاهزية للبيع
No gate is marked passed by creation of this matrix. / لا تُعد أي بوابة مجتازة لمجرد إنشاء هذه المصفوفة.

## Non-destructive rollout / إطلاق غير هدّام
Audit before editing; prefer review branches and pull requests. Preserve existing approved originals. Never auto-translate evidence, law, judgments or signed agreements. For production changes require verified rollback, backup, access rights, security review, acceptance tests and explicit authorized approval.

## Initial audit evidence / أدلة الجرد الأولي
- GitHub accessible repositories: Assylawfirm/ASSY-LEGAL-OS (public, main), Assylawfirm/ASSY_Sovereign_Archive_Organizer (private, main).
- Archive README lists assy_archive, scripts, tests, and 40_DIGITAL_PLATFORM/MVP_01_LEGAL_CONTENT_PLATFORM. README is descriptive; tests were not run.
- GitHub keyword searches for locale and i18n returned no hits; this does not establish absence of localization throughout either repository.
- Drive canonical document updated with section 25; no other Google documents or external websites modified.
