#!/usr/bin/env node
// Checks the guide's own consistency, so its conventions are enforced rather than hoped for
// (SE1/O3): every relative link and anchor resolves; every DM1 citation names a real principle in the
// file that defines it; every principle says, on the line under its heading, whether it is *New.* or
// which SE1 principles it *Reframes*; every SE1 link points at the chapter and anchor its ID implies
// (and, given a local copy of the SE1 guide, names a principle that exists); README's principle index
// and its SE1 map match the chapters exactly; chapter numbers agree; llms.txt links to files that
// exist; and CHANGELOG.md, AGENTS.md, and the templates agree on the release.
// Exits nonzero on any problem.
// Usage: node tools/check.js            (SE1 IDs checked against ../software-engineering if present)
//        SE_GUIDE=path node tools/check.js
const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const VERSION = 'DM1';
const SE = 'SE1';
const SE_BLOB = 'https://github.com/wmacevoy/software-engineering/blob/main/';
const SE_CHAPTER = { P: '01-purpose', U: '02-unknowing', F: '03-feedback', R: '04-requirements', D: '05-design', T: '06-testing', O: '07-operating', W: '08-work', H: '09-people', A: '10-agents' };
const HEADING = /^### <a id="([a-z0-9]+)"><\/a>([A-Z]\d+)\. (.*)$/;
const BASIS = /^\*(New|Reframes (.+))\.\*$/;
const SE_LINK = /\[SE1\/([A-Z]\d+)\]\(([^)]+)\)/g;

let problems = 0;
function problem(msg) { console.log(msg); problems++; }

// Releases come from CHANGELOG.md's "## v1.0 — date" headings, newest first. Until one is dated,
// copies (AGENTS.md, templates) link to main; after, to the newest dated release.
const RELEASE = /^## (v\d+\.\d+) — (\d{4}-\d{2}-\d{2}|unreleased)$/;
const changelog = fs.readFileSync(path.join(root, 'CHANGELOG.md'), 'utf8');
const releaseLines = changelog.split('\n').map((l) => l.match(RELEASE)).filter(Boolean);
const releases = releaseLines.map((m) => m[1]);
const latest = (releaseLines.find((m) => m[2] !== 'unreleased') || [])[1];
const GH = new RegExp(`^https://github\\.com/wmacevoy/data-mining/blob/(main|${releases.map((r) => r.replace('.', '\\.')).join('|')})/`);

const files = [];
(function walk(dir) {
  for (const name of fs.readdirSync(dir)) {
    // Dot-directories include .git and CI's checkout of the SE1 guide (.se1).
    if (name.startsWith('.') || name === 'node_modules') continue;
    const p = path.join(dir, name);
    if (fs.statSync(p).isDirectory()) walk(p);
    else if (p.endsWith('.md')) files.push(p);
  }
})(root);
const rel = (f) => path.relative(root, f);

