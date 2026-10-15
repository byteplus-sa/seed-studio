---
name: seedance-ai-avatar
description: >-
  Prepare a reusable AI avatar (digital twin) of a consenting real presenter
  and write lip-synced Seedance 2.5 talking-head prompts of them saying new
  lines. Covers the consent and real-likeness gates with provenance, authorized
  photo collection, a Seedream identity character sheet, a timbre-only voice
  clip cut from the presenter's own recording, locked 1:1 and 9:16 camera-beat
  talking-head templates, and take QA (identity, transcript diff, lip-sync,
  voice resemblance). Never disguises or reroutes inputs after a provider
  privacy rejection. Use when the user wants an AI avatar, digital twin, or
  voice clone of a creator, host, founder, or spokesperson speaking a new
  script in Seedance. Prompt-only; never generates or submits.
---

# Seedance AI Avatar

Turns a consenting real person into two locked assets, a **character sheet**
and a **voice clip**, and then into **talking-head prompts** for any new script.
The user pastes each prompt block into Lumina or another Seedance UI with the
named references. This skill does not write topics, source B-roll, or edit.
Its output is a take prompt that a downstream edit cuts into a finished video.

When the user asks to submit through a connected transport, follow
[generation transport](../../contracts/generation-transport.md); the gates below
still apply first.

## Hard rules

1. **Consent gate.** Before collecting photos or voice of a real person,
   confirm the user has that person's authorization and record it in
   `PROVENANCE.md`. Without it, offer an original invented host built from text
   only. See [likeness and inputs](references/likeness-and-inputs.md).
2. **Real-likeness policy gate.** Consent from the presenter does not by itself
   authorize sending their likeness to Seedance. The generated character sheet
   is still a photoreal depiction of a real person. Before any Seedance prompt
   that carries it is handed off, the user must confirm that real-likeness
   generation is sanctioned for their account or organization, for example
   through a provider authorized-likeness route or a named policy owner's
   approval. Record who approved it and when. Without that confirmation, stop
   after the character sheet and present the options in rule 3. This follows
   the real-people clause of the [production policy](../../contracts/production-policy.md).
3. **A privacy rejection is a stop, not an obstacle.** If the user reports
   `InputImageSensitiveContentDetected.PrivacyInformation`, stop and ask for the
   request ID and the flagged inputs. Never crop, blur, stylize, recompose, or
   swap inputs to get a real likeness past the check. Offer: (a) the provider's
   authorized-likeness route (a registered asset, see
   [video-to-video inputs](../../contracts/video-to-video-inputs.md)), (b) an
   original invented host, or (c) filming the presenter. Revise only on the
   user's explicit decision, within the recorded gate 2 approval, and log the
   decision in PROVENANCE.
4. **Real photos never go to Seedance.** They are Seedream identity references
   only.
5. **Voice clip is timbre-only.** Bind it with: "@Audio 1 defines <Name>'s voice
   timbre, accent and pacing only; do not reuse any words from @Audio 1."
6. **Freeze the prompt before handoff.** One paid submission per take; a
   submission must match the prompt the user saw byte for byte.
7. Outputs are an AI likeness of a real person. Tell the user to keep them
   private unless the presenter signs off, and to label them as AI-generated
   when posted.

## Element layout

Saved only when the user asks:

```
projects/<project>/elements/<id>/
  refs/ref_NN_<source>-<desc>.<ext>      real photos (Seedream only)
  refs/ref_voice-timbre.wav              8–15s clean voice (+ ref_voice-timbre-long.wav)
  prompt_char_<id>_turnaround_v01.md
  char_<id>_turnaround_vNN.png           generated sheets; one selected
  character.md                           descriptor, outfit, scene-only props, voice, selected_variant
  PROVENANCE.md                          consent, likeness-policy approval, sources, decisions
```

PROVENANCE holds no signed URLs, credentials or account data.

## Stages

### 1. Photos
Ask the user for 3–7 authorized photos of the presenter, such as their site,
socials, or frames from their own videos; prefer user-supplied photos over
scraping. Creator sites often mix in guest photos, so confirm each photo shows
the presenter, using the reference video frames as ground truth. Crop the
presenter out of split-screen frames for a clean wardrobe and setting ref.

### 2. Character sheet
Write the prompt with `seedream-character-sheet` (I2I): headshot for face,
reference crop for wardrobe, mid shot for build. Put the on-camera outfit on
the sheet, for example a knit crew-neck, chain and watch. Keep scene-only props
such as a lav mic off it. Suggest 3 seeds, compared next to the real headshot,
and let the user pick. Record `selected_variant` in `character.md`.

### 3. Voice clip
Cut an 8–15s clean clip of the presenter's own voice at a natural pause. See
[voice reference](references/voice-reference.md).

### 4. Talking-head prompt
Confirm gate 2 is recorded. Write the prompt from
[the talking-head templates](references/seedance-talking-head.md):
- **1:1 locked** take when the presenter will sit in a split-screen or card.
- **9:16 camera-beat** take when the edit goes full-screen on the presenter.

Settings to give the user: audio on, 1080p, no watermark, duration = script
length rounded up with about 1s of slack (≤30). Deliver the frozen prompt with
the references named in binding order: the selected sheet as `@Image 1` and the
voice clip as `@Audio 1`.

### 5. Take QA
- Compare a contact sheet against the selected sheet: face, hairline,
  wardrobe, accessories, props.
- Transcribe the take audio and diff it against the script. No words from the
  voice clip may appear. Keep the word timings for captions added in post.
- Check lip-sync on close frames and on plosives. Distinguish sampled-frame
  inspection from playback review.
- Voice resemblance: a rough pitch comparison is only a hint; ask the user for
  a human listen.

At most one retake, and only for a clear defect. Tell the user why before
revising.

## Known failure modes

| Symptom | Fix |
|---|---|
| `PrivacyInformation` on submit | Stop and report (rule 3). Do not alter or swap inputs to get past it. |
| Sheet panels leak in (grey bg, full-body pose) | "Use only face, hairstyle, skin tone, build and outfit; do not use the grey background, panel layout or standing pose" |
| Mic or accessory missing | Name it in both scene and subject text and QA it. It cannot come from the sheet. |
| Words from the voice clip spoken | Strengthen the timbre-only binding and keep the clip ≤15s |
| Voice resemblance weak | Retake with the 15s alternate clip |
