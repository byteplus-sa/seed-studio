# Seedance Reference — Directorial Axes

Canonical reference for composing directorial axes from the preset skills. Each
preset skill resolves one axis into canonical prompt phrasing that drops into
the six-part formula (Subject + Action + Scene + Visual Style + Camera + Audio);
they are prompt-composition only and never call the API themselves.

| Axis | Skill | Notes |
|---|---|---|
| Requested shot planning | `seedance-shot-design` | Plan each shot's purpose, duration, framing, move, lens intent and motivated light; preserve user locks and static formats |
| Camera movement & camera styles | `seedance-camera-presets` | Moves, techniques (dolly zoom, FPV, bullet-time orbit, one-take), and 10 camera styles; keep ≤2 moves per shot |
| Lens / focal length / aperture / sensor | `seedance-lens-presets` | Always pairs numeric optics with the visible result; resolve requested 4K against current model capabilities |
| Lighting | `seedance-lighting-presets` | Causal lighting presets; emit both the Seedream `Lighting:` recipe (elements) and the Seedance visual-style phrase so image + video share one lighting intent |
| Color grading | `color-grade-palettes` | Named palettes + film looks in the Visual Style slot; keep one project-wide palette; optional post-grade filter expression for cross-shot matching in the destination workflow |
| Acting / emotion | `seedance-acting-console` | Scene-level analysis (motive, tactic, eye-work) + per-character cue encoding (6 emotions × 3 intensities); optional audio reinforcement via `seed-audio-prompt` |
| Scene structure & dramaturgy | `tig-scene-engine` | Five-element engine (Goal, Obstacle, Tactic, Reversal, Value Shift); bespoke definitions — do not substitute textbook craft |
| Staging / blocking | `tig-blocking-map` | Color-coded outline schematic for character disposition; geometry only, no style bleed |
| Pacing / rhythm | `seedance-pacing-presets` | Speed ramps and montage pacing; second-level timestamps are opt-in and not frame-accurate |
| Animation medium & handcrafted style | `seedance-animation-styles` | Material-first Seedance prompts for clay, felt, wood puppets, toys, vintage cel, painterly 2D, crafted 3D, silicone, crayon, and custom media |
| Music video | `seedance-music-video` | Song-first Seedance prompts: format (performance/narrative/conceptual/lyric/visualizer/hybrid), song-section map, beat/cut-density contract, black-sync lip-sync timing reference, and a per-genre style lock |
| Original music / vocal master, audio-first track | `seed-audio-prompt` | Seed Audio prompt structure (T2A/TA2A) for an original music or vocal master |
| Audio commercial (story arc, cast, tagline) | `seed-audio-commercial` | Five-act commercial soundscape prompt (dialogue + BGM + SFX + ambience in one pass) with multi-character voice profiles |
| Storyboard prompts | `seedream-storyboard`, `template-factory` | Panel and grid prompts (sketch default, single-image grid or separate images); `template-factory` authors them inside a reference-video reverse-engineering package; full multi-scene production is out of scope in this workspace |
| Motion recast of a source clip | `seedance-motion-recast` | Keep a source clip's motion, camera, cuts and timing; rebuild cast, wardrobe, product, location and style from references |
| Object swap in existing footage | `seedance-object-swap` | Replace one character, outfit, product, prop or location and keep everything else as filmed |
| Restyle a whole clip | `seedance-restyle` | Redraw the same cast, place, motion and camera in a new visual medium |

## Composition rules

Use a preset skill only when the user asks for a concrete axis ("dolly in on her
face", "teal and orange grade", "Rage at medium intensity", "bullet-time
slow-mo"). For ordinary shots without such direction, `seedance-prompt-25` alone
is sufficient. Use `seedance-shot-design` when the user requests a shot list,
coverage or a more dynamic camera and light plan; carry the supplied plan into
each shot without adding unrequested axes. Do not let two skills fight: exactly
one grade per clip, one dominant lighting direction per shot, and 1–2 camera
moves per shot. Return chosen axes and canonical phrases alongside the prompt
in chat; save them only when requested.

Load `seedance-lighting-presets` / `color-grade-palettes` alongside
`seedream-prompt` when generating matching element sheets. Use
`seedance-animation-styles` when writing a Seedance prompt whose animation
medium, surface behavior, motion cadence, and handmade imperfections must stay
coherent throughout the video. Use `seedance-music-video` when the prompt's
timing, energy, and visual structure must follow the music (music video, lyric
video, visualizer, performance clip) rather than a spoken story.