// GitHub's heading slug, close enough for the headings used here.
const slug = (h) => h.trim().toLowerCase().replace(/[^\p{L}\p{N}\s_-]/gu, '').replace(/\s/g, '-');
function anchorsOf(file) {
  const text = fs.readFileSync(file, 'utf8');
  const anchors = new Set();
  for (const line of text.split('\n')) {
    if (/^#{1,6} /.test(line)) anchors.add(slug(line.replace(/^#+ /, '').replace(/<a id="[^"]+"><\/a>/, '')));
  }
  for (const m of text.matchAll(/<a id="([^"]+)">/g)) anchors.add(m[1]);
  return anchors;
}

// SE1 IDs, from a local copy of the guide's README if there is one. Without it, SE1 citations are
// checked for form only, and the summary line says so (a check that cannot fail says so; SE1/T3).
const seRoot = process.env.SE_GUIDE || path.join(root, '..', 'software-engineering');
const seReadme = path.join(seRoot, 'README.md');
const seIds = fs.existsSync(seReadme)
  ? new Set([...fs.readFileSync(seReadme, 'utf8').matchAll(/\[\*\*SE1\/([A-Z]\d+)\*\*\]/g)].map((m) => m[1]))
  : null;
function checkSe(id, url, where) {
  const want = `${SE_BLOB}guide/${SE_CHAPTER[id[0]]}.md#${id.toLowerCase()}`;
  if (!SE_CHAPTER[id[0]]) problem(`unknown SE1 chapter ${where}: SE1/${id}`);
  else if (url !== want) problem(`SE1 link       ${where}: SE1/${id} should link to ${want}`);
  if (seIds && !seIds.has(id)) problem(`unknown SE1 ID ${where}: SE1/${id}`);
}

// Principles, their basis lines, and the index and map README must contain.
const definedIn = new Map(); // DM1 ID -> chapter file
const index = [];
const reframes = new Map();  // SE1 ID -> [DM1 links]
const ORDER = 'PUFRDTOWHA';
const seSort = (a, b) => ORDER.indexOf(a[0]) - ORDER.indexOf(b[0]) || Number(a.slice(1)) - Number(b.slice(1));
for (const f of files.filter((f) => f.includes(`${path.sep}guide${path.sep}`)).sort()) {
  const lines = fs.readFileSync(f, 'utf8').split('\n');
  lines.forEach((line, i) => {
    const m = line.match(HEADING);
    if (!m) return;
    const [, anchor, id, title] = m;
    if (anchor !== id.toLowerCase()) problem(`anchor         ${rel(f)}: ${id} has anchor "${anchor}"`);
    if (definedIn.has(id)) problem(`${id} defined twice`);
    definedIn.set(id, f);
    const link = `guide/${path.basename(f)}#${anchor}`;
    index.push(`- [**${VERSION}/${id}**](${link}) ${title}`);
    const basis = (lines[i + 2] || '').match(BASIS);
    if (!basis) { problem(`no basis       ${rel(f)}: ${id} needs *New.* or *Reframes [SE1/…](…).* under its heading`); return; }
    if (basis[1] === 'New') return;
    const cited = [...basis[2].matchAll(SE_LINK)];
    if (!cited.length) problem(`no SE1 link    ${rel(f)}: ${id} says Reframes but links no SE1 principle`);
    for (const [, seId] of cited) {
      if (!reframes.has(seId)) reframes.set(seId, []);
      reframes.get(seId).push(`[${VERSION}/${id}](${link})`);
    }
  });
}
const map = [...reframes.keys()].sort(seSort).map((seId) =>
  `- [SE1/${seId}](${SE_BLOB}guide/${SE_CHAPTER[seId[0]]}.md#${seId.toLowerCase()}) → ${reframes.get(seId).join(', ')}`);

// Links: relative files and anchors, DM1 citations, SE1 citations.
for (const f of files) {
  const text = fs.readFileSync(f, 'utf8');
  for (const m of text.matchAll(SE_LINK)) checkSe(m[1], m[2], `${rel(f)}: ${m[0]}`);
  for (const m of text.matchAll(/\[([^\]]+)\]\(([^)]+)\)/g)) {
    let [, label, href] = m;
    const where = `${rel(f)}: ${m[0]}`;
    const gh = href.match(GH);
    if (!gh && href.startsWith('https://github.com/wmacevoy/data-mining/blob/')) { problem(`unknown ref    ${where}`); continue; }
    if (gh) href = path.relative(path.dirname(f), path.join(root, href.slice(gh[0].length)));
    else if (/^[a-z]+:/.test(href)) continue;
    const [target, anchor] = href.split('#');
    const targetFile = target ? path.resolve(path.dirname(f), target) : f;
    if (!fs.existsSync(targetFile)) { problem(`missing file   ${where}`); continue; }
    if (anchor && !anchorsOf(targetFile).has(anchor)) problem(`missing anchor ${where}`);
    const cite = label.replace(/\*/g, '');
    if (/^[PUFRDTOWHA]\d+$/.test(cite)) { problem(`unversioned    ${where}`); continue; }
    const v = cite.match(/^(DM\d+)\/([A-Z]\d+)$/);
    if (v) {
      if (v[1] !== VERSION) problem(`wrong version  ${where}`);
      else if (!definedIn.has(v[2])) problem(`unknown ID     ${where}`);
      else if (definedIn.get(v[2]) !== targetFile) problem(`wrong file     ${where} (defined in ${rel(definedIn.get(v[2]))})`);
    }
  }
}

