# Seedance Reference — Directorial Axes

Canonical reference for composing directorial axes from the preset skills. Each
preset skill resolves one axis into canonical prompt phrasing that drops into
the six-part formula (Subject + Action + Scene + Visual Style + Camera + Audio);
they are prompt-composition only and never call the API themselves.

| Axis | Skill | Notes |
|---|---|---|
| Requested shot planning | `seedance-shot-design` | Plan each shot's purpose, duration, framing, move, lens intent and motivated light; preserve user locks and static formats |
| Camera movement & camera styles | `seedance-camera-presets` | Named or custom paths, compatible components and ordered style transitions; move simplicity is a heuristic, not a cap on requested or delegated choreography |
| Lens / focal length / aperture / sensor | `seedance-lens-presets` | Always pairs numeric optics with the visible result; resolve requested 4K against current model capabilities |
| Lighting | `seedance-lighting-presets` | Causal lighting presets; emit both the Seedream `Lighting:` recipe (elements) and the Seedance visual-style phrase so image + video share one lighting intent |
| Color grading | `color-grade-palettes` | Named or custom looks in the Visual Style slot, including compatible combinations and ordered palette transitions; preserve approved look scope; optional post-grade filter expression for cross-shot matching in the destination workflow |
| Performance planning | `acting-direction` | Source-bound goals, tactics, listening and performance beats, returned in chat |
| Performance cue encoding | `seedance-acting-console` | Encode supplied intent without repeating scene analysis; emotion vocabulary is optional |
| Requested fictional fight action | `seedance-fight-choreography` | Readable interactions, stable actors and props; no generation or real-world combat instruction |
| Scene structure & dramaturgy | `scene-craft` | Apply the explicitly selected framework; the five-element engine is optional |
| Staging / blocking | `blocking-map` | Color-coded outline schematic for character disposition; geometry only, no style bleed |
| Pacing / rhythm | `seedance-pacing-presets` | Speed ramps and montage pacing; second-level timestamps are opt-in and not frame-accurate |
| Animation medium & handcrafted style | `seedance-animation-styles` | Material-first Seedance prompts for clay, felt, wood puppets, toys, vintage cel, painterly 2D, crafted 3D, silicone, crayon, and custom media |
| Music video | `seedance-music-video` | Song-first Seedance prompts: format (performance/narrative/conceptual/lyric/visualizer/hybrid), song-section map, beat/cut-density contract, black-sync lip-sync timing reference, and a brief-led treatment with optional genre ingredients |
| Original music / vocal master, audio-first track | `seed-audio-prompt` | Seed Audio prompt structure (T2A/TA2A) for an original music or vocal master |
| Audio commercial (story arc, cast, tagline) | `seed-audio-commercial` | Five-act commercial soundscape prompt (dialogue + BGM + SFX + ambience in one pass) with multi-character voice profiles |
| Production design: sets, props and locations with an emotional function | `seedream-location-asset`, `seedream-prop-asset` | The element manifest's optional `emotional_function` (see element identification) turns a feeling into visible design: fit, scale, height, pattern, age; a counterpoint location states a world rule |
| Editorial structure: intercut, ellipsis, inserts | `seedance-pacing-presets`, `seedance-shot-design` | Blink cuts, intercuts and vision flashes are assembly-only cuts: each side is generated at a natural length and cut in post; the scene's shot plan records them |
| Sonic motif and voice treatment | `seed-audio-prompt` | A recurring sound for a power or ordeal (layered voice, abrasive drone, solo vocal) with one curve keyed to the scene's beats |
| Storyboard prompts | `seedream-storyboard`, `template-factory` | Panel and grid prompts (sketch default, single-image grid or separate images); `template-factory` authors them inside a reference-video reverse-engineering package; full multi-scene production is out of scope in this workspace |
| Motion recast of a source clip | `seedance-motion-recast` | Keep a source clip's motion, camera, cuts and timing; rebuild cast, wardrobe, product, location and style from references |
| Object swap in existing footage | `seedance-object-swap` | Replace one character, outfit, product, prop or location and keep everything else as filmed |
| Restyle a whole clip | `seedance-restyle` | Redraw the same cast, place, motion and camera in a new visual medium |

## Composition rules

Delegated creative authorship permits custom looks, fictional staging and
camera, lens, lighting and palette proposals without user-specified preset or
technical axis names. Choose only what serves the brief; recipes are optional,
and quiet, ungraded or unchanged treatments remain valid. Label inventions as
proposals, not source facts or user approvals. Preserve explicit locks, supplied
scripts, identities, factual claims, rights and consent. Source-preserving
edits and technical conform change only the authorized `may_change` scope;
delegation does not reopen protected optics, palettes or ungraded delivery.
Keep existing approval, generation and capability checks. Use only installed
skills and available tools; missing departments remain gaps, not new installs.

Requested acting work follows [Performance direction](performance-direction.md).
Return the plan in chat and pass supplied intent to any requested coverage and
cue encoding. Do not turn that handoff into mandatory scene files or automatic
review. Source-preserving edits inherit performance; quiet holds and deliberate
non-response need no extra motion, cuts or emotional turn.

Use a preset skill for a concrete requested axis or an in-scope proposal under
delegated direction. For ordinary shots, `seedance-prompt-25` alone can suffice;
delegation does not require a preset stack or whole-scene plan. Use
`seedance-shot-design` for requested or delegated coverage and carry supplied
choices into each shot without reopening locked axes.

Compose compatible looks, motivated light sources and camera paths within the
same interval. Ordered transitions may change palette, light or camera style
across a shot or scene; state boundaries and endpoints and preserve locked
continuity. A sustained source is a choice, not a universal lighting rule.
One or two camera moves is a simplicity heuristic, not a cap on requested or
delegated choreography. Return genuine simultaneous contradictions or verified
capability conflicts; do not drop choices by count or require style purity.
Return chosen axes and resolved phrases alongside the prompt
in chat; save them only when requested.

The production design, editorial and sonic motif axes do not live in the shot
line alone. Production design reaches the element sheets and the prompt's scene
description, editorial structure reaches the shot plan's assembly cuts and the
post edit, and a sonic motif reaches the Audio block or the separate Seed
Audio prompt. When one of them is confirmed, record where it is carried.

Load `seedance-lighting-presets` / `color-grade-palettes` alongside
`seedream-prompt` when generating matching element sheets. Use
`seedance-animation-styles` when writing a Seedance prompt whose animation
medium, surface behavior, motion cadence, and handmade imperfections must stay
coherent throughout the video. Use `seedance-music-video` when the prompt's
timing, energy, and visual structure must follow the music (music video, lyric
video, visualizer, performance clip) rather than a spoken story.
