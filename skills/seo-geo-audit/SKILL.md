---
name: seo-geo-audit
description: Audit a web page for classic SEO and for AI-search (GEO) citation readiness — llms.txt, FAQ and schema, verifiable facts, clear structure, working links and speed — and return a prioritised fix list. Use when a small site asks why it is not ranking or why ChatGPT and Gemini never mention it. Pairs with the GEO Visibility Checker companion repo.
---

# SEO + GEO Site Audit

## When to Use

- A site owner asks "why am I not ranking?" or "why does AI search never
  mention me?"
- Before a launch, a redesign, or after a traffic drop.
- One page or a small site (up to ~50 pages). This skill is a checklist
  audit, not a keyword database or a backlink index — it cannot tell you
  search volumes or who links to you, and it must say so.

## Workflow

1. **Scope it in writing.** The URL(s) under audit, the audit date, and what
   is *out* of scope (no keyword database, no backlink index — those need
   paid data). If the user expects search volumes, stop and say so now.
2. **Crawl the page(s).** Fetch each URL and record: HTTP status, title,
   meta description, canonical, headings (H1–H3 order), images and alt text,
   internal links, outbound links, and structured data (JSON-LD) if present.
   Note anything missing or duplicated. A page with no H1, or two H1s, is a
   finding, not a style choice.
3. **Check the classics.**
   - Exactly one H1, matching the page's topic; headings in order, no skipped
     levels.
   - Title ≤ 60 characters, meta description 120–160 characters, both
     naming the topic — no keyword stuffing.
   - Images have alt text; decorative images have empty alt (`alt=""`).
   - No broken internal links; no redirect chains (a link that redirects
     twice is a finding).
   - Canonical points at the live URL (or the intended canonical).
   - The page is indexable: not `noindex`, not blocked in robots.txt.
4. **Check GEO / AI-search readiness.** AI answer engines cite pages they
   can read, trust, and quote. Check:
   - **llms.txt** exists at the site root and lists the site's key pages
     in plain Markdown.
   - **FAQ content** answers the page's core questions in short, direct
     paragraphs, with matching `FAQPage` schema where it fits.
   - **Facts are verifiable**: every number, date, price and claim on the
     page is either sourced or plainly the site's own statement. Unsourced
     statistics are a finding.
   - **Structure a machine can quote**: one idea per heading, short
     paragraphs, lists and tables for comparisons — not a wall of prose.
   - **Entity clarity**: the page says who/what it is about in the first
     screen (named person, place, product, or topic), and the About / author
     information is reachable.
5. **Check speed and rendering.** Run the page through PageSpeed Insights
   (free API) and record Core Web Vitals. Note render-blocking resources
   and oversized images. Do not guess at speed — measure it.
6. **Score and prioritise.** Give each check a pass / fail / partial, then
   order the failures: (1) indexability and broken links, (2) missing or
   duplicated titles/headings, (3) GEO gaps (llms.txt, FAQ, unsourced
   claims), (4) speed. Each fix gets a one-line action and the file or
   setting to change.
7. **Write the report** using the template below. End with the top 5 fixes
   in order. Never invent a ranking position, a search volume, or a
   competitor's data.

## Checklist

- [ ] Scope and date written; out-of-scope items stated (no keyword data)
- [ ] Every URL fetched live (status recorded), none assumed
- [ ] One H1 per page; title and meta description within length limits
- [ ] Alt text present or correctly empty; no broken internal links
- [ ] llms.txt checked at the site root (present / absent, noted either way)
- [ ] FAQ/schema checked; unsourced statistics flagged, none added
- [ ] PageSpeed measured, not guessed; numbers recorded with the date
- [ ] Every failure has a one-line fix and a location
- [ ] No ranking position, search volume, or backlink count invented

## Templates

### Audit finding

```markdown
| Check | Result | Evidence | Fix |
|-------|--------|----------|-----|
| H1 count | FAIL | 2 H1s: "Guides" and "Best Budget Tools" | Keep one H1: "Best Budget Tools"; demote "Guides" to H2 |
```

### GEO readiness summary

```markdown
## GEO readiness: 3/6
- [x] llms.txt present
- [x] FAQ section with direct answers
- [ ] FAQPage schema missing
- [ ] 2 unsourced statistics on the page
- [x] Named topic in the first screen
- [ ] Author/About page not linked
```

### Top 5 fixes

```markdown
1. [Fix] — in [file/setting] — because [evidence]
```

## Anti-Patterns

- **Never invent data.** No keyword volumes, ranking positions, or backlink
  counts unless they came from a named tool with a date.
- **Never recommend keyword stuffing.** A readable title that names the
  topic beats a stuffed one, every time.
- **Never promise rankings.** The honest claim is "these fixes remove the
  known blockers"; rankings depend on competition you cannot see here.
- **Never treat AI search as magic.** llms.txt and FAQs help engines cite
  you; they do not guarantee citation.
- **Never audit a screenshot.** Fetch the live page. A screenshot can hide
  a `noindex` tag, a redirect, or a broken link.

## Output Format

A Markdown report: scope, per-page findings table, GEO readiness score,
PageSpeed numbers with date, then the top 5 fixes in priority order.

## Related Repos

- `geo-visibility-checker` — companion tracker that measures whether AI
  answer engines actually mention a brand/site over time; this skill audits
  the page those engines would cite.
- `seo-geo-audit` CLI (project #10 in the same series) — the automated
  version of this checklist: crawl + PageSpeed + GEO checks in one command.
