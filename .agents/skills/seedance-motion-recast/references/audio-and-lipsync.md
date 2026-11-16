# Audio and Lip-Sync

Focused reference for `seedance-motion-recast`. Read [the entrypoint](../SKILL.md)
for mode selection, gates and the prompt-only boundary.

- [Silent submission](#silent-submission)
- [Post-audio routes](#post-audio-routes)
- [Speaker ownership](#speaker-ownership)
- [Preparing source audio](#preparing-source-audio)
- [Lip-sync checks](#lip-sync-checks)

## Silent submission

Every recast binds the muted master as `@Video 1`, sets
`generate_audio: false` in the parameter block and uses no `@Audio` bindings.
The prompt's audio block is always:

```text
[Audio]
Silent output. Sound is added in post.
```

The audio decision lives in the package as a post-audio route, following the
[video-to-video inputs contract](../../../contracts/video-to-video-inputs.md#post-audio).
Native audio generation is used only when the user explicitly asks for it on a
named take; note that exception in the package and write it as its own prompt
block.

## Post-audio routes

| Route | Use when | Source | Lips |
| --- | --- | --- | --- |
| **Original** | The recast keeps the source music, dialogue or ambience | Saved source audio | New mouths follow the source mouth motion |
| **New** | The brief asks for new music, SFX, ambience or voice | A Seed Audio prompt or an approved library track | No on-screen speech, or a re-voiced line |
| **Mixed** | Keep the source dialogue, replace the bed (or the reverse) | Stems the user separates, plus new audio | Kept dialogue follows the source mouth motion |
| **Re-voiced** | New words, language or voice | A Seed Audio TA2A prompt the user generates, laid over the picture | Check sync; lip-sync work is opt-in |

Voice rules:

- Keeping a real person's recorded voice, or cloning its timbre for a new
  character, requires that person's confirmed voice consent, separate from
  footage rights and image likeness. See the
  [production policy](../../../contracts/production-policy.md).
- Separate lip-sync audio is opt-in, and it is the one case where an `@Audio`
  binding is allowed: write it as its own prompt block and note the exception
  in the package. When the user asks for it, follow the
  [audio-video alignment contract](../../../contracts/audio-video-alignment.md):
  exact dialogue in both prompts, audio duration checked before handoff, and
  both prompts updated when the audio changes.
- When lips are off-screen or not the focus, a voice overlay in post avoids
  re-rendering the mouth.

## Speaker ownership

Speech windows come from your source inspection. Map each window to one named
character. A line whose speaker is removed or turned into a background extra
needs an explicit decision: cut the line, give it to a mapped character, or
keep it off-screen.

## Preparing source audio

Audio preparation happens on the user's side, in the destination workflow; this
workspace does not separate, trim, transcode, transcribe or mux media. State
these needs in the package and ask the user to prepare the files:

1. Save the full original source audio before making any derivative. Keep the
   original picture and sound unchanged and write the muted picture master.
   Record independent fractional picture and sound spans, source offsets,
   timestamps and the complete audio tail; a shared timeline does not imply
   equal end times. Do not trim full-take sound to the picture span.
2. For a Mixed route, separate voice and background with a tool of the user's
   choice, name each layer's time range and retain the original master and
   all kept sound through its locked ending.
3. A matching excerpt is allowed only for an explicitly selected probe or
   exact authorized derivative adaptation. Record the exact authorized picture
   and sound windows and offsets separately; general probe permission does not
   authorize cutting the delivered full take. Keep the full saved audio and
   muted master intact. Any destination-required trim, pad, rounding or retiming
   needs verified requirements and explicit agreement for that separate copy.
   Without that agreement, report the delivery requirement as unresolved.
4. Transcribe kept dialogue and keep the word timings as the reference for the
   lip-sync checks.

For full-take Original or retained Mixed sound, delivery keeps the entire locked
sound span, including any tail after picture ends. A backup alone does not satisfy
delivery preservation. Do not use `-shortest` to truncate a longer soundtrack.
Do not pad a shorter soundtrack or extend, freeze, trim or retime picture without
exact derivative authorization. Equal picture and sound spans need no excerpt.
These locks govern the shared trim/mux recipes for this request; their
picture-length conform is not applicable to unequal locked spans. If the
destination cannot preserve both spans, keep the masters unchanged and leave
combined delivery unresolved rather than silently adapting either track.
For exact-audio delivery, use compatible stream copy where possible and verify
audio payload or decoded-sample equality against the original; re-encoding is
not an exact encoded copy. Actual full listening and visible lip-sync inspection
remain separate from those technical checks.

## Lip-sync checks

Apply after the user muxes the post-audio route, to anything they share or
describe, when any character speaks on screen:

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
- A visible drift routes to the Re-voiced route or a new take; note the failure
  rather than accepting it.
