# AGENTS.md — seed-prompt-studio

Prompt-first workspace for composing Lumina-paste-ready prompts for BytePlus
Seed-family models (Seedance, Seedream, Seed Audio) and OmniHuman 2.0
lip-sync video. It writes prompts; default review is one inline preflight,
not a full checklist pipeline. Generation and media production
are optional when requested or necessary to complete a user-authorized
deliverable with available tools.

## Scope and authority

This workspace produces copy-paste prompt blocks. By default the user pastes
them into Lumina or another Seed-model UI, where generation happens. When the
user requests generation or a deliverable requiring generated Seed media,
and a usable `ark-mcp` or `arkcli` is connected, or the user explicitly requests
direct HTTP/curl with an established secure runtime configuration, follow
[Generation transport](.agents/contracts/generation-transport.md): show the exact
prompt, confirm each submit, use one transport per job. With no usable selected
transport, stay prompt-only and say so. The workspace never assumes, configures,
or stores generation credentials.

Per-submit confirmation is generation opt-in, not financial approval. Do not
require project or generation budget declarations, caps, cost estimates or
spending authorization. Cost information is optional and never a prerequisite
for prompt delivery, analysis or a confirmed submit. Keep native-draft,
provider-limit, rights, consent and duplicate-submission safeguards intact.

Within the authorized task, agents may generate media, download references
and results, prepare audio/video inputs, trim, mux, concatenate, assemble,
transcode, and export deliverables using available tools, including local
`ffmpeg`/`ffprobe`. Save outputs to the user's requested destination, including
Desktop when requested. Preserve source assets and existing takes; do not
overwrite unrelated files. These permissions override prompt-only,
analysis-only, and destination-workflow-only restrictions in linked contracts
and skills for these operations. Other generation approval, reference,
security, and verification requirements still apply. Unrelated 3D, Blender,
and deterministic graphics workflows remain out of scope.

Deliver prompts in chat by default. Save a draft under
`projects/<name>/prompts/` only when the user explicitly asks.

Task scope does not expand into unrelated global configuration, external
publishing, or production edits. Keep project-specific instructions in
`.agents/`. Do not create a second competing `.agents/AGENTS.md`.

Before editing, inspect relevant files, plans and existing Git changes. Never
revert, overwrite or clean up work you did not create for this task. Ask for
missing information when it materially affects the intended result.

## Operational contracts

Load only the contract relevant to the current request:

| Need | Tracked source |
| --- | --- |
| Default/strict review depth, independent of decision authority | [Review mode](.agents/contracts/review-mode.md) |
| Manual `/prompt-review` policy and stable rule IDs | [rules.json](.agents/contracts/rules.json) and [production policy](.agents/contracts/production-policy.md) |
| Requested camera, lens, lighting, grade, acting, pacing, blocking, medium axes | [Directorial axes](.agents/contracts/seedance-reference.md) |
| Requested performance plans, cue encoding and fictional action | [Performance direction](.agents/contracts/performance-direction.md) |
| Canon, props, screens and reference roles | [Element identification](.agents/contracts/element-identification.md) |
| Dialogue synchronization and assembly | [Audio-video alignment](.agents/contracts/audio-video-alignment.md) |
| Source footage, Virtual Portrait identities, muted master and post audio for swap, recast and restyle | [Video-to-video inputs](.agents/contracts/video-to-video-inputs.md) |
| Explicit request to generate or submit a prompt | [Generation transport](.agents/contracts/generation-transport.md) |

## Routing

Compose requested axes and in-scope proposals under delegated creative
authorship, including custom looks, compatible light and camera variations, and
ordered transitions. Camera simplicity is a heuristic, not a move-count cap.
Preserve explicit locks, the brief, rights, consent and verified capabilities;
source-preserving edits and conform change only authorized axes. Return actual
simultaneous contradictions for clarification without imposing recipe purity.

