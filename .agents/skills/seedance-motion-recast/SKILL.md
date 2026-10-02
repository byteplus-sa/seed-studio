---
name: seedance-motion-recast
description: >-
  Write Seedance 2.5 Motion Transfer (recast) prompts that keep a source clip's
  body motion, pose sequence, screen positions, camera path, framing changes,
  cuts and timing while rebuilding cast, wardrobe, product, location and style
  from locked reference images. Covers the motion-only authority split, an
  explicit mapping or disposition for every visible source subject, bleed and
  extra-people guards, audio and lip-sync routes, named style presets, consent
  and real-likeness gates for real people in targets or source footage, and a
  480p key-beat probe ladder. Inspects the source clip itself. Use to recast
  performers, localize a take for another market, restyle a clip, or rebuild
  its world around the same performance. Prompt-only: never generates or
  submits. Not for changing one region or object while preserving source
  pixels (use seedance-vfx-prompt) or new T2V/I2V shots.
---

# Seedance Motion Recast

Motion Transfer rebuilds everything a viewer sees and keeps only how it moves.
The source clip supplies body motion, pose sequence, screen positions, camera
path, framing changes, hard cuts and timing. Locked reference images supply the
new cast, wardrobe, products, location and style.

## Boundary with VFX editing

| Need | Skill | Source pixels |
| --- | --- | --- |
| Rebuild cast, world and look around the same performance | this skill | Discarded; only motion and timing survive |
| Change one region, object, background, weather or light | `seedance-vfx-prompt` | Preserved outside the edit scope |

If the user wants to keep the original people, faces or location and change
only one thing, route to VFX editing instead. If they want new people in a new
place doing exactly what the source people did, stay here.

## Input and output contract

Input:

- A source clip that the agent has inspected (duration, fps, aspect ratio,
  audio presence, cuts) and whose footage rights the user has confirmed.
- The agent's own inspection of the source: an agent video pass when the client
  can watch it, or local frame extraction read as images when it cannot (see
  [multi-subject mapping](references/multi-subject-mapping.md)). Open
  ambiguities block prompt writing.
- Approved target elements (character, product, prop, location sheets or
  authorized images the user supplies), one image per view.
- The requested style (a named preset or free text) and audio route.

Output: a recast prompt package delivered in chat, containing the ordered
`@Video`/`@Image`/`@Audio` bindings with roles, the disposition table for every
source subject, the prompt text, the selected route and parameter block, the
reference-count check, and the test-ladder rung it targets.

## Hard rules

1. **Every visible source subject gets a disposition**: mapped to a reference,
   removed, or kept as a background extra. Never write "replace everyone" or
   any wording that leaves the model to guess who becomes whom.
2. **References come only from approved elements** (Seedream sheets or
   authorized images the user supplies). Use separate images per view; never
   collages or turnaround strips. The user attaches them in the order the
   package lists.
3. **Real people pass the consent and likeness gates.** A real, identifiable
   person as a target needs the user's confirmed consent and confirmed
   real-likeness generation approval. Source footage needs confirmed rights, and
   identifiable real performers in it need confirmed consent for reuse of their
   performance. Note each confirmation in the package. Unknown facts stop the
   work; a creative choice never supplies them, and calling the job a test does
   not either. Offer an invented cast or a consenting performer instead. See
   the [production policy](../../contracts/production-policy.md) and
   [element identification](../../contracts/element-identification.md).
4. **Privacy and moderation rejections are diagnosed, not routed around.** When
   the user reports a `PrivacyInformation` or other sensitive-content rejection,
   stop and ask for the request ID and the flagged inputs. Never crop, blur,
   stylize, recompose or swap inputs to get a real likeness or real footage past
   the check. Offer an invented cast, generated or owned-talent source footage,
   or the provider's authorized route, and revise only on the user's explicit
   decision.
5. **Stay within recommended reference ranges**: 1–8 distinct subjects in R2V,
   1–5 reference images in edit mode, source under 20 s for edit. Above those,
   warn the user that stability drops and propose splitting into shots.
6. **No baked text.** Keep generated footage free of captions, taglines, CTAs,
   end cards and legible signage copy; add text in post.
7. **Test ladder**: a 480p probe of the key beat, then the full duration at
   480p, then the final resolution. Each rung is a separate prompt
   block, pasted and judged by the user before the next rung.

