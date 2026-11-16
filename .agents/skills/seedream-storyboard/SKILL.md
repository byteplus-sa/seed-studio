---
name: seedream-storyboard
description: Write and revise production-ready Seedream prompts for cinematic storyboards—from one hero panel with alternatives to a multi-panel continuity sequence. Supports two delivery modes — single-image grid (one image containing all panels, default) and separate images (one image per panel). Prompt-only, never generates or submits. Use whenever the user asks for storyboards, shot boards, continuity boards, storyboard frames, visual sequences, previsualization, scene panels, or image planning for film, advertising, animation, games, or AI video.
---

# Seedream Storyboard

Create storyboards that make narrative, shot, staging, and continuity decisions
clear before expensive production. A storyboard is a sequence-level decision
artifact, not merely a collection of attractive images.


## Input and output contract

Input: scene beats, delivery mode, relevant approved Elements, and panel geography.

Output: a panel plan and paste-ready panel or grid prompts in chat, with the ordered reference list, a parameter block, and any unresolved review requirements.

## Procedure and reference loading

Read context-and-preflight, then panel-and-grid-prompts for authoring. Read scene-density for a requested whole-scene density choice or staging that needs start, peak, end or action sub-beats. Read review-and-selection when the user shares candidates, and editing-failed-panels only for a requested revision.

Read only the mode-specific resources needed for the request. Reference paths
mentioned in prose are relative to this skill directory unless a link says otherwise.

- [Context And Preflight](references/context-and-preflight.md) — 1. Inspect existing project context; 2. Lock the brief; 3. Break the scene into observable beats; 4. Decide panel density; 5. Preflight every reference; 6. Establish geography and continuity; 7. Build the panel plan.
- [Panel And Grid Prompts](references/panel-and-grid-prompts.md) — 8. Write the exact prompt for each panel; 9. Write the multi-panel prompt; 9c. Prompt length budget; 9d. Prompt self-checks.
- [Review And Selection](references/review-and-selection.md) — 12. Review the board; 13. Present variants for the user's selection.
- [Scene Density](references/scene-density.md) — optional L1, L2 and L3 scene planning and explicit panel budgets.
- [Editing Failed Panels](references/editing-failed-panels.md) — Revising a failed panel; Revision contract.

## Prompt-only boundary and failure behavior

This skill writes prompts only. It returns a paste-ready prompt package for
Lumina or another Seed-model UI without loading sibling skills, and never
generates, uploads, downloads, edits or persists images. The user pastes the
block. Missing required inputs remain unresolved; a draft does not establish
approval.
Preserve optional timing and the requested delta. Default review uses one
sample; strict review uses three where applicable. Explicit counts win.

Preserve the selected model before considering defaults. If none is selected,
resolve the configured exact model ID and verify the requested operation,
reference count, size, format, and parameters against the current provider and
destination tool schema. Unknown capability evidence remains unresolved.
Do not substitute a model, transport, full-frame operation, or extra calls
without authorization. Offer alternatives as unselected proposals.
In prompt-only mode return the prompt, ordered references, and separate verified
or unresolved settings; do not submit. Reconcile an interrupted or ambiguous
submission before any retry or transport change.

## Source authority

