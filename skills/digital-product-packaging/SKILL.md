---
name: digital-product-packaging
description: Research, outline, write, format and package a digital product (guide, ebook, template, checklist) so it is ready to sell — validated topic, honest pricing, complete file set and a storefront listing. Use when a creator wants to turn knowledge into a product instead of another post. Pairs with the Digital-Product-Agent companion repo.
---

# Digital Product Packaging

## When to Use

- A creator asks "can I sell what I know?" and has an audience, a skill,
  or a repeatable result.
- A draft (notes, scripts, a video series) exists and should become a
  product.
- Do **not** use this skill to invent expertise. If the creator cannot name
  three real problems their buyers have, in the buyers' own words, the
  product is not ready — go back to research.

## Workflow

1. **Validate the topic before writing a word.** Find the demand: 5–10 real
   questions people ask (comments, forums, search suggestions, support
   emails). Write them down verbatim. If the same question appears three
   times from different people, it is a chapter. If no question repeats,
   the topic is a guess — say so and pick a narrower one.
2. **Define the buyer and the promise in one sentence each.**
   Buyer: "Busy new YouTubers who..." Promise: "After this guide you can
   ..." The promise must be something the product actually teaches — no
   income claims, no "guaranteed results".
3. **Outline from the questions.** One chapter per repeated question, in
   the order a buyer meets the problem. Each chapter gets: the problem in
   the buyer's words, the method, a worked example, and a checklist. Cut
   any chapter with no source question behind it.
4. **Write the content.** Short sections, one idea per heading, concrete
   steps, real examples. Every claim must be something the creator can
   stand behind: their own experience, a cited source, or a worked
   calculation shown in full. No filler chapters, no "in this chapter we
   will..." padding.
5. **Build the file set.** A sellable product is a folder, not a file:
   - The product itself (PDF and/or editable source: Markdown, Docs, or
     spreadsheet for templates).
   - A 1-page quick-start / cheat sheet.
   - A README for the buyer: what is inside, how to use it, requirements.
   - A licence file stating what the buyer may and may not do (personal
     use, no resale, no redistribution).
   - A cover image and 2–3 preview images (real pages, not mockups of
     pages that do not exist).
6. **Price it honestly.** Price from the promise and the work, not from a
   guru's chart: comparable products, time saved, and what the audience
   already pays for. List the price, what is included, and the refund
   policy in plain language. Never use fake scarcity ("only 3 left" for a
   digital file) or fake discounts (a "was $199" price it never sold at).
7. **Write the listing.** Title names the buyer and the outcome. The
   description opens with the promise, then what is inside (chapter list),
   who it is for and not for, and the file list. Every screenshot is a real
   page from the product.
8. **Pre-flight check.** Run the checklist below on the finished folder.
   Fix failures before the product goes on sale — a buyer who finds a
   broken file on day one does not come back.

## Checklist

- [ ] 5–10 real buyer questions collected; chapters map to them
- [ ] Buyer and promise each in one sentence; promise is teachable, not income
- [ ] No chapter without a source question; no filler chapters
- [ ] Every claim is the creator's experience, a cited source, or a shown calculation
- [ ] File set complete: product + quick-start + buyer README + licence + cover + previews
- [ ] Previews are real pages from the product, not mockups
- [ ] Price, contents, and refund policy stated plainly; no fake scarcity or fake discounts
- [ ] Listing names the buyer and the outcome; "not for" is stated
- [ ] All files open cleanly (PDF, spreadsheet, docs — actually opened and checked)

## Templates

### Product folder

```text
my-product/
├── my-product.pdf
├── my-product-source.md
├── quick-start.pdf
├── README-buyer.md
├── LICENSE-buyer.txt
├── cover.png
└── preview-1.png
```

### Listing description

```markdown
## [Product name] — [outcome] for [buyer]
**Promise:** [one sentence]
### What's inside
- Chapter 1: [title] — [what the buyer can do after it]
### You get
- [file list with formats]
### Not for
- [who should not buy it]
### Refund policy
[plain-language policy]
```

## Anti-Patterns

- **Never invent expertise.** Three real buyer problems, in their words,
  or the product is not ready.
- **Never fake scarcity or discounts.** Digital files do not run out.
- **Never promise income or guaranteed results.** Teach a skill; let the
  buyer judge the outcome.
- **Never ship a mockup as a preview.** Previews show real pages.
- **Never sell an outline.** A table of contents is not a product.

## Output Format

A product folder (see template) plus a listing draft in Markdown. If the
companion Digital-Product-Agent repo is available, it can generate the
research and draft; this skill is the quality gate that decides whether
the draft is sellable.

## Related Repos

- `Digital-Product-Agent` — companion Streamlit + Gemini agent that
  researches, generates, formats and packages digital products; this skill
  validates and finishes its output.
- `creator-repurpose-agent` — turn a product's source material (a video or
  talk) into launch content: announcement post, thread, newsletter.
- Free Digital-Product Storefront (project #9 in the same series) — the
  static storefront that sells the finished folder without a platform fee.
