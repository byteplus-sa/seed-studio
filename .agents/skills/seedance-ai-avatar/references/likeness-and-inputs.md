# Likeness and inputs

## Gate 1: presenter consent

Ask before collecting anything:

> Do you have <Name>'s permission to create an AI avatar and voice of their likeness?

- **Yes:** proceed. Write the confirmation (date, who confirmed, scope) at the
  top of `PROVENANCE.md`.
- **No / unsure:** offer an original invented host with a similar vibe (a new
  Seedream sheet from text only and a generic voice). The rest of the flow
  stays the same.
- **The user supplies photos:** prefer them over scraping.

## Gate 2: real-likeness generation policy

Before handing off the first Seedance prompt that carries the character sheet,
ask:

> The character sheet is a photoreal likeness of <Name>. Is generating real-person video sanctioned for this account — via the provider's authorized-likeness route or a policy owner's approval? Who approved it?

Record the answer (approver, date, scope) in `PROVENANCE.md`. If it is not
sanctioned, stop after the sheet and offer: the provider's authorized-likeness
route, an original invented host, or filming the presenter.

## Where references may go

| Asset | Seedream (character sheet) | Seedance (video) |
|---|---|---|
| Real photos / reference frames of the person | Yes, as I2I identity/wardrobe refs | Never |
| Generated character sheet | — | Only after gates 1 and 2 are recorded |
| Voice clip cut from their own recording | — | Yes, as @Audio 1 (timbre only), under the same gates |
| Setting, lighting, mic, backdrop | Text | Text |

## Provider rejections

`InputImageSensitiveContentDetected.PrivacyInformation` is evidence to
diagnose and report. It is not an obstacle to route around.
- Stop. Ask for the request ID and the flagged `content[n]` indices.
- Never crop, blur, stylize, recompose, or substitute inputs to get a real
  likeness past the check.
- Revise only on the user's explicit decision, within the recorded gate 2
  approval. Log that decision.
- If the generated sheet itself is rejected, stop. It is not a candidate for
  alteration either.

## Provenance file

`PROVENANCE.md` holds, when the user asks for a saved record:
- The gate 1 and gate 2 records and any later scope decisions.
- A table of every ref: file, source (page or video name, not a signed URL),
  SHA-256.
- The voice clip: source recording, time range, processing chain.
- Every provider rejection and the decision that followed.
- A line to keep outputs private and label them as AI-generated if posted.

## Photo collection tips

- Creator sites (Framer, Linktree, podcast pages) embed many guest photos.
  Build an indexed contact sheet and pick visually, using the reference
  frames as ground truth.
- Crop the talking-head half out of split-screen reference frames. This gives
  the best wardrobe and setting ref.
- Three refs in the sheet request are enough: a headshot (face), a reference
  crop (wardrobe), and a mid shot (build).
