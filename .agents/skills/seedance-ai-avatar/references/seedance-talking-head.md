# Seedance talking-head templates

Settings and references to give with the pasted block: the selected sheet as
`@Image 1` (reference image), the voice clip as `@Audio 1`, audio on,
`resolution: "480p"`, boolean `draft: true`, no watermark. Keep 1080p or the
requested delivery resolution as the later promotion target. Derive duration from measured or language-aware delivery,
including onset and final-word tail, within current destination limits.
Hand off the sheet
only after the consent and real-likeness gates are recorded. Placeholders in
angle brackets (`<Name>`, `<possessive>`) are filled before the prompt is frozen.

Keep duration, resolution and aspect ratio outside the model-facing prompt,
in its parameter note. Use performance and framing descriptions in the prompt;
format exact dialogue as `Dialogue language: <language and accent>. <Name>
says: {<full script>}`.

These are optional framing recipes. Resolve topic, language, accent, setting,
delivery and final expression from the current brief. A news style, statistic,
smile or studio is not assumed for an unrelated presenter script.

## A. Locked take for split-screen (ratio 1:1)

Choose the source crop and safe area from the actual destination layout.

```
[Character]
<Name> corresponds to @Image 1. Use only <possessive> face, hairstyle, skin tone, build and outfit: <outfit list>. Do not use the grey backdrop or the multi-panel layout of @Image 1. All three panels of @Image 1 show the same one person; the output contains only one person, <Name>, throughout.

[Scene]
A small studio with a dark charcoal gradient backdrop, slightly lighter behind <possessive> head and falling off to near-black at the edges. A small black lavalier mic is clipped at the center of <possessive> sweater collar.

[Shot]
<Name> delivers <requested subject and performance> straight to camera in one continuous take, in a centered medium close-up. Use <brief-selected gestures tied to exact script words, with anatomical and frame sides>. Keep gestures inside the delivery crop and lips synchronized with the dialogue. After the last word, hold <brief-selected final expression and pose> to the end.

[Style and camera]
Soft frontal key light slightly above eye level with gentle falloff into the dark background, clean 50mm-equivalent look, neutral slightly cool studio grade with natural skin tones. Static locked-off medium close-up at eye level, no camera movement, no cuts.

[Audio reference]
@Audio 1 defines <Name>'s voice timbre, accent and pacing only; do not reuse any words from @Audio 1.

[Audio]
Dialogue language: <requested language and accent>. <Name> says with <brief-selected delivery, emphasis and pauses>: {<full approved script>}
Quiet studio room tone only. No background music. No subtitles or on-screen text.
```

## B. Vertical take with camera beats (ratio 9:16)

Use for remix edits that go full-screen on the presenter. Add a `[Timeline]`
with 4–5 timestamped beats covering the full duration: medium waist-up →
slow push-in to chest-up on the pivot line → ease back → hold for the closer.
Tie one gesture to one quoted word per beat, naming anatomy and frame side,
and keep gestures inside the frame edges, and end the last beat with a held pose. Add: "Single continuous take,
vertical framing, <Name> centered and facing the camera throughout." and
"Close lavalier-mic studio voice with quiet room tone. No background music."

## Notes

- Budget for speech onset and a complete final word with a quiet tail. The
  word-count estimate is language-specific; do not silently accelerate or
  rewrite an approved script to fit. Split it or request an authorized edit.
- Anatomical left is frame-right for a front-facing, unmirrored presenter;
  establish orientation first if the shot is mirrored or the presenter turns.
  Keep the active gesture visible through every crop and camera beat.
- Wardrobe and accessories come through the sheet, but the lav mic does not
  reliably appear from text alone. If it matters, QA it and say it twice
  (scene + subject).
- Inspect and select the native draft before promotion by `draft_task_id`.
  Resolve missing draft controls in the destination rather than using plain
  480p; creative retries require a new native draft. Confirm supported final
  resolution and actual output dimensions. Repeat transcript, final-word
  timing and lip-sync checks on the delivered final even when a draft passed.
- Do not put captions, source badges or other overlay text in the prompt;
  they are added in post.