| Intent | Route |
| --- | --- |
| Brief shaping | `brief-intake` |
| Requested shot list, coverage or dynamic camera and light plan | `seedance-shot-design` |
| Named visual-effect recipes and effect menu | `seedance-effects-studio` |
| Reference-video reverse engineering (breakdown → element, storyboard, Seedance prompts) | `template-factory` |
| Storyboard panel and grid prompts | `seedream-storyboard` |
| Motion recast of a source clip (new cast and world, same motion) | `seedance-motion-recast` |
| Object swap in existing footage (one character, outfit, product, prop or location) | `seedance-object-swap` |
| Restyle a whole clip into a new visual medium (same cast, place and motion) | `seedance-restyle` |
| Seedance 2.5 prompt grammar | `seedance-prompt-25` |
| Seedance 2.0 / 4K legacy grammar | `seedance-prompt-20` |
| Filipino/Tagalog dialogue direction | `seedance-prompt-25-filipino` |
| Filipino micro-drama stories and episode briefs | `filipino-micro-drama` |
| Character goals, tactics, listening and performance beats | `acting-direction` |
| Encode supplied performance intent for Seedance | `seedance-acting-console` |
| Requested fictional screen-fight choreography | `seedance-fight-choreography` |
| Camera / lens / lighting / pacing presets | `seedance-camera-presets`, `seedance-lens-presets`, `seedance-lighting-presets`, `seedance-pacing-presets` |
| Frame-break pop-out effect (subject bursts over black bars, 3D billboard look) | `seedance-frame-break` |
| Animation styles / Blender-video edit prompts | `seedance-animation-styles`, `seedance-graybox-world` |
| Motion design / music video / restoration / VFX edit prompts | `seedance-motion-design`, `seedance-music-video`, `seedance-restoration`, `seedance-vfx-prompt` |
| Seedream image prompts, character sheets, location plates, prop sheets | `seedream-prompt`, `seedream-character-sheet`, `seedream-location-asset`, `seedream-prop-asset` |
| Handcrafted painterly 3D character portraits, sheets and wardrobe material studies | `seedream-handcrafted-3d` |
| Engraved woodblock-style illustrated posters and cohesive folklore or creature series | `seedream-woodblock-poster` |
| Seedream edit prompt that leaves one readable face on a character sheet | `seedream-character-sheet-cleanup` |
| New outfit on an approved character sheet | `seedream-character-outfit` |
| Authorized AI avatar or digital twin of a consenting presenter, talking-head takes | `seedance-ai-avatar` |
| Seed Audio prompts | `seed-audio-prompt` |
| Audio commercial prompts (story arc, cast, tagline) | `seed-audio-commercial` |
| OmniHuman 2.0 lip-sync prompts (one image + driving audio) | `omnihuman-prompt-20` |
| UGC ad modes / UGC motion presets | `ugc-ad-modes`, `ugc-motion-presets` |
| Color grade sentence | `color-grade-palettes` |
| Scene structure / staging references | `scene-craft`, `blocking-map` |
| Prompt QA (manual; only when the user runs `/prompt-review`) | `prompt-review` |

## Skills and orchestration

One skill provides one capability. Leaf skills remain independently usable;
composition hints are prose, not directives to load siblings. Load only the
specialists needed for the current request. `template-factory` is this
workspace's declared orchestrator for reference-video reverse engineering; it
sequences the prompt leaves.

This workspace ships prompt-composition skills only, plus the maintenance-only
`sync-skills` skill, which runs on explicit request. Generation is a transport
contract, not a skill: it uses the user's connected `ark-mcp` or `arkcli`, or
explicitly requested direct HTTP/curl with existing runtime authentication.
Prompt leaves and `template-factory` produce prompts; the calling agent owns
authorized submission and media production. No installed media-processing
skill is required to use available tools for the operations permitted above.
Recipes such as muxing a song onto a video may be executed by the agent when
needed for the authorized deliverable; otherwise deliver them as instructions.
Do not assume unavailable tools or expand into unrelated production work.

Review depth is `review_mode: default` unless explicitly set to `strict`.
Default uses a compact inline preflight; strict adds validity explanations
and detailed candidate inspection without invoking manual prompt review.
`approval_mode: approve_for_me` separately lets the agent make in-scope creative
decisions; `ask_for_approval` waits for user decisions in either review mode.
Never infer permission for review sub-agents from either setting.
Prompt QA runs only when the user invokes `/prompt-review`; no prompt-writing
skill or workflow runs, loads, or waits on it.
See [Review mode](.agents/contracts/review-mode.md) for chat-only toggles,
sampling, final sanity checks and the safeguards that remain in both modes.

For requested performance work, pass the source-bound intention and relevant
beats from direction to cue encoding, with coverage only when requested.
Return these in chat; scene files and hashes are not prerequisites. Preserve
quiet holds, exact dialogue and source performances. The five-element scene
engine and named fighting styles are opt-in, not universal defaults.

For new, underspecified moving-image work, resolve a compact creative premise
in chat: intended audience response, what carries attention, and why the ending
matters. Use supplied intent first; ask about material gaps and offer distinct
alternatives only while the idea is unresolved. Settled prompt edits do not
need a new treatment or whole-scene plan.

Carry early sound and edit intent alongside the prompt: what is revealed,
withheld or sustained, and whether sound or silence supports that moment.
Suggest brief-specific observable acceptance checks, not approval records.
Separate actor energy, camera energy and edit rhythm; derive each from the
brief and readable action. Slow motion, repeated holds, equal durations,
energetic dialogue and repeated framing are valid when purposeful. No cadence,
coverage, turn, burst or "wow" quota supersedes that intent. See the existing
performance contract for this inline handoff and its evidence limits.

Keep skill metadata concise and valid YAML. Move substantial conditional
modes and examples into focused same-skill references.

## Portable content

Market, language, register, setting and identity come from the current brief,
not the installed skill list or previous projects. Use a market-specific pack
only when the user requests that market or confirms it in the brief. Ask when
a missing choice materially changes the output; do not silently choose Taglish
or any other language. Preserve approved dialogue verbatim.

Keep shared skills independent of real local clients, prior production results,
personal paths and private links. Use clearly fictional, varied examples and
parameterized paths, never example values as runtime defaults. Reuse project
assets or context only when explicitly selected for the current task.

## Prompt invariants

