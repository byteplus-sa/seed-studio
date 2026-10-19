# Audio Evidence

Use when the requested breakdown depends on source sound. Adapted from
[upstream PR #47](https://github.com/byteplus-sa/ark-director/pull/47) at
`391d5c67718c9c8b0606368ee4ad552fea79678b`. This is an analysis checklist,
not a generation step or a bundled provider integration.

## Establish access and perception separately

1. Probe the original media with available `ffprobe`. Record audio stream
   presence, duration, start time, channels and sample rate. Use `absent` only
   after a successful probe shows no audio stream. An inaccessible or
   undecodable stream is `unavailable`, not silent.
2. Prefer actual native audio input or a verified on-device audio model.
   If unavailable, the caller may use a permitted audio-understanding tool,
   or obtain documented human listening notes. Record which route heard
   the audio; never relabel tool output or human notes as native listening.
3. Check privacy, budget and explicit offline constraints before any remote
   analysis. A local command can invoke a remote model; it does not establish
   on-device inference. Do not require provider setup for capable native
   analysis, or require local tools when a permitted capable route exists.
4. Cover the whole soundtrack, including any tail after the picture. If needed,
   have the caller prepare lossless audio without changing the source. Divide
   long audio into contiguous windows and retain each window's offset.
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
| Stream status | Present, absent or unavailable, with probe result and measured duration |
| Listening status | Complete, partial or unavailable; stream presence does not imply review completion |
| Reviewer | Native host, verified on-device model, named tool/model, or human |
| Capability | Actual audio interface used and any reason for fallback; no fabricated model or task IDs |
| Coverage | Ordered start/end ranges relative to the exact audio input, including its tail |
| Evidence | Analysis instructions and returned observations, or timestamped human notes |
| Sync | Audio/video start-time offset and mapping of audible cues to overlapping shots |
| Uncertainty | Unheard ranges, undecodable passages, unverified words and ambiguous sources |

For a complete listening record, coverage must begin at zero, end at measured
audio duration, and be gap-free and non-overlapping. Context may be replayed,
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