## Mode selection (provisional)

This route is unverified. No project has yet confirmed which Seedance 2.5 mode
rebuilds appearance from references while keeping motion from a video. Ask the
user to confirm it with a low-cost 480p probe on synthetic or owned footage
before any production use, and note the result before relying on it.

- **Default route (pending verification): multimodal R2V.** Bind the source as
  `@Video 1` with role `reference_video`, stated as a motion-only reference.
  Bind targets as `reference_image`. Set `omni_reference_task_type` to `auto`,
  `ratio` to the source ratio and `duration` to the source length (4–30 s).
  These are parameter-block values for the destination UI, never prompt text.
- **Fallback plan B: full-frame edit.** If the probe output keeps the source's
  people, clothing or location, switch to the edit operation the destination UI
  offers for Seedance 2.5 and write the edit variant in
  [recast grammar](references/recast-grammar.md#plan-b-full-frame-edit-variant).
  Its scope sentence is "replace all subjects and the environment", always
  followed by the per-subject mapping. Edit mode locks duration and aspect
  ratio to the source and prefers 1–5 reference images.
- An explicit `reference` task type, if the destination UI lists it, is a second
  probe before plan B. Change one variable per probe.

Confirm the model ID and the accepted parameters in the destination UI or the
current documentation before finalizing the parameter block; do not assume a
`seed` parameter exists.

## Procedure and reference loading

1. **Route check.** Confirm the request is a recast, not a region edit.
2. **Gates.** Confirm footage rights and real-person consent for the source and
   every target before asking for references (rule 3).
3. **Source analysis.** Inspect the source yourself. Build the disposition
   table and per-cut presence.
   Read [multi-subject mapping](references/multi-subject-mapping.md).
4. **Reference budget.** Count distinct subjects, views and total images; warn
   or split per rule 5.
5. **Prompt.** Assemble the template in
   [recast grammar](references/recast-grammar.md). Add guards from
   [guards and failures](references/guards-and-failures.md), a look from
   [style presets](references/style-presets.md), and the audio block from
   [audio and lip-sync](references/audio-and-lipsync.md).
6. **Deliver.** Deliver bindings, dispositions, prompt, route, parameter block
   and ladder rung in chat.
7. **Acceptance checks.** When the user pastes the prompt and shares or
   describes the result, apply the checks in
   [guards and failures](references/guards-and-failures.md) and the lip-sync
   checks when dialogue is present.

Load only the references the request needs. A stylized medium such as
claymation or toy miniature may also use the `seedance-animation-styles`
recipes by name; the six-part formula and reference syntax stay with
`seedance-prompt-25`. These are composition hints; this leaf does not load
sibling skills.

## Prompt-only boundary and failure behavior

This skill writes prompts only. It returns a paste-ready prompt package for
Lumina or another Seed-model UI and never generates, uploads, submits, polls or
deletes anything, and never separates, trims or transcodes media. Missing
gates, unapproved references, unresolved source ambiguities or an unconfirmed
route remain open items in the package; a draft does not establish approval. A
provider rejection the user reports is evidence to diagnose (rule 4).

When the user reports a result that fails the acceptance checks, record the
locked decisions, the one requested delta and the observed failure, then change
only one of prompt wording, reference bundle or route per retry.

## Checklist

- [ ] Request is a recast; region-only edits routed to `seedance-vfx-prompt`
- [ ] Source inspected: duration, fps, ratio, audio, cuts; footage rights confirmed
- [ ] Real-person consent and likeness approvals recorded, or invented cast used
- [ ] Source ambiguities resolved; the inspection covers every cut
- [ ] Every visible source subject and swappable object has a disposition
- [ ] Each mapped subject has an observable descriptor (position, clothing, action)
- [ ] References approved, one image per view, ordered and role-bound
- [ ] Reference count within recommended range, or warning and split proposed
- [ ] Motion Authority names what `@Video 1` supplies and excludes its appearance
- [ ] Guards: exact people count, wardrobe only from references, residual originals
- [ ] Style block present; no overlay text, captions or legible signage requested
- [ ] Audio route stated, with lip-sync plan when dialogue is kept or re-voiced
- [ ] Route marked provisional until the verification probe passes
- [ ] Ladder rung stated: key-beat 480p probe, full-duration 480p, or final