// Bare citations, the form AGENTS.md uses: "(DM1/F5, SE1/T3)". Only chapter letters count, so "(K3)"
// and other parentheticals are left alone.
const CITE = '(?:(?:DM|SE)\\d+\\/)?[PUFRDTOWHA]\\d+';
for (const f of files) {
  for (const m of fs.readFileSync(f, 'utf8').matchAll(new RegExp(`\\((${CITE}(?:,\\s*${CITE})*)\\)`, 'g'))) {
    for (const cite of m[1].split(/,\s*/)) {
      const where = `${rel(f)}: ${m[0]}`;
      const [version, id] = cite.includes('/') ? cite.split('/') : [null, cite];
      if (!version) problem(`unversioned    ${where}`);
      else if (version === VERSION) { if (!definedIn.has(id)) problem(`unknown ID     ${where}`); }
      else if (version === SE) { if (seIds && !seIds.has(id)) problem(`unknown SE1 ID ${where}`); }
      else problem(`wrong version  ${where}`);
    }
  }
}

// Chapter numbers: the file prefix, the title, and every link label that names a chapter agree.
const chapterTitle = new Map();
for (const f of files.filter((f) => /guide[\\/]\d\d-[a-z-]+\.md$/.test(f))) {
  const title = fs.readFileSync(f, 'utf8').split('\n')[0].replace(/^# /, '');
  const n = parseInt(path.basename(f), 10);
  if (!title.startsWith(`${n}. `)) problem(`title number   ${rel(f)}: "${title}"`);
  chapterTitle.set(path.basename(f), title);
}
for (const f of files) {
  for (const m of fs.readFileSync(f, 'utf8').matchAll(/\[(\d+)\. ([^\]]+)\]\(([^)#]*?)(\d\d-[a-z-]+\.md)\)/g)) {
    if (m[3].startsWith('http')) continue; // a chapter of SE1, not of this guide
    const title = chapterTitle.get(m[4]);
    if (title && `${m[1]}. ${m[2]}` !== title) problem(`chapter label  ${rel(f)}: ${m[0]} (title is "${title}")`);
  }
}

// llms.txt points agents at raw files by URL, which the link check above never sees.
const RAW = 'https://raw.githubusercontent.com/wmacevoy/data-mining/main/';
for (const m of fs.readFileSync(path.join(root, 'llms.txt'), 'utf8').matchAll(/\]\(([^)]+)\)/g)) {
  if (m[1].startsWith('https://raw.githubusercontent.com/wmacevoy/software-engineering/')) continue;
  if (!m[1].startsWith(RAW)) problem(`not a raw link llms.txt: ${m[0]}`);
  else if (!fs.existsSync(path.join(root, m[1].slice(RAW.length)))) problem(`missing file   llms.txt: ${m[0]}`);
}

// Releases: the newest release states the principle count, and every copy names the same release.
const count = changelog.match(/· (\d+) principles/);
if (!releases.length) problem('CHANGELOG.md has no "## vX.Y — yyyy-mm-dd|unreleased" release');
if (!count || Number(count[1]) !== definedIn.size) problem(`principle count CHANGELOG.md says ${count ? count[1] : 'nothing'}, the chapters define ${definedIn.size}`);
const copyRef = latest || 'main';
for (const f of ['AGENTS.md', ...files.filter((f) => f.includes(`${path.sep}templates${path.sep}`)).map(rel)]) {
  for (const m of fs.readFileSync(path.join(root, f), 'utf8').matchAll(/wmacevoy\/data-mining\/(?:blob|tree)\/([^/\s;)]+)/g)) {
    if (m[1] !== copyRef) problem(`stale release  ${f}: links to ${m[1]}, copies should link to ${copyRef}`);
  }
}
const agents = fs.readFileSync(path.join(root, 'AGENTS.md'), 'utf8').match(/This copy is\s+from\s+\*\*(v\d+\.\d+)\*\*/);
if (!agents || agents[1] !== releases[0]) problem(`stale release  AGENTS.md: says it is from ${agents ? agents[1] : 'nothing'}, newest release is ${releases[0]}`);

const readme = fs.readFileSync(path.join(root, 'README.md'), 'utf8');
for (const line of index) if (!readme.includes(line)) problem(`README index out of date: ${line}`);
for (const line of map) if (!readme.includes(line)) problem(`README SE1 map out of date: ${line}`);

if (process.argv.includes('--print')) console.log(['', ...index, '', ...map, ''].join('\n'));
console.log(`${files.length} files, ${definedIn.size} principles (${definedIn.size - [...new Set([...reframes.values()].flat())].length} new), ` +
  `${reframes.size} SE1 principles reframed, SE1 IDs ${seIds ? `checked against ${rel(seReadme)}` : 'NOT checked (no local SE1 guide; set SE_GUIDE)'}, ${problems} problems`);
process.exit(problems ? 1 : 0);
