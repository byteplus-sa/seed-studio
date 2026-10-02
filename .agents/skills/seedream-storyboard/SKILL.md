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

Read context-and-preflight, then panel-and-grid-prompts for authoring. Read review-and-selection when the user shares candidates, and editing-failed-panels only for a requested revision.

Read only the mode-specific resources needed for the request. Reference paths
mentioned in prose are relative to this skill directory unless a link says otherwise.

- [Context And Preflight](references/context-and-preflight.md) — 1. Inspect existing project context; 2. Lock the brief; 3. Break the scene into observable beats; 4. Decide panel density; 5. Preflight every reference; 6. Establish geography and continuity; 7. Build the panel plan.
- [Panel And Grid Prompts](references/panel-and-grid-prompts.md) — 8. Write the exact prompt for each panel; 9. Write the multi-panel prompt; 9c. Prompt length budget; 9d. Prompt self-checks.
- [Review And Selection](references/review-and-selection.md) — 12. Review the board; 13. Present variants for the user's selection.
- [Editing Failed Panels](references/editing-failed-panels.md) — Revising a failed panel; Revision contract.

## Prompt-only boundary and failure behavior

This skill writes prompts only. It returns a paste-ready prompt package for
Lumina or another Seed-model UI without loading sibling skills, and never
generates, uploads, downloads, edits or persists images. The user pastes the
block. Missing required inputs remain unresolved; a draft does not establish
approval.
Preserve optional timing, the three-variant sampling default where applicable,
and the requested delta.

## Source authority

Follow the official [capability matrix](https://docs.byteplus.com/en/docs/ModelArk/1824121)
and [prompt guide](https://docs.byteplus.com/en/docs/ModelArk/1829186).
If live documentation conflicts with a detail below, use it and state the
changed capability.

## What this produces

Depending on the request, produce a beat and panel plan, reference inventory,
spatial and continuity contract, exact prompts and the parameter block, and an
acceptance checklist the user applies to the images they generate.

Keep these artifacts distinct:

- **Storyboard panel:** communicates a decisive story and staging state.
- **Look frame:** locks style, palette, lighting, and materials.
- **Video keyframe:** a polished image promoted as a generation anchor.

A storyboard panel may later become a keyframe, but only after the user
confirms it passes both storyboard and visual-anchor review.

## Core rules

- Optimize for instant story clarity before polish.
- Describe one frozen, decisive moment per panel.
- **Always use available Elements.** Before writing any prompt, check the
  project's `elements/` records, or ask the user, for approved character,
  location, and prop sheets. A storyboard must bind every visible Element by
  its canonical reference so identity, geometry, materials, and wardrobe stay
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
- A candidate the user generates is a draft until the user chooses. Only an
  explicit user choice selects a variant or approves a panel; a
  recommendation alone never does.

## Panel delivery mode

A multi-panel storyboard can be delivered in one of two modes. The choice
affects prompt structure, model selection, output file count, and how panels
are reviewed and promoted.

| Mode | Output | Default? | Best for |
|---|---|---|---|
| **Single-image grid** | One image containing all panels arranged in a grid | Yes | Quick overview, pitch boards, editorial review, sharing a whole scene at a glance |
| **Separate images** | One image per panel (N files) | No | High-resolution per-panel detail, individual editing, video keyframe promotion, continuity-critical sequences |

### When to use each

- **Default to single-image grid** for multi-panel boards unless the user asks
  for separate images or the downstream workflow requires individual panels.
- **Switch to separate images** when: the user requests per-panel editing,
  panels need to be promoted individually to video keyframes, the panel count is
  small and each panel needs high-fidelity detail, or the user explicitly says
  "one image per panel" or "separate panels."
- **A single-image grid cannot be directly promoted to a video keyframe.** To
  promote a panel from a grid, the user crops it or generates that panel as a
  standalone image from the same canon and the panel's prompt section.
- **Keep a sketch grid control-only by default.** Translate its composition,
  shot order, and blocking into prompt text. Bind the whole grid in a Seedance
  prompt only when the user explicitly chooses it as conditioning, the
  destination mode accepts its `reference_image` role, and the Seedance prompt
  carries the planning-sheet guard in [Seedance handoff](#seedance-handoff).
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

Panel numbers, dividers, and sketch lines are annotations on a planning sheet,
not scene content. When a board is bound to a Seedance prompt, tell the Seedance
prompt writer to: bind the grid as a planning sheet only; name every board mark
(numbers, digits, badges, dividers, captions, sketch style) as an annotation
that must never appear in the video, including all four frame corners; refer to
shots by reading position ("the first panel"), not by the printed numerals; and
end each shot line with "one clean full-frame image". A single "do not copy
panel numbers" clause has not been enough: boards with corner numerals have
leaked the same digits into every generated shot. When the board will condition
a Seedance prompt, prefer a numberless grid or separate images.

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

Choose the path according to the production need.

| Need | Preferred path | Important limits |
|---|---|---|
| Single-image grid storyboard (multiple panels in one image) | Seedream 5.0 Pro, `dola-seedream-5-0-pro-260628` | Single-image output; up to 10 references; 1K/2K; works because the grid is one image |
| Precise single panel, or a narrow edit prompt for one failed panel | Seedream 5.0 Pro, `dola-seedream-5-0-pro-260628` | Single-image output; up to 10 references; 1K/2K |
| Coordinated multi-panel sequence as separate images in one request | Seedream 5.0 Lite or configured 4.x binding | Supports multiple outputs; input references + outputs must stay within the live model limit |
| Three alternatives for one panel | Three samples of the same prompt, v01–v03 | Each output is a candidate, not an ordered story sequence |
| No sequence-capable model available | Pro, one panel at a time from the same canon | Reuse the same approved anchors and continuity record |

Never invent a model binding. If Lite or 4.x is not available to the user,
either write individual Pro panel prompts or deliver the sequence prompt and
state what binding is needed.

Use the delivery aspect ratio from the brief. If absent:

- `16:9` for landscape film, television, presentation, and horizontal ads;
- `9:16` for vertical short-form work;
- use another ratio only when the intended delivery format requires it.

For rough Pro panels, prefer the smallest valid size that preserves the target
ratio, such as `1280x720` for 16:9. Increase resolution only after composition
and continuity are accepted.

## Default response structure

For a one-panel request, return a compact hero-beat decision, one `p010` panel
plan, reference inventory, exact prompt, a note that the user generates three
samples (v01–v03) of it, video-handoff recommendation, review checklist, and
selection needed. For a multi-panel plan
or prompt package, return the panel delivery mode (single-image grid or
separate images), render style (sketch default or full color), assumptions and
locks, reference inventory, beat and panel plan, spatial and continuity
contract, parameter block, exact panel prompts, review checklist, and open
decisions. When the user shares generated candidates, add a review against the
acceptance checks and a recommendation.

Do not claim that a storyboard, asset, or variant exists: this skill delivers
prompts, and any image comes from the user's generation step.

## Compose with other skills

- Compose with `seedream-character-sheet` / `seedream-location-asset` /
  `seedream-prop-asset` for canonical Element references in every panel.
- Hand a board that conditions a Seedance prompt to `seedance-prompt-25`
  (keyframes, storyboards, blockouts) together with the Seedance handoff notes.
- Inside a reference-video reverse-engineering package, `template-factory`
  authors the storyboard prompts; use this skill for standalone boards.
