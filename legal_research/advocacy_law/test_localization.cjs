"use strict";
/* No browser/network credentials, and no legal corpus is altered or translated. */
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = __dirname;
const source = fs.readFileSync(path.join(root, "localization.js"), "utf8");
const staticNode = {nodeValue: "عرض بحثي لفهرس المواد وإشارات التعديل والأحكام؛ ليس نسخة رسمية معتمدة للقانون.",
  parentElement: {closest() { return null; }}};
const protectedNode = {nodeValue: "إعادة تعيين",
  parentElement: {closest(selector) { return selector.includes("#results") ? {} : null; }}};
const nodes = [staticNode, protectedNode];
const attrInput = {
  value: "محرر قضائي أصلي - لا تترجم",
  attributes: {"placeholder": "ابحث برقم مادة أو موضوع أو حكم", "aria-label": "بحث"},
  getAttribute(key) {return this.attributes[key] ?? null;},
  setAttribute(key, value) {this.attributes[key] = value;},
  closest() {return null;}
};
const store = new Map();
let toggle;
const document = {
  title: "ASSY LEGAL OS | محرك مراجعة قانون المحاماة",
  readyState: "complete",
  body: {},
  documentElement: {lang: "ar", dir: "rtl"},
  querySelector(selector) {
    return selector === "header" ? {prepend(button) {toggle = button;}} : null;
  },
  querySelectorAll(selector) {
    return selector === "[aria-label],[placeholder]" ? [attrInput] : [];
  },
  getElementById(id) {return id === "language-switch" ? toggle : null;},
  createTreeWalker() {
    let i = 0;
    return {nextNode() {return nodes[i++] ?? null;}};
  },
  createElement(tag) {
    assert.equal(tag, "button");
    return {
      attributes: {},
      setAttribute(key, value) {this.attributes[key] = value;},
      addEventListener(type, handler) {this.event = {type, handler};}
    };
  }
};
const sandbox = {
  document, NodeFilter: {SHOW_TEXT: 4},
  sessionStorage: {
    getItem(key) {return store.get(key) ?? null;},
    setItem(key,value) {store.set(key,value);}
  },
  CustomEvent: class {constructor(type, options) {this.type=type;this.detail=options.detail;}},
  window: {dispatchEvent() {}}
};
vm.runInNewContext(source, sandbox, {filename:"localization.js"});
const i18n = sandbox.window.ASSYArchiveLocale;
assert.ok(i18n);
assert.equal(i18n.getLocale(), "ar");
assert.ok(i18n.count() > 30);
assert.equal(toggle.type, "button");
assert.equal(i18n.setLocale("en"), true);
assert.equal(document.documentElement.lang, "en");
assert.equal(document.documentElement.dir, "ltr");
assert.equal(document.title, "ASSY LEGAL OS | Advocacy Law Research Review");
assert.match(staticNode.nodeValue, /^Research-only index/);
assert.equal(protectedNode.nodeValue, "إعادة تعيين");
assert.equal(attrInput.value, "محرر قضائي أصلي - لا تترجم");
assert.equal(attrInput.getAttribute("placeholder"), "Search by article number, topic or judgment");
assert.equal(toggle.textContent, "العربية");
assert.equal(i18n.setLocale("ar"), true);
assert.equal(staticNode.nodeValue, "عرض بحثي لفهرس المواد وإشارات التعديل والأحكام؛ ليس نسخة رسمية معتمدة للقانون.");
assert.equal(attrInput.getAttribute("placeholder"), "ابحث برقم مادة أو موضوع أو حكم");
assert.equal(attrInput.value, "محرر قضائي أصلي - لا تترجم");
assert.equal(i18n.setLocale("de"), false);
assert.equal(document.documentElement.lang, "ar");
console.log("PASS: archival Arabic/English UI, original legal records and form inputs preserved");
