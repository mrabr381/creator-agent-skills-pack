---
name: thumbnail-title-test
description: Generate title and thumbnail variants for a video, score them on a fixed rubric (curiosity gap, named subject, payoff honesty, readability), and keep a test log so winning patterns compound. Use before publishing, when a video needs a title and thumbnail that earn the click and keep the promise. Works standalone — no companion tool needed.
---

# Thumbnail + Title Test

## When to Use

- A video is finished (or nearly finished) and needs a title and thumbnail
  before publishing.
- A published video underperforms and the title/thumbnail is the suspect.
- Do **not** use this skill before knowing what the video actually delivers.
  A title is a promise about the first 30 seconds; if you have not watched
  the opening, you cannot write the title.

## Workflow

1. **State the payoff in one sentence.** What does the viewer learn, see,
   or feel in the first 30 seconds? Write it down. Every title and
   thumbnail is judged against this sentence — if it promises something
   else, it is a lie, however clickable.
2. **Name the subject.** The strongest titles name a person, place, case,
   or specific thing ("The Tower of London's Forgotten Prisoners", not
   "This Place Is Haunted"). Write the named subject down before
   brainstorming titles.
3. **Generate 6 title variants.** Cover at least three patterns:
   - Question / paradox: "Why Did Nobody Find Her for 40 Years?"
   - Named case + revelation: "The Claudia Lawrence Files: What the Police
     Missed" (only if the video actually covers it).
   - Numbered / list: "5 Witches the Trials Could Not Explain".
   - Stakes / consequence: "The Village That Vanished Overnight".
   Never generate six versions of the same pattern.
4. **Generate 3 thumbnail concepts per shortlisted title.** Each concept:
   one focal subject, at most 3 words of text, high contrast, readable at
   phone size. Describe the concept in words (subject, expression or
   object, background, text) — a thumbnail you cannot describe cannot be
   made.
5. **Score every variant on the rubric below.** Score honestly; a 5/5 that
   the video cannot pay off is a 0. Keep the two highest-scoring titles
   and their best thumbnail concept each.
6. **Check the pair together.** Title + thumbnail must agree: the thumbnail
   shows the subject the title names, and neither repeats the other
   word-for-word. Read the pair at phone size (or imagine it at 120 px
   wide): if the text is unreadable or the subject is unclear, it fails.
7. **Log the test.** Record the chosen pair, the scores, the publish date,
   and — after 7 days — the result (click-through rate and stayed-through
   percentage if available). Winners go into a pattern log: "named case +
   question scored 18/20 and held 71% — use again." Losers are logged too;
   an unlogged test is a wasted test.

## Checklist

- [ ] Payoff sentence written before any title was generated
- [ ] Named subject identified (person, place, case, or specific thing)
- [ ] 6 title variants across at least 3 patterns
- [ ] 3 thumbnail concepts for each shortlisted title, describable in words
- [ ] Every variant scored on all 4 rubric criteria (show the scores)
- [ ] Chosen pair agrees: thumbnail shows what the title names
- [ ] Pair readable at phone size (≤ 3 words on the thumbnail)
- [ ] Test logged with date; 7-day result to be added later

## Templates

### Rubric (score each 0–5)

```markdown
| Criterion | What it means | Score |
|-----------|---------------|-------|
| Curiosity gap | An unanswered question or paradox, not a summary | /5 |
| Named subject | A specific person/place/case is named | /5 |
| Payoff honesty | The video delivers what the title promises in the first 30s | /5 |
| Readability | Clear at phone size; ≤ 3 words on thumbnail | /5 |
| **Total** | | **/20** |
```

### Test log entry

```markdown
| Date | Video | Title | Thumbnail concept | Score | CTR 7d | Stayed % | Verdict |
|------|-------|-------|-------------------|-------|--------|----------|---------|
| 2026-11-20 | ... | ... | ... | 18/20 | — | — | pending |
```

## Anti-Patterns

- **Never promise what the video does not deliver.** Clickbait that the
  first 30 seconds cannot pay off is a swipe, a dislike, and a dead
  channel signal — not a win.
- **Never use ALL CAPS or red-arrow spam.** One emphasised word is a
  highlight; a thumbnail that shouts everything says nothing.
- **Never repeat the title on the thumbnail.** The two work together; the
  thumbnail shows, the title tells.
- **Never test without logging.** A "winning" title you cannot remember
  next month is luck, not learning.
- **Never judge on day one.** Click-through needs days of data; a 7-day
  result is the verdict, not a 7-hour one.

## Output Format

A Markdown test sheet: payoff sentence, 6 scored titles, thumbnail
concepts for the top 2, the chosen pair, and a test-log entry ready to fill
in after 7 days.

## Related Repos

- `youtube-outlier-research` — use first to learn which title patterns
  already won in the niche; use this skill to apply them to a specific video.
- `creator-repurpose-agent` — once the video is published, repurpose it
  with the winning title as the anchor for the blog and social posts.
