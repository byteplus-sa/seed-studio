# Voice reference

Seedance 2.5 accepts up to 10 audio refs, ≤30s combined. A single clean 8–15s
clip of the presenter is enough to carry timbre, accent and pacing.

## Source the voice

Use a clean recording of the presenter's own voice, supplied by the user. If the
only source is a video with music, a second speaker or heavy room noise, ask the
user for an isolated voice track, from a voice-separation step they run or a
cleaner recording. Do not substitute a different voice.

## Cut the clip

Find natural pauses:

```bash
ffmpeg -i voice-source.wav -af silencedetect=n=-40dB:d=0.25 -f null - 2>&1 | grep silence_
```

Choose `START_S` and `DURATION_S` from the inspected recording's pause
boundaries. Set `FADE_START_S` to the excerpt duration minus the chosen
`FADE_DURATION_S`, without fading a spoken word. These are measured inputs,
not fixed timestamps from another recording. Set a new `OUTPUT_AUDIO` path.
Cut at a pause, mono 48 kHz, normalised; keep the source untouched:

```bash
ffmpeg -n -i voice-source.wav -ss "${START_S:?}" -t "${DURATION_S:?}" -ac 1 -ar 48000 \
  -af "loudnorm=I=-16:TP=-1.5:LRA=11,afade=t=out:st=${FADE_START_S:?}:d=${FADE_DURATION_S:?}" \
  "${OUTPUT_AUDIO:?}"
```

Also keep a ~15s alternate (`refs/ref_voice-timbre-long.wav`) for a retake if
resemblance is weak. Verify the cut with `ffprobe` (duration, one audio stream,
48 kHz).

## Binding

```
@Audio 1 defines <Name>'s voice timbre, accent and pacing only; do not reuse any words from @Audio 1.
```

Put the full new script in the `{}` dialogue block and state the language
("Dialogue language: <requested language and accent>").

## QA

- Transcribe the generated take and diff it against the script. No words from
  the reference clip may appear. Automatic transcription can mishear words and
  names, so listen to suspected differences before declaring a spoken error.
  Repeat the comparison on the actual final, including a promoted draft.
- Compare median pitch as a rough check. A human listen is still required, so
  say so in the handoff. A native listener judges accent and pronunciation;
  neither a transcript nor a pitch comparison establishes them.