- Never run `prompt-review` on your own, including in strict mode. Review
  happens only when the user invokes `/prompt-review`; it never gates handoff
  or generation. Review sub-agents require a separate explicit request.
- Freeze the exact prompt text before handoff. A generation submit must match
  the prompt the user saw byte for byte.
- Every new Seedance 2.5 generation starts in native draft mode with explicit
  `resolution: "480p"` and boolean `draft: true`, including edits, extensions,
  retries and first tests. A delivery target does not skip this first pass.
  Keep these settings outside prompt text. The caller inspects and selects the
  draft before promotion by `draft_task_id`; changed creative inputs need a new
  native draft. A tool or UI that cannot expose draft mode is a capability
  mismatch to resolve, not permission to silently send ordinary 480p.
  Other video models without native draft mode use an ordinary 480p test,
  clearly labeled non-promotable. Do not invent unsupported parameters.
- Prefer an agent video pass when the client can watch the source, or local
  `ffmpeg`/`ffprobe` frame extraction read with image perception. When native
  perception is insufficient, the caller may use a capable available analysis
  tool under privacy and explicit offline constraints. Record actual
  inspected ranges, tool provenance and uncertainty; never claim to have
  watched footage you could not access or continuously reviewed sparse frames.
- Audio requires actual auditory perception or documented human listening.
  Transcripts, waveforms and player launches do not verify soundscape. Native
  host reasoning is not necessarily on-device; offline requests require
  verified on-device perception or human evidence. Continue supported analysis
  with unavailable modalities unresolved; analysis is not generation approval.
- Preserve exact canonical descriptors where applicable. Prefer positive,
  observable direction; necessary edit-scope exclusions are allowed.
- Identify all visible props; only threshold-qualified props need locked
  references. Incidental generic props may be described.
- Do not bake captions, taglines, CTAs, end cards or other overlay text into
  prompts; on-screen text is added in post by the destination workflow.
- Static sheets use visible-design criteria; narrative shots need action and
  intent; audio uses its requested sound arc. Do not apply narrative tactics
  to every static sheet.
- Moderation rejection is evidence to diagnose, not proof of a false
  positive. Revisions remain legitimate and authorized.
- Exact-copy, typography, logo, UI, and deterministic HTML/CSS/SVG work is
  out of scope; say so rather than improvising a prompt.

## Local state and naming

`projects/<project-name>/` holds durable local drafts, never a default Git
staging target.

| Location | Contents |
| --- | --- |
| `projects/<project>/project.md` | Optional brief and confirmed choices |
| `projects/<project>/prompts/prompt_<asset-stem>.md` | Saved prompt drafts, immutable after handoff |
| `projects/<project>/elements/<element-id>/` | Optional element prompt records and acquired-asset provenance |
| `projects/<project>/generations/<asset-stem>.md` | Optional generation provenance record, saved on request; no signed URLs |
| `projects/<project>/frames/` | Analysis-only frame-extraction scratch; never a deliverable |

Folders and IDs use lowercase kebab-case. Prompt snapshots are saved only on
explicit request; chat-only is the default.

## Security and change boundaries

No credentials belong in this workspace; prompts and drafts contain no
secrets, signed URLs, or account data. Never output or commit credentials.

Never commit or push repository changes unless requested. When authorized,
stage only task-owned files. Clean up only your own temporary artifacts;
never revert or discard work you did not create.

## Verification

Prompt QA is optional: the user runs `/prompt-review` when they want it. For
repository changes run `git diff --check`, the maintenance metadata/link
validator and nonpaid policy regressions:

```bash
python3 -B .agents/skills/sync-skills/scripts/verify.py
python3 -B -m unittest discover -s tests -p 'test_*.py' -v
python3 -B .agents/skills/sync-skills/scripts/test_generation_policy.py
bash -n .agents/skills/sync-skills/scripts/sync.sh
```

These check repository instructions, not generated media or live model
behavior. Prompt skills ship no runtime code; application lint, type and build
checks are not applicable.

For produced media, verify output existence, audio/video streams, dimensions,
duration, and full decode integrity before delivery. When exact original audio
is required, preserve it without re-encoding where supported and verify audio
payload or decoded-sample equality. Technical checks do not establish visual
quality or lip sync; distinguish sampled-frame inspection from playback review.

Shared skills are maintained in an upstream source checkout and pulled in with
`/sync-skills` in Claude Code or opencode, or `$sync-skills` in Codex (see README
Maintenance). The command never overwrites the local `template-factory`,
`seed-audio-commercial`, `filipino-micro-drama`, `seedream-prop-asset`,
`seedream-storyboard`, `seedream-character-sheet-cleanup`,
`seedance-motion-recast`, `seedance-object-swap`, `seedance-restyle`,
`seedance-frame-break`, `seedance-graybox-world`, `seedance-music-video`,
`seedance-shot-design`, `seedance-effects-studio`, `seedream-handcrafted-3d`,
`seedream-woodblock-poster`, `seedream-character-outfit`, `seedance-ai-avatar`,
`acting-direction`, `seedance-acting-console`, `seedance-fight-choreography`,
`scene-craft`, and `blocking-map` forks and leaves its changes uncommitted for review.
