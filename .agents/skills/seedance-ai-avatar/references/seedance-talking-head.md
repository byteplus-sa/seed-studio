# Seedance talking-head templates

Settings and references to give with the pasted block: the selected sheet as
`@Image 1` (reference image), the voice clip as `@Audio 1`, audio on, 1080p,
no watermark, duration = script seconds rounded up (≤30). Hand off the sheet
only after the consent and real-likeness gates are recorded. Placeholders in
angle brackets (`<Name>`, `<possessive>`) are filled before the prompt is frozen.

## A. Locked take for split-screen (ratio 1:1)

The square frame crops cleanly to the 1080×960 lower half and to the framed card.

```
[Character]
<Name> corresponds to @Image 1. Use only <possessive> face, hairstyle, skin tone, build and outfit: <outfit list>. Do not use the grey backdrop or the multi-panel layout of @Image 1. All three panels of @Image 1 show the same one person; the output contains only one person, <Name>, throughout.

[Scene]
A small studio with a dark charcoal gradient backdrop, slightly lighter behind <possessive> head and falling off to near-black at the edges. A small black lavalier mic is clipped at the center of <possessive> sweater collar.

[Shot]
<Name> delivers a fast, energetic tech-news explainer straight to camera in one continuous take, in a centered medium close-up framed from just above the top of <possessive> head to just below the sternum. <Name> keeps direct eye contact with the lens the whole time. While speaking, <Name> uses natural open-hand explanatory gestures at chest height: <2–4 gestures tied to quoted words>. Brows lift on key words, head gives small emphatic nods, and <possessive> lips form every syllable in sync with the dialogue. <Possessive> hands rest loosely together at the bottom edge of frame between gestures.

[Style and camera]
Soft frontal key light slightly above eye level with gentle falloff into the dark background, clean 50mm-equivalent look, neutral slightly cool studio grade with natural skin tones. Static locked-off medium close-up at eye level, no camera movement, no cuts.

[Audio reference]
@Audio 1 defines <Name>'s voice timbre, accent and pacing only; do not reuse any words from @Audio 1.

[Audio]
Dialogue language: American English. <Name> says in fast, confident, energetic news-explainer delivery, with a punchy rise on "crazy part" and a brief beat before the final stat: {<full script>}
Quiet studio room tone only. No background music. No subtitles or on-screen text.
```

## B. Vertical take with camera beats (ratio 9:16)

Use for remix edits that go full-screen on the presenter. Add a `[Timeline]`
with 4–5 timestamped beats covering the full duration: medium waist-up →
slow push-in to chest-up on the pivot line → ease back → hold for the closer.
Tie one gesture to one quoted word per beat, keep gestures inside the frame
edges, and end the last beat with a held pose. Add: "Single continuous take,
vertical framing, <Name> centered and facing the camera throughout." and
"Close lavalier-mic studio voice with quiet room tone. No background music."

## Notes

- Hands below a chest-up frame (template A) and a duration too tight for the
  word count (template B) are the usual faults. Leave about 1s of slack after
  the last word.
- Wardrobe and accessories come through the sheet, but the lav mic does not
  reliably appear from text alone. If it matters, QA it and say it twice
  (scene + subject).
- A 1:1 request at 1080p returns 1440×1440; 9:16 returns 1080×1920.
- Do not put captions, source badges or other overlay text in the prompt;
  they are added in post.
