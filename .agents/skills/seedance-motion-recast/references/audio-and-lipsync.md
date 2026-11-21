# Audio and Lip-Sync

Focused reference for `seedance-motion-recast`. Read [the entrypoint](../SKILL.md)
for mode selection, gates and the prompt-only boundary.

- [Audio preservation](#audio-preservation)
- [Scoped sound choices](#scoped-sound-choices)
- [Speaker ownership](#speaker-ownership)
- [Preparing source audio](#preparing-source-audio)
- [Lip-sync checks](#lip-sync-checks)

## Audio preservation

Preserve generated or supplied audio unchanged by default. Satisfactory native
audio suffices without an exception or a mute/extract/mux pass. State sound
intent in the package under the
[video-to-video inputs contract](../../../contracts/video-to-video-inputs.md#audio-preservation).
Verify exact model/operation/transport support for native generation and exact
source preservation independently; one does not prove the other. Unknown
support remains unresolved, not permission to disable or replace audio.
Finalization alone does not authorize audio editing.

## Scoped sound choices

Derive these choices from the brief; only explicit authorization permits an
audio edit. No separate soundtrack is required when native sound satisfies it.

| Route | Use when | Source | Lips |
| --- | --- | --- | --- |
| **Native** | Generated sound satisfies the brief | Unchanged provider output | Inspect the actual output |
| **Original** | The recast keeps the exact source music, dialogue or ambience | Untouched source audio; scoped assembly only if needed | New mouths follow the source mouth motion |
| **New** | The brief asks for new music, SFX, ambience or voice | A Seed Audio prompt or an approved library track | No on-screen speech, or a re-voiced line |
| **Mixed** | Keep the source dialogue, replace the bed (or the reverse) | Stems the user separates, plus new audio | Kept dialogue follows the source mouth motion |
| **Re-voiced** | New words, language or voice | A Seed Audio TA2A prompt the user generates, laid over the picture | Check sync; lip-sync work is opt-in |
| **Silent** | Explicit silence | Supported silence control or scoped removal; no bed | No audible dialogue |

Voice rules:

- Keeping a real person's recorded voice, or cloning its timbre for a new
  character, requires that person's confirmed voice consent, separate from
  footage rights and image likeness. See the
  [production policy](../../../contracts/production-policy.md).
- Separate lip-sync audio is opt-in; bind `@Audio` only for a selected,
  supported role. When the user asks for it, follow the
  [audio-video alignment contract](../../../contracts/audio-video-alignment.md):
  exact dialogue in both prompts, audio duration checked before handoff, and
  both prompts updated when the audio changes.
- An explicitly requested off-screen voice overlay can avoid re-rendering
  the mouth; its availability is not permission to replace accepted sound.

## Speaker ownership

Speech windows come from your source inspection. Map each window to one named
character. A line whose speaker is removed or turned into a background extra
needs an explicit decision: cut the line, give it to a mapped character, or
keep it off-screen.

## Preparing source audio

This leaf describes preparation only when independently verified destination
requirements and explicit authorization call for it. The caller owns any
authorized execution; no routine extraction or conversion is needed:

1. Retain the full original source before making any derivative. Keep the
   original picture and sound unchanged.
   Record independent fractional picture and sound spans, source offsets,
   timestamps and the complete audio tail; a shared timeline does not imply
   equal end times. Do not trim full-take sound to the picture span.
2. For an explicitly authorized Mixed edit, describe separation only for the
   selected layers, name each layer's time range and retain the original master and
   all kept sound through its locked ending.
3. A matching excerpt is allowed only for an explicitly selected probe or
   exact authorized derivative adaptation. Record the exact authorized picture
   and sound windows and offsets separately; general probe permission does not
   authorize cutting the delivered full take. Keep the full saved audio and
   picture master intact. Any destination-required trim, pad, rounding or retiming
   needs verified requirements and explicit agreement for that separate copy.
   Without that agreement, report the delivery requirement as unresolved.
4. When needed, use a transcript as fallible timing evidence for lip-sync
   checks, not as proof of what was heard or permission for word-level surgery.

For full-take Original or retained Mixed sound, delivery keeps the entire locked
sound span, including any tail after picture ends. A backup alone does not satisfy
delivery preservation. Do not use `-shortest` to truncate a longer soundtrack.
Do not pad a shorter soundtrack or extend, freeze, trim or retime picture without
exact derivative authorization. Equal picture and sound spans need no excerpt.
These locks govern any authorized assembly, not just backup retention. If the
destination cannot preserve both spans, keep the masters unchanged and leave
combined delivery unresolved rather than silently adapting either track.
For exact-audio delivery, use compatible stream copy where possible and verify
audio payload or decoded-sample equality against the original; re-encoding is
not an exact encoded copy. Actual full listening and visible lip-sync inspection
remain separate from those technical checks.

## Lip-sync checks

Apply to any supplied output when a character speaks on screen, whether native
or explicitly assembled. Missing listening evidence remains unresolved:

- The output transcript (user-side) matches the intended lines. Kept dialogue
  matches the source; replaced or translated lines match the approved script;
  timbre references contribute no words.
- Each line comes from the mapped character's mouth, never from a removed
  subject or an extra.
- Step through close frames on plosives (p, b, m) and open vowels; mouth shapes
  land on the audible sounds.
- Measure the audio-to-mouth offset at two or three syllables. An offset that
  grows across the clip suggests a duration mismatch between picture and audio.
- Listen in full. Loudness readings and waveforms do not replace listening.
- Report visible drift and offer scoped options. Re-voicing, splicing or a new
  take requires explicit authorization; no repair runs automatically.
