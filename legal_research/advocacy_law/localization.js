/* ASSY Legal Research — Arabic/English interface only.
 * This file MUST NOT translate legislative source text, evidence, court extracts,
 * research records, input values or reviewer notes. Translations are drafts.
 */
(() => {
  "use strict";
  const KEY = "assy_advocacy_research_locale";
  const translations = new Map(Object.entries({
    "ASSY LEGAL OS | محرك مراجعة قانون المحاماة": "ASSY LEGAL OS | Advocacy Law Research Review",
    "ASSY LEGAL OS – مراجعة مصادر القانون": "ASSY LEGAL OS – Legal Source Review",
    "ASSY LEGAL OS – محرك مراجعة قانون المحاماة": "ASSY LEGAL OS – Advocacy Law Research Review",
    "ASSY LEGAL OS – محطة المراجعة البشرية": "ASSY LEGAL OS – Human Review Station",
    "مستشارك الشخصي في مصر": "Your Personal Legal Adviser in Egypt",
    "ASSY LAW FIRM | مستشارك الشخصي في مصر": "ASSY LAW FIRM | Your Personal Legal Adviser in Egypt",
    "عرض بحثي لفهرس المواد وإشارات التعديل والأحكام؛ ليس نسخة رسمية معتمدة للقانون.": "Research-only index of legal provisions, amendment notices and case references; this is not an officially certified version of the law.",
    "بوابة سلامة الاقتباس:": "Quotation integrity gate:",
    "لا توجد بهذه الواجهة نصوص كاملة للمادة تمت مطابقتها رسميًا. لا يجوز نسخ أي نتيجة بوصفها نصًا تشريعيًا معتمدًا أو حكمًا قضائيًا موثقًا من أصله.": "This interface does not contain full legal provisions verified against official originals. Results must not be quoted as certified legislation or authenticated judgments.",
    "بحث": "Search",
    "ابحث برقم مادة أو موضوع أو حكم": "Search by article number, topic or judgment",
    "نوع السجل": "Record type",
    "جميع السجلات": "All records",
    "المواد (1–231)": "Articles (1–231)",
    "السوابق القضائية": "Judicial precedents",
    "ملاحظات وتصحيحات": "Notices and corrections",
    "إعادة تعيين": "Reset",
    "مصدر التشريع:": "Legislation reference:",
    "نقابة المحامين المصرية": "Egyptian Bar Association",
    ". حالة المرجع كما بتاريخ 19 أكتوبر 2026. يتطلب الاعتماد فحص الجريدة الرسمية ومنطوق الأحكام ومراجعة محامٍ مختص.": ". Reference status as of 19 October 2026. Approval requires checking the Official Gazette, authenticated judicial holdings and review by a qualified lawyer.",
    "النتائج": "Results",
    "لا توجد نصوص معتمدة للاقتباس": "No certified text available for quotation",
    "قيد المراجعة — الاقتباس غير معتمد": "Under review — quotation not authorized",
    "تظهر أول 100 نتيجة؛ استخدم خانة البحث لتضييق النتائج.": "The first 100 results are displayed; refine your search to narrow the list.",
    "تنسيق البيانات غير مطابق": "Unexpected index data format",
    "المادة": "Article",
    "النص الكامل غير معتمد": "The full text is not certified",
    "الإجراءات الجنائية — مادة": "Criminal procedure — Article",
    "قيد مراجعة النص والحكم القضائي": "Legal text and judicial ruling under review",
    "تعذر تحميل ملف البيانات المستقل:": "Unable to load the standalone research index:",
    "لتشغيل البحث افتح الصفحة عبر خادم HTTP أو GitHub Pages؛ فتح HTML مباشرة بصيغة file:// قد يمنع تحميل JSON. لم تُحمّل أية نتائج غير معتمدة.": "To use search, open the page through an HTTP server or GitHub Pages; opening file:// directly may prevent JSON loading. No unverified results were loaded.",
    "نموذج استعراض أولي — غير متصل بنظام مصادقة أو بقاعدة اعتماد منتجة.": "Preliminary review interface — not connected to authentication or a production approval system.",
    "اعتماد المستندات معطل.": "Document approval is disabled.",
    "لا تعمل أزرار الاعتماد أو الرفض حتى يتم ربط الهوية الموثوقة وواجهة خدمة آمنة وسجل تدقيق دائم. البيانات المدخلة هنا لا تُحفظ ولا تُرسل.": "Approval and rejection controls remain disabled until verified identity, a secure API and a permanent audit trail are provided. Entered information is neither saved nor submitted.",
    "سجل المصدر": "Source record",
    "معرف المادة أو الحكم": "Article or judgment identifier",
    "بيانات العدد والصفحة أو رقم الطعن": "Gazette issue and page or appeal number",
    "رابط المصدر الأولي": "Primary source URL",
    "بصمة SHA-256 للملف الرسمي": "Official-file SHA-256 checksum",
    "النص المقابل للصورة الرسمية": "Text corresponding to the official source image",
    "هذه حقول مراجعة بصرية فقط، وليست وسيلة اعتماد أو حفظ.": "These fields support visual review only; they do not approve or save records.",
    "قائمة فحص الاعتماد": "Approval verification checklist",
    "المادة 50 مكررًا — الإحالة النصية متعارضة ولم تُحسم": "Article 50 bis — conflicting source reference remains unresolved",
    "□ معاينة الصورة الأصلية بنفسها": "□ Inspect the original official image",
    "□ مطابقة النص والصفحة ورقم العدد": "□ Cross-check text, page and issue number",
    "□ مراجعة تاريخ النفاذ والتعديلات": "□ Review effective date and amendments",
    "□ التحقق من بصمة الملف": "□ Verify the file checksum",
    "□ مراجعة مستقلة من محامٍ مخول": "□ Independent review by an authorized lawyer",
    "□ موافقة نهائية من مشرف منفصل عن الرافع والمراجع": "□ Final approval by a supervisor separate from uploader and reviewer",
    "الإجراءات": "Actions",
    "اعتماد قانوني": "Legal approval",
    "رفض وحفظ القرار": "Reject and record decision",
    "غير مفعلة عمدًا. لا يوجد اتصال بالخادم أو تخزين للمستندات.": "Intentionally disabled. There is no server connection or document storage."
  }));
  const originalNodes = new WeakMap();
  const originalAttributes = new WeakMap();
  const originalTitle = document.title;
  let locale;
  try { locale = sessionStorage.getItem(KEY) === "en" ? "en" : "ar"; }
  catch (_error) { locale = "ar"; }

  function t(source) {
    if (typeof source !== "string" || locale !== "en") return source;
    const match = /^(\s*)([\s\S]*?)(\s*)$/.exec(source);
    const english = translations.get(match[2]);
    return english === undefined ? source : match[1] + english + match[3];
  }
  function eligible(node) {
    return node.parentElement &&
      !node.parentElement.closest("script,style,pre,code,textarea,[contenteditable],[translate='no'],[data-no-translate],#results,#count");
  }
  function render() {
    document.documentElement.lang = locale;
    document.documentElement.dir = locale === "en" ? "ltr" : "rtl";
    document.title = t(originalTitle);
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    let node;
    while ((node = walker.nextNode())) {
      if (!eligible(node)) continue;
      if (!originalNodes.has(node)) originalNodes.set(node, node.nodeValue);
      const next = t(originalNodes.get(node));
      if (node.nodeValue !== next) node.nodeValue = next;
    }
    for (const element of document.querySelectorAll("[aria-label],[placeholder]")) {
      if (element.closest("[data-no-translate],[translate='no']")) continue;
      if (!originalAttributes.has(element)) {
        originalAttributes.set(element, {
          aria: element.getAttribute("aria-label"),
          placeholder: element.getAttribute("placeholder")
        });
      }
      const value = originalAttributes.get(element);
      if (value.aria !== null) element.setAttribute("aria-label", t(value.aria));
      if (value.placeholder !== null) element.setAttribute("placeholder", t(value.placeholder));
    }
    const toggle = document.getElementById("language-switch");
    if (toggle) {
      toggle.textContent = locale === "en" ? "العربية" : "English";
      toggle.setAttribute("aria-label", locale === "en" ? "Switch to Arabic" : "التبديل إلى الإنجليزية");
      toggle.setAttribute("aria-pressed", String(locale === "en"));
    }
  }
  function setLocale(next) {
    if (next !== "ar" && next !== "en") return false;
    const changed = locale !== next;
    locale = next;
    try { sessionStorage.setItem(KEY, locale); } catch (_error) { /* optional */ }
    render();
    if (changed) window.dispatchEvent(new CustomEvent("assy:archive-locale", { detail: { locale } }));
    return true;
  }
  window.ASSYArchiveLocale = Object.freeze({
    getLocale: () => locale, setLocale, t, count: () => translations.size
  });
  function init() {
    const header = document.querySelector("header");
    if (header) {
      const button = document.createElement("button");
      button.id = "language-switch";
      button.type = "button";
      button.addEventListener("click", () => setLocale(locale === "ar" ? "en" : "ar"));
      header.prepend(button);
    }
    render();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init, { once: true });
  else init();
})();
