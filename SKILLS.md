# Skills Index

Six composable skills for creator workflows. Each skill lives in its own
folder under `skills/` as a `SKILL.md` file (the standard Agent Skills
layout) and is usable on its own — install one, or install all six.

| # | Skill | One-line purpose |
|---|-------|------------------|
| 1 | [youtube-outlier-research](skills/youtube-outlier-research/SKILL.md) | Find outlier videos in a niche: rank by views vs channel baseline and velocity, surface the patterns that actually worked. |
| 2 | [repurpose-episode](skills/repurpose-episode/SKILL.md) | Turn one long recording into show notes, a blog post, LinkedIn + X posts, a newsletter, chapters and pull quotes — without inventing anything. |
| 3 | [seo-geo-audit](skills/seo-geo-audit/SKILL.md) | Audit a page for classic SEO and for AI-search (GEO) citation readiness: llms.txt, FAQ/schema, facts, structure, links, speed. |
| 4 | [digital-product-packaging](skills/digital-product-packaging/SKILL.md) | Research, outline, write, format and package a digital product (guide, template, checklist) ready to sell. |
| 5 | [thumbnail-title-test](skills/thumbnail-title-test/SKILL.md) | Generate title + thumbnail variants, score them on a fixed rubric, and keep a test log so winners compound. |
| 6 | [privacy-tool-review](skills/privacy-tool-review/SKILL.md) | Review a privacy tool before recommending or shipping it: threat model, data flow, secrets, encryption claims, permissions. |

## Companion repos (same series by mrabr381)

- **Creator Repurpose Agent** (`creator-repurpose-agent`) — the CLI + Streamlit
  tool the `repurpose-episode` skill drives: transcript → 7 outputs in one run.
- **Open-vidIQ** (`open-vidiq`) — the YouTube outlier / SEO research agent the
  `youtube-outlier-research` skill drives.
- **GEO Visibility Checker** (`geo-visibility-checker`) — the AI-search brand
  tracker the `seo-geo-audit` skill pairs with.
- **Digital-Product-Agent** — Streamlit + Gemini agent the
  `digital-product-packaging` skill pairs with.
- **Hidden-Chat** — privacy-first steganography messenger, a worked reference
  for the `privacy-tool-review` skill.

## Worked examples

One worked example per skill lives in `examples/` — short, real-looking
input → output, clearly marked as sample data, never presented as real
measurements. Run `python3 validate.py` to check that every skill, example
and link in this repo is intact.
