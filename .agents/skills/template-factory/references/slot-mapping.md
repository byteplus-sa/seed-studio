# Slot Mapping — breakdown → prompt slots

How each `VideoBreakdown` field maps into Seedream and Seedance prompt slots.
This keeps the mapping reproducible and prevents slot drift.

## Seedance 2.5 six-part formula (via `seedance-prompt-25`)

| Six-part slot | Source field(s) | Notes |
| --- | --- | --- |
| Subject | `elements[]` descriptors, bound to `@Image N` | Copy descriptors word for word; never summarize |
| Action | `shots[].action` + `shots[].motion` imperative wording | Per-shot stages with end states; motion wording is the anti-static fix |
| Scene | `elements[]` location descriptors | `@Image` binding |
| Visual style | `shots[].lighting`, requested shot-specific choices, then `visual_style` defaults | Shot lighting wins for that shot; order: lighting → lens → grade → film |
| Camera | `camera` + per-shot `shots[].camera` + `shots[].motion.camera_motion` | ≤2 moves per shot |
| Audio | `shots[].audio` + verified `audio` | `( )` music, `< >` SFX, `{ }` dialogue; transcribe only verified dialogue; `No audio at all` only when silence is verified |

## Per-shot scope

Carry observed shot-specific lighting and camera grammar into that shot rather
than flattening the whole sequence into one setup. Requested lens or pacing
changes apply only to their assigned shots. A shared default fills an axis only
when that shot has no explicit choice; preserve one shared grade unless the
user requests a change. Bind each shot to its own applicable references so a
location or look does not leak across cuts. Do not infer measured focal length
or speed from footage; use observable perspective and motion descriptions when
those values are unknown.

## Reference binding order (Seedance)

1. Build the eligible input set: approved element references, and any
   explicitly selected production panel. Omit analysis sketches by default;
   translate their choreography into text.
2. Assign `@Image N` in the exact paste order, with one role per input.
   Intentional control-image conditioning requires explicit user selection.

The ordered reference list delivered beside the prompt must match the
`@Image N` tokens exactly.

## Static element routing

| Type | Prompt skill | Reference id |
| --- | --- | --- |
| character | `seedream-character-sheet` | `char_<id>` |
| location | `seedream-location-asset` | `loc_<id>` |
| prop | `seedream-prop-asset` | `prop_<id>` |
| invented or illustrative screen/card imagery | `seedream-prompt` | `screen_<id>` |
| exact screen/UI, title card, poster, product layout, price/CTA, logo | Out of scope in this workspace — say so | — |

Bind the breakdown's flagged keyframe as `@Image 1` (image-to-image) where
one exists.

## Storyboard

- Panel count defaults to `shots.length`; an explicit user budget wins and
  must retain a documented mapping from every source shot to a panel or
  combined beat.
- Render defaults to monochrome sketch. Honor an explicit limited-palette,
  full-color, or standalone-production-panel request.
- Delivery defaults to the smallest readable single-image grid. Use separate
  panels when the user wants individual images.
- Authoring templates and the prompt-length budget live in
  [storyboard-prompts.md](storyboard-prompts.md).
