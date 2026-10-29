---
name: seedance-object-swap
description: >-
  Write Seedance 2.5 Object Swap prompts that replace one named element in
  existing footage (a character, outfit, product, prop or object, or the
  location behind the subjects) and preserve everything else as filmed:
  performance, camera path, cuts, lighting and event order. Covers the
  five-part swap contract (identification, object count, Timeline Inheritance,
  residual-original guard, preservation), contact and occlusion windows,
  Virtual Portrait asset:// references for realistic people, a muted source
  master with audio added in post, and swap checks. Use for product placement,
  competitor-to-own SKU swaps, wardrobe changes, single-character replacement
  or location swaps on a kept take. Prompt-only: never generates or submits.
  Not for rebuilding the whole cast or world around the source motion
  (seedance-motion-recast), whole-frame style changes (seedance-restyle), or
  new T2V/I2V shots.
---

# Seedance Object Swap

Object Swap changes **one named element** in existing footage and keeps the
rest of the shot as filmed. `@Video 1` is the sole editing master; one or more
reference images define only the target's appearance.

## Boundary

| Need | Skill | What survives from the source |
| --- | --- | --- |
| Replace one character, outfit, product, prop, object or the location | this skill | Every pixel outside the swapped element |
| New cast and world doing the same performance | `seedance-motion-recast` | Motion, camera and timing only |
| Same shot redrawn in a new visual medium | `seedance-restyle` | Content, layout, motion and camera; the look changes |
| Added creature, effect, weather, relight, or a background rebuild that relights the subjects | `seedance-vfx-prompt` | Everything except the edit |

Swap one element class per request. Two unrelated changes run as two sequential
swaps, with the user judging the first result before the second prompt. When
most of the frame changes, the job is a Motion Transfer.

## Swap classes

| Class | Target reference | Typical scope |
| --- | --- | --- |
| Character | Virtual Portrait `asset://` views | One person replaced; others kept |
| Outfit | Garment packshot, flat-lay or mannequin view | One garment on one person |
| Product | Official or authorized packshot | One product, including grip and labels |
| Prop or object | Prop sheet view | One object, including its path and contacts |
| Location | Location sheet or plate | Environment behind kept subjects |

## Input and output contract

Input:

- A source clip inspected per the
  [video-to-video inputs contract](../../contracts/video-to-video-inputs.md):
  duration, frame rate, ratio, audio streams, cuts, and footage rights the user
  has confirmed.
- The muted master and the saved source audio, prepared by the user from the
  same contract.
- One approved target element. A character target is a Virtual Portrait asset
  the user uploads; a real brand or labeled product uses the official or
  authorized asset per
  [element identification](../../contracts/element-identification.md).
- The post-audio route (original, new, mixed or re-voiced).

Output: a swap prompt package delivered in chat, with ordered
`@Video 1`/`@Image N` bindings and roles, the five-part contract facts,
contact windows, the prompt, the parameter block, the post-audio route, and
the test-ladder rung.

## Hard rules

1. **State the five-part contract**: identification, object count, Timeline
   Inheritance, residual-original guard and preservation. Read
   [swap contract](references/swap-contract.md).
2. **Realistic people are Virtual Portraits.** Recommend that the user upload
   every realistic human likeness (the target character, and the source clip
   when it shows a person) to the Virtual Portrait library and bind it as
   `asset://`, per the
   [video-to-video inputs contract](../../contracts/video-to-video-inputs.md).
   Rights and consent follow the
   [production policy](../../contracts/production-policy.md): unknown rights,
   identity and consent facts stop the work, a creative choice never supplies
   them, and calling the job a test does not either.
3. **Bind the muted master.** `@Video 1` is the muted master;
   `generate_audio` is `false`; there are no `@Audio` bindings. Sound returns in
   post through the stated route.
4. **Reference budget**: 1–5 target images, one view per image, no collage.
   Several views of one target state that the output contains only one.
5. **No baked text.** A label printed on a product is part of the product;
   captions, taglines, CTAs and end cards are added in post.
