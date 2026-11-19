---
name: repurpose-episode
description: Turn one long recording (podcast episode, YouTube video, talk) into show notes, a blog post, LinkedIn and X posts, a newsletter, chapters and pull quotes — every word traced back to the transcript, nothing invented. Use when a creator has a finished recording and wants it working across platforms. Pairs with the Creator Repurpose Agent companion repo.
---

# Repurpose Episode

## When to Use

- A podcast episode, YouTube video, or recorded talk is finished and the
  creator asks "what else can I make from this?"
- A transcript (or audio/video file, or YouTube URL) exists.
- Do **not** use this skill without a transcript. If there is no transcript,
  make one first (Whisper locally, or YouTube captions) — never summarise
  from a title or a guess about what was said.

## Workflow

1. **Get the transcript.** Prefer the companion Creator Repurpose Agent
   repo (`creator-repurpose-agent`): it takes a YouTube URL, an audio/video
   file, or a pasted transcript, transcribes with local Whisper when needed,
   and produces all seven outputs in one run. By hand, follow steps 2–8.
2. **Read the transcript fully before writing anything.** Note the episode's
   one big idea in a single sentence, and mark: the 3–5 strongest points,
   every timestamp where the topic changes, and any sentence quotable
   word-for-word.
3. **Chapters first.** Split the transcript at topic changes. Each chapter
   needs a timestamp that exists in the transcript and a short phrase title.
   If a timestamp is not in the transcript, the chapter does not exist.
4. **Show notes.** One page: the big idea, 3–5 key points (each traceable to
   a transcript passage), key topics as two-word phrases taken from the
   transcript, and the chapters.
5. **Blog post.** 600–1,200 words, built only from transcript material.
   Headings are short phrases; the body under each heading develops the
   transcript point in full sentences. Never add a fact, statistic, or
   example that is not in the transcript.
6. **LinkedIn post.** Hook (the most surprising true sentence, rewritten
   tight — not a quote unless marked as one) + 3 takeaways + 1 question.
   The hook must not reappear as takeaway #1.
7. **X thread.** 6–10 posts, one idea per post, every post ≤ 280
   characters, numbered 1/N–N/N. Post 1 is the hook; the last post asks a
   question or points to the full episode. Never repeat post 1 inside
   post 2.
8. **Newsletter.** Big idea + 3 keepers + one verbatim quote (exact words,
   in quotation marks) + a link to the episode.
9. **Pull quotes.** 3–5 sentences copied exactly from the transcript,
   word for word, with their timestamps. If a sentence needs trimming, use
   an ellipsis (…) and never change a word inside the quote.
10. **Verify before delivering.** Run the checklist below on the finished
    pack. Fix failures, then re-check — do not ship a pack with a failed
    check.

## Checklist

- [ ] Every pull quote is an exact substring of the transcript
- [ ] Every chapter timestamp exists in the transcript, in order
- [ ] Duration stated anywhere matches the last timestamp
- [ ] Every X post is ≤ 280 characters, one idea per post
- [ ] The LinkedIn hook is not repeated as takeaway #1
- [ ] No claim appears in any output that is not in the transcript
- [ ] No statistic, date, or name was added from outside the transcript
- [ ] Key topics are phrases from the transcript, not single junk words
- [ ] Blog headings are short phrases; the body adds detail, not repetition

## Templates

### Show notes

```markdown
# Show notes: [episode title]
**Big idea:** [one sentence]
## Key points
- [point, traceable to the transcript]
## Chapters
- [00:00] [chapter title]
```

### LinkedIn post

```markdown
[Hook — one surprising true sentence.]

Here are 3 takeaways:
1. ...
2. ...
3. ...

[Question for the reader?]
```

### X thread post

```markdown
1/8 [One idea, ≤ 280 characters total.]
```

### Pull quote

```markdown
> "[Exact sentence from the transcript.]" — [00:00]
```

## Anti-Patterns

- **Never invent.** No invented quotes, statistics, examples, or
  "research says" lines. If it is not in the transcript, it does not exist.
- **Never pad.** A short episode makes a short pack. Repeating the same
  point in five formats is filler, not repurposing.
- **Never fake a timestamp.** Chapters and quotes use real timestamps only.
- **Never let the hook leak.** The opening sentence is the hook; do not
  restate it as a takeaway, a blog heading, and a newsletter opener.
- **Never exceed the X limit.** Count characters. A 281-character post is a
  failed post.

## Output Format

Seven files plus a combined pack: `show_notes.md`, `blog_post.md`,
`linkedin_post.txt`, `x_thread.txt`, `newsletter.md`, `chapters.md`,
`pull_quotes.md`, `repurpose_pack.md`. Each file states at the top whether
it was produced with the local fallback (extracted only) or with an AI
rewrite — and an AI rewrite still may not add facts.

## Related Repos

- `creator-repurpose-agent` — companion tool that runs this whole workflow
  (CLI + Streamlit, local Whisper, optional BYO free Gemini key for the
  AI-rewritten versions of the same outputs).
- `youtube-outlier-research` — use before recording, to pick a topic with
  evidence; use this skill after recording, to squeeze the episode dry.
