# ASSY LEGAL OS — Bilingual Legal Language Governance / سياسة الحوكمة القانونية ثنائية اللغة
Policy ID: ASLOS-LANG-AR-EN-001 | Version: 1.0 | Effective decision: 2026-11-09 | Status: APPROVED_AS_POLICY / IMPLEMENTATION_PENDING_QA

## 1. Mandatory scope / نطاق الإلزام
AR: تُنتج جميع المخرجات الجديدة للمنظومة بالعربية القانونية المصرية والإنجليزية القانونية الدقيقة، بما فيها الواجهات والتقارير والقوالب والمراسلات ونصوص المساعدة والواجهات البرمجية الموجهة للبشر والملفات المعرفية والاختبارات والمحتوى التسويقي. تُحفظ النصوص التشريعية والأحكام والأدلة والأوامر البرمجية كما وردت دون ترجمة تستبدل الأصل؛ وتضاف ترجمة شارحة موثقة بجانب الأصل. لا تُعد ترجمة النص القانوني بديلًا عن صيغته الرسمية.
EN: All new human-facing system outputs must include accurate Egyptian legal Arabic and legal English: UI, reports, templates, client communications, help, human-facing API descriptions, knowledge records, tests and commercial copy. Preserve original statutes, judgments, evidence, identifiers and executable syntax verbatim; add an attributed translation alongside, never in place of the controlling original. A translation is not an official legal text.

## 2. Quality and precedence / الجودة والأولوية
AR: القانون المصري بصيغته المنشورة رسميًا هو المرجع الحاكم في مسائل القانون المصري؛ تُترجم المصطلحات بحسب السياق ونوع الإجراء، ولا يُنقل اصطلاح من نظام القانون العام باعتباره معادلًا تشريعيًا تلقائيًا. عند التعارض يعرض الأصل والاختلاف للمراجعة البشرية.
EN: The officially published Arabic Egyptian legal text controls Egyptian-law issues. Translate concepts contextually; common-law analogies must not be treated as exact statutory equivalents. Flag ambiguity and conflicts for human legal review.
AR/EN publication requires: source traceability, termbase review, independent language QA, legal peer review, and final human approval by authorized ASSY reviewer.

## 3. Presentation and technical safeguards / العرض والضوابط
- AR RTL / العربية من اليمين لليسار; EN LTR / English left to right. Separate language fields; do not join in one unstructured string.
- Semantic headings; accessible language tags ar-EG and en; UTF-8; localized dates/currency without changing legal meaning.
- Document metadata: language, jurisdiction, controlling_language, source_url, source_date, reviewed_by, approved_at, glossary_version, translation_status.
- Code, env keys, CLI commands, URLs, case numbers, SHA values, database column identifiers and statutory citation strings must remain unchanged.
- Public marketing must accurately describe service scope and licensing. No automated legal advice released without human controls.

## 4. Controlled mini-termbase / معجم أولي محكوم
| العربية | English preferred | Caution / تنبيه |
|---|---|---|
| توكيل رسمي عام في القضايا | General notarized power of attorney for litigation | Avoid implying unlimited authority / لا يفيد سلطة مطلقة |
| الشهر العقاري والتوثيق | Real Estate Registration and Notarization Department | Verify official agency rendering for publication / تحقق من التسمية الرسمية |
| صحة توقيع | Authentication of signature (signature-validity action) | Not proof of title / ليست إثباتًا للملكية |
| صحة ونفاذ | Action for validity and enforceability of a sale contract | Context-dependent / بحسب السياق |
| وكالة خاصة | Special power of attorney | Specify authorized acts / تحديد التصرفات |
| حكم بات | Judgment no longer open to any form of appeal | Different from merely final in some contexts / يختلف عن النهائي بحسب السياق |
| حكم نهائي | Final judgment | Check available appeal routes / مراجعة طرق الطعن |
| النقض | Cassation | Not generic 'appeal' / ليس استئنافًا عاديًا |
| النيابة العامة | Public Prosecution | Egyptian institution / جهة مصرية |
| التوقيع الإلكتروني | Electronic signature | Distinguish approved certificate / التمييز بين الشهادات المعتمدة |
Termbase is a starting review list, not a universal certified dictionary / المعجم الأولي ليس مرجعًا نهائيًا معتمدًا لكل السياقات.

## 5. Acceptance gate / بوابة القبول
- Each new user-facing artifact contains complete Arabic and English sections, with semantic parity and no omitted obligations, numbers, deadlines or exceptions.
- Glossary conflicts reviewed, verified official references cited, human language + legal approval logged.
- Unit/integration tests cover RTL/LTR, locale fallback, numeric formats, XSS/bidi controls and round-trip export of bilingual text.
- Missing translation: BLOCK_PUBLICATION. Mismatch of legal effect: BLOCK_RELEASE. Unverified jurisdictional translation: HUMAN_REVIEW_REQUIRED.
- Existing assets: audit and migrate incrementally; do not mass-translate or overwrite signed, published, or historical records.
- Do not enable external deployment, payment, live client intake, production integrations or sales release until separate go/no-go review.

## 6. Applicability / التطبيق
ASSY LEGAL OS, government-service registry, e-court, research corpora, public front door, professional directory, archive organizer, design assets, video/script metadata and future projects. External sites and third-party systems are subject to verified permissions; policy text alone does not change them.

## 7. Verification log / سجل التحقق
2026-11-09: Policy staged in GitHub review branch. No claim of full site localization, complete glossary validation, passing CI, production merge, or release authorization.
