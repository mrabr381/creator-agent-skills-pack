# Worked Example — seo-geo-audit

> **Sample data.** The page below is fictional
> (`https://example.com/budget-tools` — example.com is a reserved domain).
> Findings are invented for this example only.

## Scope

- **URL:** https://example.com/budget-tools (fictional sample page)
- **Audit date:** 2026-11-20
- **Out of scope:** keyword volumes, backlink data (both need paid tools).

## Findings

| Check | Result | Evidence | Fix |
|-------|--------|----------|-----|
| HTTP status | PASS | 200 | — |
| H1 count | FAIL | 2 H1s: "Guides" and "Best Budget Tools" | Keep one H1: "Best Budget Tools"; demote "Guides" to H2 |
| Title | PASS | "Best Budget Tools (2026) — Example" (38 chars) | — |
| Meta description | FAIL | Missing | Add 120–160 char description naming the topic |
| Image alt text | PARTIAL | 3 of 8 images missing alt | Add alt text; mark 1 decorative image `alt=""` |
| Broken internal links | FAIL | 1 link to /guides/old-tool returns 404 | Update to /guides/budget-tools |
| llms.txt | FAIL | No llms.txt at site root | Add llms.txt listing key pages |
| FAQ + schema | PARTIAL | FAQ section exists; no FAQPage schema | Add FAQPage JSON-LD matching the visible FAQ |
| Unsourced claims | FAIL | "Saves users $500 a year" — no source | Remove the number or cite the source |
| PageSpeed (mobile) | 62/100 | Largest Contentful Paint 4.1s (measured 2026-11-20) | Compress hero image (1.9 MB → under 200 KB) |

## GEO readiness: 2/6

- [ ] llms.txt present
- [x] FAQ section with direct answers
- [ ] FAQPage schema
- [ ] All statistics sourced
- [x] Named topic in the first screen
- [ ] Author/About page linked

## Top 5 fixes (in order)

1. Fix the 404 internal link — in the page body.
2. Keep one H1 — in the page template.
3. Add the missing meta description — in the page head.
4. Add llms.txt — at the site root.
5. Source or remove the "$500 a year" claim — in the page copy.
