---
name: seedance-restyle
description: >-
  Write Seedance 2.5 Restyle prompts that redraw an entire existing clip in a
  new visual style (2D cel anime, watercolor, claymation, needle felt, toy
  miniature, stylized 3D, pixel art, woodblock, film noir and 20+ more, or a
  custom style reference image) while keeping its performance, subject
  positions, motion, camera path, cuts and timing. Covers the style catalog, the
  style-only reference role, medium-matched Virtual Portrait identity anchors,
  an environment-image recipe that restyles the background while keeping the
  same place, edit and reference routes, a muted source master with audio added
  in post, a 480p probe ladder, and restyle checks. Use to turn live action into
  animation, change the medium of an animated clip, or match a house style.
  Prompt-only: never generates or submits. Not for replacing the cast or world
  (seedance-motion-recast), swapping one element (seedance-object-swap), or
  grading or relighting the original look (seedance-vfx-prompt).
---

# Seedance Restyle

Restyle redraws every frame in a new medium. The same people do the same things
in the same place with the same camera; only the way the world is rendered
changes.

## Boundary

| Need | Skill | What survives from the source |
| --- | --- | --- |
| Same shot in a new visual medium | this skill | Content, layout, identity cues, motion, camera, cuts, timing |
| New cast or world doing the same performance | `seedance-motion-recast` | Motion, camera and timing only |
| One element replaced | `seedance-object-swap` | Every pixel outside the element |
| Grade, relight, weather or effects on the original look | `seedance-vfx-prompt` | The photographed medium |

When the style should also change who appears (for example, the restyled
figures should not depict the source people), map them to new characters: that
is a Motion Transfer.

## Input and output contract

Input:

- A source clip inspected per the
  [video-to-video inputs contract](../../contracts/video-to-video-inputs.md),
  with rights the user has confirmed for the footage and the people in it.
- The muted master and the saved source audio, prepared by the user.
- One style: a catalog ID from the [style catalog](references/style-catalog.md),
  or one to three custom style reference images (user-owned or approved
  generated frames).
- Optional identity anchors: Virtual Portrait `asset://` views of recurring
  characters, designed in the target style.
- The post-audio route.

Output: a restyle package delivered in chat, with ordered bindings and roles,
the content inventory, the style block, the prompt, the route and parameter
block, the post-audio route, and the test-ladder rung.

## Hard rules

1. **The performance stays; the medium changes.** Keep the subject count, their
   screen positions, actions, props, the furniture they use and identity cues
   (hair shape, wardrobe colours, silhouettes). The background keeps its place;
   an environment image is an optional aid (rule 9). Read
   [restyle grammar](references/restyle-grammar.md).
2. **One style per take, applied to everything.** People, props, set, sky and
   effects share one medium lock. Blends happen only on request.
3. **A style reference supplies style only**: medium, palette, line, texture
   and light quality. Never its subjects, layout or characters.
4. **No studio, artist or franchise names**, and no frames from copyrighted
   productions as style references. Copyright IP enters only as an asset the
   user is authorized to use.
5. **Realistic people are Virtual Portraits.** Recommend that the user upload
   the source clip, when it shows a person, and any identity anchors to the
   Virtual Portrait library and bind them as `asset://`, per the
   [video-to-video inputs contract](../../contracts/video-to-video-inputs.md).
   Rights and consent follow the
   [production policy](../../contracts/production-policy.md): unknown rights,
   identity and consent facts stop the work, and a creative choice never
   supplies them. Identity anchors are designed in the target medium: a photoreal sheet under
   a drawn style leaks photoreal skin.
6. **Bind the muted master** with `generate_audio: false` and no `@Audio`
   binding; sound returns in post.
7. **No baked text.** Source signage becomes abstract shapes in the style;
   captions and copy are added in post.
8. **Test ladder**: every new Seedance 2.5 test uses `resolution: "480p"`
   and boolean `draft: true`, including an agreed hardest-beat probe and the
   full clip. The caller inspects and selects the full-clip native draft before
   promotion by `draft_task_id`; changed inputs need another native draft.
   Resolve a missing draft control rather than substituting ordinary 480p.
9. **Keep the same place.** A restyle changes how the background looks, never
   where the scene is: a city street stays a city street, with the same kind of
   buildings, furniture and plants. Never name a different location unless the
   user asks for one. If the current output leaves unwanted photographic
   surfaces, or the user requests an environment reference, offer an approved
   image of that same place in the target medium (see Environment image).
10. **Source timing.** Preserve the exact source span, frame timestamps, cuts
    and playback speed. Do not trim, pad or retime to an assumed 8n+1 frame
    count or whole-second duration. Adapt a separate copy only to a verified
    destination requirement, with the user's agreement and the timing change
    recorded. Keep the original video and audio untouched.

## Routes

Route support and restyle quality are separate checks. Verify the selected
model, operation, image roles, resolution and timing constraints in the current
destination UI or documentation. Do not generalize success or failure from one
source, medium or resolution to another. A native probe uses explicit
`resolution: "480p"` and boolean `draft: true`; resolve missing draft controls
before submission. It can test the current source but is not proof that other
styles or final-resolution output will behave identically.