Follow the official [capability matrix](https://docs.byteplus.com/en/docs/ModelArk/1824121)
and [prompt guide](https://docs.byteplus.com/en/docs/ModelArk/1829186).
If live documentation conflicts with a detail below, use it and state the
changed capability.

## What this produces

Depending on the request, produce a beat and panel plan, reference inventory,
spatial and continuity contract, exact prompts and the parameter block. Add the
full acceptance checklist only for strict or explicitly requested review.

Keep these artifacts distinct:

- **Storyboard panel:** communicates a decisive story and staging state.
- **Look frame:** locks style, palette, lighting, and materials.
- **Video keyframe:** an independently eligible non-board production still
  selected as a generation anchor, not a promoted storyboard panel.

A storyboard panel remains planning-only after fidelity inspection or selection.
These references author and revise Seedream planning images; their panel
continuity anchors and standalone-panel recipes never grant Seedance conditioning
eligibility. For every video handoff, apply [Seedance handoff](#seedance-handoff)
instead of earlier panel-promotion or supported-grid exceptions.

## Core rules

- Optimize for instant story clarity before polish.
- Describe one frozen, decisive moment per panel.
- **Always use available Elements.** Before writing any prompt, check the
  project's `elements/` records, or ask the user, for approved character,
  location, and prop sheets. Bind every visible recurring or critical Element
  by its canonical reference; incidental generic props may be described under
  the workspace prop threshold. This keeps identity, geometry, materials, and wardrobe
  on point across panels. A text description or an earlier storyboard panel is
  not a substitute for a canonical Element sheet. If an Element has no selected
  sheet, use the best available approved reference; if none exists, mark the
  asset `unresolved` and keep the output as an unlocked draft.
- Honor an explicit panel budget. When the user requests one panel, select the
  strongest representative moment instead of silently expanding the board.
- Without an explicit panel budget, add a panel when visual information or
  state materially changes.
- Keep recurring identities, locations, props, and style in an explicit canon.
- When matching canonical Element sheets exist, list the selected character,
  location, and visible-prop sheets in the reference order the user attaches in
  the destination UI.
- Treat screen direction and location geography as sequence-level constraints.
- Use coherent natural language, not comma-heavy keyword piles.
- Bind every reference by role and target with exact `@Image N` tokens.
- After a composition is approved, revise it with a narrow edit prompt or a
  revised full prompt; pixel-level edit tooling is out of scope here.
- Use seeds for experiment tracking, not as the identity system. A seed is a
  parameter-block value, never prompt text.
- Put arrows, labels, dialogue, timing, and production notes outside the
  generated image unless visible story-world text is required. Exception: in
  single-image grid mode, thin dividers and panel numbers are part of the
  layout, not annotations — they belong inside the image.
- Select an inspected candidate under the caller's approval mode: an agent
  choice under `approve_for_me`, or the user's choice under `ask_for_approval`.
  A request to choose personally always waits for that choice. A draft prompt
  or an unseen image never counts as inspected output.

## Panel delivery mode

A multi-panel storyboard can be delivered in one of two modes. The choice
affects prompt structure, model selection, output file count, and how panels
are reviewed and revised.

| Mode | Output | Default? | Best for |
|---|---|---|---|
| **Single-image grid** | One image containing all panels arranged in a grid | Yes | Quick overview, pitch boards, editorial review, sharing a whole scene at a glance |
| **Separate images** | One image per panel (N files) | No | High-resolution per-panel detail, individual editing, continuity-critical sequences |

### When to use each

- **Default to single-image grid** for multi-panel boards unless the user asks
  for separate images or the downstream workflow requires individual panels.
- **Switch to separate images** when: the user requests per-panel editing,
  the panel count is small and each panel needs high-fidelity detail, or the user explicitly says
  "one image per panel" or "separate panels."
- **Grids and separate panels remain planning-only.** Cropping a grid cell or
  regenerating it from the same canon and panel prompt does not create an
  independent video keyframe.
- **Translate storyboard staging to text for video.** A selected grid with a
  supported `reference_image` role is still ineligible for Seedance conditioning;
  selection and leakage guards do not change its origin.
- **A one-panel board is always a single image** regardless of mode — the mode
  distinction applies only when the board has two or more narrative panels.

### Grid layout

For single-image grid mode, arrange panels in a reading-order grid. Choose the
smallest grid that fits the panel count:

| Panels | Grid | Reading order |
|---|---|---|
| 2 | 1×2 or 2×1 | match aspect ratio — horizontal for 16:9, vertical for 9:16 |
| 3 | 1×3 or 3×1 | match aspect ratio |
| 4 | 2×2 | left-to-right, top-to-bottom |
| 5–6 | 2×3 or 3×2 | left-to-right, top-to-bottom |
| 7–9 | 3×3 | left-to-right, top-to-bottom |
| 10–12 | 3×4 or 4×3 | left-to-right, top-to-bottom |

Use thin divider lines between panels. Place a small panel number in the
top-left corner of each cell. Do not add speech bubbles, captions outside panel
numbers, watermarks, or decorative borders.

### Seedance handoff

Storyboard grids, panels, crops and animatics are planning-only in every video
conditioning role, including first/last-frame, R2V and motion. Crop, cleanup,
approval, selection, current hashes and board-derived regeneration do not change
planning origin. Translate approved shot order, staging, blocking and continuity
into text, not a board binding or upload. A numberless or text-free board is
still a board; regenerating a standalone from its panel prompt is not independence.

Independently authored, selected, text-free non-board production stills and
independent animated blockouts remain eligible only with verified exact
model/operation/transport roles, rights, consent where applicable, current
canonical hashes, source lineage and artifact-specific QA. Independent first-frame
stills use only supported roles; R2V uses eligible canonical assets and any
eligible independent stills, with board staging in text. Independent blockout
motion and appearance have separate authorities; storyboard animatics are excluded.
This leaf returns caller handoff notes, not video generation or approval.

Preserve historical board-linked tasks, hashes and selection records unchanged.
Earlier reports of corner numerals leaking into video are historical observations,
not evidence that any negative wording makes board conditioning eligible.

## Render style

A storyboard is a decision artifact, not a finished frame. Its job is to
communicate staging, blocking, composition, eyelines, continuity, and story
beat — not polished color rendering.

**Default to sketch style.** Unless the user requests full color, write
storyboard prompts in a monochrome or limited-palette sketch style. This keeps
generation fast, cheap, and focused on structure rather than surface polish.

| Style | When to use | Prompt keywords |
|---|---|---|
| **Pencil sketch** (default) | Most boards — editorial, continuity, pitch | "rough pencil sketch storyboard, monochrome graphite lines on white, loose shading, no color" |
| **Ink / brush sketch** | When the user wants bolder contrast or cleaner lines | "bold ink storyboard sketch, black brush lines on off-white, minimal cross-hatching, no color" |
| **Charcoal / tonal** | When lighting direction and contrast matter more than detail | "charcoal storyboard sketch, monochrome tonal shading, soft gradients, no color" |
| **Limited palette** | When color coding is part of the staging (e.g. character A warm, character B cool) | "storyboard sketch with limited color: [list only the colors that carry meaning], otherwise monochrome" |
| **Full color** | Only when the user explicitly asks for color, look frames, or style exploration | "full color cinematic storyboard, [palette and lighting]" |

### Sketch and Elements are not in conflict

Sketch style does not mean abandoning canonical Element references. Even in a
pencil sketch, bind approved character, location, and prop sheets as
`@Image N` inputs so the sketch preserves the correct face shape, body type,
costume silhouette, location geometry, and prop form. The sketch simplifies
surface detail — it does not invent a different identity.

In the prompt, pair the sketch style with an explicit binding instruction:

```text
Use the face shape, hair silhouette, and wardrobe cut from @Image 1 for Mara,
rendered as a loose pencil sketch. Preserve the room geometry and doorway
position from @Image 2. Render all surfaces as monochrome graphite — no color,
no texture detail, no material finishes.
```

## Model selection

Preserve the selected model. Resolve the configured exact model ID only when
the request has not selected one. A valid configured Pro default remains valid;
it never overrides an explicit 5.5 or future-model selection.

| Need | Path after verification | Important limits |
|---|---|---|
| Single-image grid storyboard | Selected model's single-image generation | A grid is one image, not native sequential output |
| Single panel or local correction | Selected model's generation or verified interactive edit | Check references, size, and coordinate mapping for that operation and tool |
| Separate panels in one request | Selected model with verified native sequential support | Pro and 5.5 do not support native sequential generation; unknown models are unresolved |
| Alternatives for one panel | Authorized stochastic samples or creative variants | Candidates are not story beats; optional seed controls need model and tool support |
| No verified sequential path | Offer per-panel prompts/calls from the same canon | A change in model, call count, or delivery mode requires authorization |

Known exact IDs are scoped reference data: Pro is
`dola-seedream-5-0-pro-260628`, and 5.5 is `dola-seedream-5-5-261028`.
Older Lite/4.x bindings may be candidates only after current capability and
configuration verification. Never invent a binding, treat a proposed alternative
as selected, or silently turn layers or variations into an ordered sequence.

Use the delivery aspect ratio from the brief. If absent:

- `16:9` for landscape film, television, presentation, and horizontal ads;
- `9:16` for vertical short-form work;
- use another ratio only when the intended delivery format requires it.

For rough panels, after size verification, prefer the smallest valid size that preserves the target
ratio, such as `1280x720` for 16:9. Increase resolution only after composition
and continuity are accepted.

## Default response structure

For a one-panel request, return a compact hero-beat decision, one `p010` panel
plan, reference inventory, exact prompt and any material unresolved inputs.
Use one sample by default, or three in strict mode; explicit counts win.
Do not include a full checklist or demand selection when no images exist.
For a multi-panel plan
or prompt package, return the panel delivery mode (single-image grid or
separate images), render style (sketch default or full color), assumptions and
locks, reference inventory, beat and panel plan, spatial and continuity
contract, parameter block, exact panel prompts and open decisions. When the
user shares generated candidates, inspect and select under the approval mode.
Use a concise fidelity check by default and the full table only in strict
mode or for an explicit review request.

Do not claim that a storyboard, asset, or variant exists: this skill delivers
prompts, and any image comes from the user's generation step.

## Compose with other skills

- Compose with `seedream-character-sheet` / `seedream-location-asset` /
  `seedream-prop-asset` for canonical Element references in every panel.
- Hand translated board staging and independently eligible reference notes
  to the caller for the selected Seedance adapter; boards themselves stay
  planning-only.
- Inside a reference-video reverse-engineering package, `template-factory`
  authors the storyboard prompts; use this skill for standalone boards.