6. **Test ladder**: every new Seedance 2.5 test uses `resolution: "480p"`
   and boolean `draft: true`, including an agreed contact-window probe and the
   full clip. The caller inspects and selects the full-clip native draft before
   promotion by `draft_task_id`; changed inputs need another native draft.
   Resolve a missing draft control rather than substituting ordinary 480p.

## Route and parameters

Seedance 2.5 edit. These are parameter-block values for the destination UI,
never prompt text:

- `videos`: the muted master as `@Video 1`, first in order; an `asset://` video
  when the source shows a person.
- `images`: target views as `reference_image`, in binding order.
- `omni_reference_task_type`: `edit` when supported, not an assumed
  `edit_video` alias. Verify the current model and destination's accepted
  operation; test the current target class, contacts and camera motion without
  extrapolating success from another clip.
- Omit `ratio` and `duration` only when the destination locks them to the
  source. Preserve the exact source span, frame timestamps, cuts and playback
  speed. Do not trim, pad or retime to an assumed 8n+1 frame count or
  whole-second duration. Adapt a separate copy only to a verified destination
  requirement, with the user's agreement and the timing change recorded.
  Preserve the original video and audio.
- `generate_audio: false`, `watermark: false`, `resolution: "480p"`,
  `draft: true` for each new test; record delivery resolution separately.

Confirm the model ID and the accepted parameters in the destination UI or the
current documentation before finalizing the parameter block.
Use explicit `resolution: "480p"` and boolean `draft: true` for a new native
probe; resolve missing draft controls before submission. It does not guarantee
final-resolution quality or timing. Treat linked
preparation recipes as conditional on these checks, not default trim instructions.

## Procedure

1. **Route check.** One element class changes; everything else is kept.
2. **Source intake.** Inspect the source, confirm rights, and describe a muted
   copy preserving exact timing ([video-to-video inputs](../../contracts/video-to-video-inputs.md)).
   Propose trimming only for a requested span or verified destination constraint,
   with the user's agreement.
3. **Facts.** Inspect the source and note descriptors, counts and contact
   windows. Uncertain facts stay open questions.
4. **Target.** Confirm the approved element. For a character, recommend the
   Virtual Portrait upload and bind the views the user supplies.
5. **Prompt.** Fill the class template in
   [swap templates](references/swap-templates.md).
6. **Deliver.** Deliver bindings, facts, prompt, parameter block, audio route
   and rung in chat.
7. **Acceptance checks.** When the user shares or describes the silent output,
   apply [swap checks](references/swap-qa.md); after the user muxes the
   post-audio route, apply the audio checks.

The canonical 2.5 edit blocks and face-protection lines come from
`seedance-prompt-25` and `seedance-vfx-prompt`. These are composition hints;
this leaf does not load sibling skills.

## Prompt-only boundary and failure behavior

This skill writes prompts only. It returns a paste-ready prompt package for
Lumina or another Seed-model UI and never generates, uploads, registers assets,
submits, polls or deletes anything, and never trims, separates or muxes media.
Missing rights, an unuploaded character asset or open contact-window questions
remain open items in the package.

A provider rejection the user reports follows the rejection rule in the
[video-to-video inputs contract](../../contracts/video-to-video-inputs.md#provider-rejections).
When a take fails the checks, note the locked decisions, the one requested
delta and the observed failure, then change only one of wording, reference or
route per retry.

## Checklist

- [ ] One element class changes; recast and restyle requests routed elsewhere
- [ ] Source inspected; footage rights confirmed
- [ ] Muted master bound as `@Video 1`; source audio saved; `generate_audio: false`
- [ ] Exact source timing preserved; any adaptation tied to a verified
      destination requirement, agreed and recorded on a separate copy
- [ ] Original identified by observable descriptors and first appearance
- [ ] Object count stated for the whole video and per cut when it changes
- [ ] Timeline Inheritance clause present
- [ ] Residual-original guard phrased positively
- [ ] Contact and occlusion windows listed with approximate times
- [ ] Preservation list names faces, accessories, hands, camera and lighting
- [ ] Realistic people (target and source) recommended for Virtual Portrait upload and bound as `asset://`
- [ ] Target reference states what to ignore in the image
- [ ] 1–5 target images, one view each
- [ ] Post-audio route stated
- [ ] Ladder rung stated