**If the request allows no image input,** compose a text-only whole-frame
restyle without promising coverage. If the supplied result is only partly
restyled, offer a focused medium-lock revision or another verified route.
An environment image or a subject-only scope is optional and needs agreement;
never change the location to work around a coverage failure.

These are parameter-block values for the destination UI, never prompt text:

- **Route A (default when supported): full-frame edit.**
  `omni_reference_task_type: edit`, `@Video 1` as editing master.
  Omit ratio and duration only when the destination locks them to the source.
  Use the exact source timing; an environment image is optional.
- **Route B (alternative): reference.** `auto`, or `reference` when the
  destination UI lists it, with `@Video 1` as the authority for motion, timing
  and camera, with the source content inventory and optional environment
  image. Set ratio and duration from the source only as the destination
  supports them. If exact timing is unsupported, disclose the mismatch rather
  than rounding or promising this route fixes it. Consider this route when a
  current Route A result fails the requested coverage or timing.

Both routes bind `@Video 1` as an `asset://` video when the source shows a
person. When used, bind the environment image, then style images and identity
anchors, as `reference_image` after `@Video 1`; prefer 1–5 images for Route A
within the verified limit; `watermark: false` when supported.
Confirm the model ID and the accepted parameters in the destination UI or the
current documentation before finalizing the parameter block.
Treat linked preparation recipes as conditional on these timing checks, not
as permission to trim the source by default.

### Environment image

Offer one when the current input or an observed coverage failure warrants it,
or the user selects it. Describe the source's own place in the target medium
(building style, furniture, plants and light). Use a text-to-image empty-set
prompt or a source-derived image edit as appropriate to the available approved
inputs and supported image mode. Neither method guarantees full coverage.
Check the resulting image for the target medium on every relevant surface,
source-matching geometry and absence of stray objects. Bind only an approved
image, with an Environment Reference Role naming what to use and ignore.
The source retains layout authority; disclose any geometry mismatch before use.

## Procedure

1. **Route check.** The request changes the look, not the cast or one element.
2. **Source intake.** Inspect the source, confirm rights, and describe a muted
   copy preserving exact timing. Propose a trim only for a requested span or
   a verified destination constraint, with the user's agreement.
3. **Content inventory.** List subjects with observable descriptors, key
   props, set layout, cuts, fast-motion windows and on-screen text.
4. **Style.** Pick a catalog entry or write a custom recipe from the user's
   style images; confirm the cadence note for stop-motion styles.
   Offer an environment image only when warranted by the current inputs,
   a supplied failure or the user's selection (see Environment image).
5. **Anchors.** For recurring characters, write medium-matched sheet prompts
   and recommend the Virtual Portrait upload of the approved views.
6. **Prompt.** Assemble the route template in
   [restyle grammar](references/restyle-grammar.md).
7. **Deliver** bindings, inventory, style block, prompt, parameter block, audio
   route and rung in chat.
8. **Acceptance checks.** When the user shares or describes the output, run
   [restyle checks](references/restyle-qa.md); after the user muxes the
   post-audio route, apply the audio checks.

Medium recipes in `seedance-animation-styles` and look presets in
`seedance-motion-recast` share vocabulary with this catalog; Seedream sheet and
environment prompts follow `seedream-character-sheet` and
`seedream-location-asset`. These are composition hints; this leaf does not load
sibling skills.

## Prompt-only boundary and failure behavior

This skill writes prompts only. It returns a paste-ready prompt package for
Lumina or another Seed-model UI and never generates, uploads, registers assets,
submits, polls or deletes anything, and never trims, separates or muxes media.
An unverified route, missing rights or an unapproved style reference stays an
open item. A provider rejection the user reports follows the rejection rule in
the
[video-to-video inputs contract](../../contracts/video-to-video-inputs.md#provider-rejections).

## Checklist

- [ ] Request changes the medium, not the cast or one element; other requests
      routed elsewhere
- [ ] Source inspected; footage rights confirmed
- [ ] Muted master bound as `@Video 1`; `generate_audio: false`; audio saved
- [ ] Content inventory covers every subject, key prop, cut and text surface
- [ ] Same place and layout preserved; optional environment image approved
      and checked for medium coverage, geometry and stray objects
- [ ] Exact source timing preserved; any adaptation tied to a verified
      destination requirement, agreed and recorded on a separate copy
- [ ] One style with a medium lock that names people, props, set and effects
- [ ] Style image role limited to medium, palette, line, texture and light
- [ ] No studio, artist or franchise names
- [ ] Source showing a person and any identity anchors recommended for Virtual
      Portrait upload; anchors designed in the target medium
- [ ] Stop-motion cadence note present when the style steps motion
- [ ] Source text disposition stated; no new copy requested
- [ ] Route and supported ladder rung stated; current case verified without
      treating a probe as a guarantee for other inputs or resolutions
- [ ] Post-audio route stated
