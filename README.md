# Creator Agent Skills Pack 🎬

[![Markdown](https://img.shields.io/badge/format-Markdown%20%2B%20YAML-blue.svg)](#skills-index)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![No API key required](https://img.shields.io/badge/API%20key-not%20required-brightgreen.svg)](#install)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-6d28d9.svg)](#install)
[![Codex](https://img.shields.io/badge/Codex-compatible-6d28d9.svg)](#install)
[![Cursor](https://img.shields.io/badge/Cursor-compatible-6d28d9.svg)](#install)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-compatible-6d28d9.svg)](#install)

**Six small, composable skills that turn a coding agent into a creator's
agent** — YouTube research, episode repurposing, SEO + AI-search audits,
digital-product packaging, title/thumbnail testing, and privacy-tool review.

No code. No API. No key. Each skill is a single `SKILL.md` file: when to use
it, the exact workflow, checklists, templates, and the mistakes not to make.

> Why this exists: the biggest skill packs on GitHub in November 2026 are
> all software-engineering workflows — [mattpocock/skills](https://github.com/mattpocock/skills)
> (327k stars, +19.1k in November 2026), obra/superpowers (321k),
> anthropics/skills (197k). Star counts are a November 2026 research
> snapshot, not a live fact. No creator-focused pack existed. This is that
> pack — and it is the instruction layer for the free creator tools in the
> same series (see [Companion repos](#companion-repos)).

## Table of contents

- [Skills index](#skills-index)
- [Install](#install)
- [Before / after](#before--after)
- [How a skill is written](#how-a-skill-is-written)
- [Worked examples](#worked-examples)
- [Companion repos](#companion-repos)
- [Honest limitations](#honest-limitations)
- [Contributing](#contributing)
- [License](#license)

## Skills index

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [youtube-outlier-research](skills/youtube-outlier-research/SKILL.md) | Find outlier videos in a niche: rank by views vs channel baseline and velocity, surface the patterns that actually worked. |
| 2 | [repurpose-episode](skills/repurpose-episode/SKILL.md) | Turn one long recording into show notes, a blog post, LinkedIn + X posts, a newsletter, chapters and pull quotes — without inventing anything. |
| 3 | [seo-geo-audit](skills/seo-geo-audit/SKILL.md) | Audit a page for classic SEO and for AI-search (GEO) citation readiness: llms.txt, FAQ/schema, facts, structure, links, speed. |
| 4 | [digital-product-packaging](skills/digital-product-packaging/SKILL.md) | Research, outline, write, format and package a digital product (guide, template, checklist) ready to sell. |
| 5 | [thumbnail-title-test](skills/thumbnail-title-test/SKILL.md) | Generate title + thumbnail variants, score them on a fixed rubric, and keep a test log so winners compound. |
| 6 | [privacy-tool-review](skills/privacy-tool-review/SKILL.md) | Review a privacy tool before recommending or shipping it: threat model, data flow, secrets, encryption claims, permissions. |

Full index with companion repos: [SKILLS.md](SKILLS.md).

## Install

**Option A — install script (Claude Code default):**

```bash
git clone https://github.com/mrabr381/creator-agent-skills-pack.git
cd creator-agent-skills-pack
./install.sh
# installs the 6 skills to ~/.claude/skills
```

Other agents — point the script at your agent's skills folder:

```bash
./install.sh --dir /path/to/your-agent/skills
# e.g. project-local: ./install.sh --dir .claude/skills
```

**Option B — via skills.sh:**

```bash
npx skills add mrabr381/creator-agent-skills-pack
```

**Option C — manual copy (works everywhere):**

```bash
cp -r skills/youtube-outlier-research ~/.claude/skills/
# repeat for any other skill you want, or copy the whole skills/ folder
```

Then invoke a skill by name in your agent, for example:
"Use the repurpose-episode skill on this transcript."

## Before / after

**Before — one 14-minute episode, used once:**

```
📹 1 YouTube video
🎧 1 podcast episode
😩 …and then the transcript sits in a folder, unused
```

**After — the same episode, run through the repurpose-episode skill:**

```
output/sample-episode/
├── show_notes.md       # overview + key points + topics
├── blog_post.md        # full blog post from the episode
├── linkedin_post.txt   # hook + 3 takeaways + question
├── x_thread.txt        # 8 posts, every one ≤ 280 chars
├── newsletter.md       # big idea + 3 keepers + verbatim quote
├── chapters.md         # real timestamps from the transcript
├── pull_quotes.md      # exact sentences, word for word
└── repurpose_pack.md   # all of the above in one file
```

## How a skill is written

Every `SKILL.md` follows the same shape, so an agent (or a human) always
knows where to look:

1. **YAML frontmatter** — `name` (matches the folder) and `description`
   (what it does and when to use it).
2. **When to Use** — the trigger, in plain language.
3. **Workflow** — numbered steps, concrete enough to follow blind.
4. **Checklist** — the pass/fail list before calling the work done.
5. **Templates** — copy-paste output shapes.
6. **Anti-Patterns** — the mistakes this skill exists to prevent. The first
   rule in every skill: **never invent numbers, quotes, or sources.** If the
   input does not contain it, the output must not claim it.

<details>
<summary>Example: the repurpose-episode checklist (excerpt)</summary>

- [ ] Every pull quote is an exact substring of the transcript
- [ ] Every chapter timestamp exists in the transcript
- [ ] Every X post is ≤ 280 characters, one idea per post
- [ ] No claim appears in any output that is not in the transcript
- [ ] The LinkedIn hook is not repeated as takeaway #1

</details>

## Worked examples

One worked example per skill, in `examples/` — short input → output, clearly
marked as sample data:

- `examples/youtube-outlier-research.md` — 5-video sample channel, outlier
  scores computed by hand (median 9,000 views; top video 95,000 = 10.6×).
- `examples/repurpose-episode.md` — timestamped excerpt → show notes,
  LinkedIn post, X posts, one verbatim quote.
- `examples/seo-geo-audit.md` — sample page audit table with pass/fail.
- `examples/digital-product-packaging.md` — sample product outline, file
  list and pricing.
- `examples/thumbnail-title-test.md` — 3 title variants scored on the rubric.
- `examples/privacy-tool-review.md` — review of a fictional note app.

## Companion repos

These skills are the instruction layer for the free creator tools in the
same series by [mrabr381](https://github.com/mrabr381). The skills never
duplicate their code — they drive them, or work the same workflow by hand
when the tool is not installed.

| Skill | Companion repo | What the tool adds |
|-------|---------------|--------------------|
| youtube-outlier-research | `open-vidiq` | YouTube Data API research agent (outliers, velocity, keywords) |
| repurpose-episode | `creator-repurpose-agent` | CLI + Streamlit: transcript → 7 outputs in one run (Whisper + BYO free Gemini key) |
| seo-geo-audit | `geo-visibility-checker` | AI-search brand tracker; pairs with the audit checklist here |
| digital-product-packaging | `Digital-Product-Agent` | Streamlit + Gemini agent that researches and packages digital products |
| thumbnail-title-test | — (works standalone) | No companion tool; the rubric and test log are the product |
| privacy-tool-review | `Hidden-Chat-` | Privacy-first steganography messenger, a worked reference implementation |

> Note: `creator-repurpose-agent`, `open-vidiq` and `geo-visibility-checker`
> are all built and tested in the same series; their repos are being
> published in order, so a companion link may 404 for a short while until
> its push lands. Every skill works standalone until then — the companion
> tool is a shortcut, never a requirement.

## Honest limitations

- **Skills are instructions, not software.** They cannot fetch YouTube data,
  transcribe audio, or call an API by themselves — they tell an agent (or
  you) how to do it, and point at the companion tools that do the heavy
  lifting. Without a tool or data source, a skill can only work from what
  you paste in.
- **Star counts are a snapshot.** The 327k / 321k / 197k figures above were
  read in November 2026 research; they change daily. Do not quote them as
  current.
- **The GEO advice is new and moving.** AI-search citation behaviour (what
  ChatGPT / Gemini / Perplexity cite and why) changes frequently; the
  `seo-geo-audit` skill checks for the durable signals (llms.txt, FAQ and
  schema, verifiable facts, clear structure) rather than promising rankings.
- **Free-tier keys are bring-your-own.** Where a companion tool uses a Gemini
  or YouTube Data API key, it is your own free-tier key, stored in your own
  `.env` — the skills never ask for one and never contain one.

## Contributing

- Keep each skill self-contained: one job, one folder, no cross-skill
  dependencies.
- Every new skill needs a worked example in `examples/` and must pass
  `python3 validate.py`.
- No invented numbers, quotes, or sources — in skills, examples, or README.

## License

MIT — see [LICENSE](LICENSE). Copyright © 2026 Muhammad AbuBakar Azam.
