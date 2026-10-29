# Audio Evidence

Use when the requested breakdown depends on source sound. Adapted from
[upstream PR #47](https://github.com/byteplus-sa/ark-director/pull/47) at
`391d5c67718c9c8b0606368ee4ad552fea79678b`. This is an analysis checklist,
not a generation step or a bundled provider integration.

## Establish access and perception separately

1. Probe the original media with available `ffprobe`. Enumerate audio streams
   with their absolute stream index, language/title tags and default disposition,
   duration, start time, channels and sample rate. Select the stream requested
   by the user, or the sole audio stream; when several tracks have no clear
   intended choice, ask which mix or language to analyze. Record the selected
   absolute index. Use `absent` only after a successful probe shows no audio
   stream. An inaccessible or undecodable stream is `unavailable`, not silent.
2. Prefer actual native audio input or a verified on-device audio model.
   If unavailable, the caller may use a permitted audio-understanding tool,
   or obtain documented human listening notes. Record which route heard
   the audio; never relabel tool output or human notes as native listening.
3. Check privacy and explicit offline constraints before any remote
   analysis; no budget declaration or financial approval is required.
   A local command can invoke a remote model; it does not establish
   on-device inference. Do not require provider setup for capable native
   analysis, or require local tools when a permitted capable route exists.
4. Cover the whole selected soundtrack, including any tail after the picture.
   Bind native playback and any extraction to the selected stream. For an
   extraction, have the caller use explicit mapping such as `-map 0:<index>`
   with the absolute stream index, recording the command and derived audio
   hash without changing the source. If a native/tool route cannot identify
   which track it heard, use an explicitly mapped single-track input or leave
   track identity and completeness unresolved. Divide long audio into
   contiguous windows and retain each window's offset.
5. Map audible music, voice, effects, ambience, silence and changes, separating
   observations from uncertainty. Inspect shorter windows around important
   accents, speech, cuts and the ending.

Receiving a video does not establish audio capability. A player launch,
waveform, loudness reading, transcript or separated stem alone is not proof
of soundscape perception. Transcription and separation may assist when needed;
verify consequential words and timing against listening evidence. Do not
install or invoke them automatically.

## Record evidence without changing the breakdown schema

Return a concise companion note in chat; save `audio-analysis.md` only when
saved drafts are requested. Do not add these fields to `analysis.json`, whose
local v1.0 schema remains unchanged.

| Field | Required evidence |
| --- | --- |
| Source | Original media hash and the exact audio input hash when available; distinguish an extracted file from its source |
| Selected track | Absolute source stream index, available language/title tags, selection reason, and playback or extraction mapping; use separate records for separately requested tracks |
| Stream status | Present, absent or unavailable, with probe result and measured duration of the selected track |
| Listening status | Complete, partial or unavailable; stream presence does not imply review completion |
| Reviewer | Native host, verified on-device model, named tool/model, or human |
| Capability | Actual audio interface used and any reason for fallback; no fabricated model or task IDs |
| Coverage | Ordered start/end ranges relative to the selected track's exact audio input, including its tail |
| Evidence | Analysis instructions and returned observations, or timestamped human notes |
| Sync | Selected audio/video start-time offset and mapping of audible cues to overlapping shots |
| Uncertainty | Unheard ranges, undecodable passages, unverified words and ambiguous sources |

For a complete listening record, coverage must begin at zero, end at measured
selected-track audio duration, and be gap-free and non-overlapping. A shared
container hash or equal track durations cannot establish track identity.
Context may be replayed,
but count it once in the coverage ledger. Check all boundaries together:
repeated small gaps do not become acceptable because each is individually
small. Allow only numerical rounding, not a per-window timing tolerance.
Record partial coverage as partial rather than declaring the full map verified.
These checks establish record consistency, not proof of actual listening.

Preserve historical evidence under its original reviewer and source identity.
Do not invent new provenance or repeat a completed external analysis merely
to rename its method. Never store credentials or signed URLs in notes.

## Unknowns and handoff

When no permitted reviewer can hear the soundtrack, keep sound identity and
reusable audio grammar unresolved. In the breakdown use `audio.mode:
"unverified"`, null music and dialogue, empty `sfx`, and `"unverified"` for
each unsupported shot audio description. Keep stream status `present` when
decodable audio exists but listening is unavailable.

Partial notes may support specific attributed observations; the remaining
soundtrack stays unverified. An untimed transcript supplies words, not their
timing or the surrounding music and effects. Never infer that a visible
event caused a sound just because it coincides with an accent.

Continue visual analysis without inventing sound or treating silence as a
default. Carry only verified reusable sound grammar into a recipe. Audio
generation and exact-source audio reuse remain separate authorized operations.
