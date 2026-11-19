---
name: youtube-outlier-research
description: Find outlier videos in a YouTube niche by comparing each video's views against its own channel's baseline and its velocity (views per day), then surface the title, topic and format patterns that actually worked. Use when a creator asks what is working in a niche, which videos to model, or what to make next. Pairs with the Open-vidIQ companion repo.
---

# YouTube Outlier Research

## When to Use

- A creator asks "what is working in my niche?" or "what should I make next?"
- A channel review, competitor analysis, or content-planning session starts.
- A video idea needs evidence before production — not a hunch.
- Do **not** use this skill to copy a video. It finds patterns to learn from,
  not videos to clone.

## Workflow

1. **Define the niche in one sentence.** Example: "British history mysteries,
   5–15 minute faceless Shorts and long-form." Write it down; every later
   step is judged against it. If the niche is wider than one sentence, split
   it — mixed niches produce meaningless averages.
2. **Collect the channels.** 3–8 channels: the creator's own channel plus
   direct competitors (same niche, same rough size band). Record each
   channel's subscriber count and the date you collected the data.
3. **Collect the videos.** For each channel, take its last 20–50 videos
   (or all videos from the last 90 days, whichever is smaller). For each
   video record: title, URL, publish date, view count, duration, and format
   (Short / long-form / live). Get this from the YouTube Data API
   (free tier, 10,000 units/day) or, preferably, from the companion
   Open-vidIQ repo (`open-vidiq`), which does the fetching and scoring.
   Never type view counts from memory — always copy them from the source.
4. **Compute the channel baseline.** For each channel, compute the **median**
   views of the collected videos (not the mean — one viral video wrecks a
   mean). This median is "a normal video" for that channel.
5. **Score every video.**
   - **Outlier score** = video views ÷ channel median views.
     2.0× or higher is an outlier; 5.0× or higher is a breakout.
   - **Velocity** = video views ÷ days since publish. Use velocity to compare
     a 3-day-old video with a 3-month-old one.
   - **Views per subscriber** = video views ÷ channel subscribers. Useful
     only when comparing channels of similar size; never compare a 1k-sub
     channel with a 1M-sub channel on this metric.
6. **Rank and filter.** Keep videos with outlier score ≥ 2.0×, sorted by
   outlier score, then velocity. Drop anything off-niche (a channel's one
   viral video about a different topic is noise, not signal).
7. **Extract patterns from the top 10.** For each, note: topic (who/what is
   named?), title structure (question? number? named case? curiosity gap?),
   length band, format, hook claim in the first seconds (if known), and
   publish day/time. Then count what repeats: e.g. "7 of 10 name a person;
   6 of 10 are under 60 seconds; 0 of 10 are pure place tours."
8. **Write the report** using the template below. End with 3–5 concrete
   video ideas that follow the winning patterns *and* fit the creator's
   channel — each idea must name the topic, the title pattern, and the
   evidence (which outlier videos support it).

## Checklist

- [ ] Niche written in one sentence before any data was collected
- [ ] 3–8 channels, subscriber counts and collection date recorded
- [ ] Every view count copied from the API/page, none from memory
- [ ] Baseline is the median, not the mean
- [ ] Outlier score and velocity computed for every video (show the maths)
- [ ] Off-niche viral videos excluded, with the reason noted
- [ ] Top 10 pattern counts add up (e.g. "7 of 10" means 7 rows say so)
- [ ] Each recommended idea names its supporting outlier videos
- [ ] No recommendation claims a result ("this will get 100k views") —
      only evidence ("videos like this scored 2–5× their channel median")

## Templates

### Outlier report table

```markdown
| # | Video | Channel | Views | Median | Outlier | Velocity/day | Age |
|---|-------|---------|-------|--------|---------|--------------|-----|
| 1 | [title](https://example.com/video) | Name | 95,000 | 9,000 | 10.6x | 3,167 | 30d |
```

### Pattern summary

```markdown
## Patterns in the top 10
- Named person/case in title: 7/10
- Question or paradox hook: 6/10
- Under 60 seconds: 6/10
- Pure place tour (no mystery/crime): 0/10
```

### Video idea

```markdown
## Idea: [working title following the winning pattern]
- Topic: ...
- Pattern it follows: ... (supported by videos #1, #3, #7)
- Format/length: ...
- Why now: ...
```

## Anti-Patterns

- **Never rank by raw views alone.** A 500k-view video on a 2M-sub channel
  is normal; a 50k-view video on a 5k-sub channel is a breakout. Always
  divide by the channel's own baseline.
- **Never invent numbers.** If the API returned no data, say so. A made-up
  view count makes the whole report worthless.
- **Never compare unlike channels.** Different sizes, languages and formats
  need separate baselines.
- **Never recommend copying.** Model the pattern (named case + curiosity
  gap), not the video.
- **Never promise outcomes.** Outliers describe the past. The honest claim
  is "videos shaped like this outperformed their channel median 2–5×",
  not "this will go viral."

## Output Format

A Markdown report: niche sentence, collection date, per-channel baselines,
the ranked outlier table (score ≥ 2.0×), pattern counts, then 3–5 video
ideas with evidence. Save it as `outlier-report-YYYY-MM-DD.md`.

## Related Repos

- `open-vidiq` — companion agent that fetches the data and computes the
  scores in this skill's workflow.
- `creator-repurpose-agent` — turn a winning video's transcript into
  follow-up content once the idea is made.
