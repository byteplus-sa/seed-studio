# Frame extraction (analysis-only)

When a local extraction tool is available, the agent extracts frames itself
instead of asking the user for screenshots. Extraction is a **read-only
analysis step**: it produces scratch frames, never deliverables, never
references, and nothing is uploaded.

## When this mode applies

Check availability first:

```bash
command -v ffmpeg >/dev/null && command -v ffprobe >/dev/null \
  && echo "extraction available" || echo "extraction unavailable"
```

If unavailable, fall back to the user keyframe set or the external pass.

## Procedure

Run these blocks in the same Bash session. Set `VIDEO` to the selected local
source and `FRAMES_ROOT` to the current project's analysis scratch directory
(`projects/<project>/frames`). Verify that destination before creating it.
Each invocation hashes the source and allocates a fresh run directory; never
reuse a previous run for a different source or extraction attempt.

```bash
set -euo pipefail
set -C
: "${VIDEO:?Set VIDEO to the selected local source}"
: "${FRAMES_ROOT:?Set FRAMES_ROOT to the project analysis scratch directory}"
test -f "$VIDEO" && test -r "$VIDEO"
mkdir -p "$FRAMES_ROOT"
SOURCE_ID="$(shasum -a 256 < "$VIDEO" | awk '{print $1}')"
FRAMES="$(mktemp -d "$FRAMES_ROOT/source-${SOURCE_ID}.run.XXXXXX")"
printf 'source=%s\nsha256=%s\nrun=%s\n' "$VIDEO" "$SOURCE_ID" "$FRAMES" \
  > "$FRAMES/source.txt"
```

Preserve `source.txt`, probe output and detector logs with that run's frames.
Each extraction block claims its output directory with `mkdir` without `-p`;
under `set -e`, a reused directory stops the block before extraction. Keep
that guard: FFmpeg image output must not rely on `-n` alone for overwrite
protection. Use a fresh run for a retry, including after partial failure.

### 1. Probe the source

```bash
ffprobe -v error -select_streams v:0 \
  -show_entries stream=duration,duration_ts,time_base,width,height,r_frame_rate,avg_frame_rate:format=duration \
  -of json "$VIDEO" > "$FRAMES/probe.json"
```

Record the picture stream's duration, dimensions and frame-rate metadata.
Use stream duration, or duration ticks multiplied by time base, for the last
picture boundary. Container duration can include a longer audio tail. If
picture duration is unavailable, mark a container-duration fallback provisional
and verify the final picture timestamp before locking the cut list. An average
frame rate does not establish constant frame timing for variable-rate footage.

### 2. Detect shot boundaries

```bash
mkdir "$FRAMES/cuts"
ffmpeg -nostdin -n -v info -i "$VIDEO" -vf "select='gt(scene,0.3)',showinfo" \
  -fps_mode vfr "$FRAMES/cuts/cut_%04d.png" 2> "$FRAMES/scene-detection.log"
awk '/pts_time:/ { sub(/^.*pts_time:/, ""); sub(/ .*/, ""); print }' \
  "$FRAMES/scene-detection.log"
```

No detected events is a valid result, not proof that the source has no cuts.
Check the saved log if extraction fails; do not treat failure as an empty result.

Each `pts_time` is a measured detector event, initially a **candidate cut**.
Inspect a short frame strip around it: a flash or fast motion may be a false
positive, while a dissolve, whip or speed ramp may hide a real boundary.
Changing the threshold changes sensitivity, not certainty. Add confirmed
missed boundaries and remove false positives with their reasons. Use `0.0`
as the first relative boundary and the verified picture duration as the last;
record any source timestamp offset before comparing streams.

For an edit-structure remake, record confirmed boundaries and uncertainty in
the optional [measured edit ledger](measured-edit-ledger.md).

### 3. Extract per-shot frames

For each shot, set `START_S`, `MID_S` and `LAST_IN_SHOT_S` to inspected numeric
timestamps, and use a distinct shot number in the output directory:

```bash
mkdir "$FRAMES/shot01"
ffmpeg -nostdin -n -v error -ss "${START_S:?Set START_S}" -i "$VIDEO" \
  -frames:v 1 "$FRAMES/shot01/a.png"
ffmpeg -nostdin -n -v error -ss "${MID_S:?Set MID_S}" -i "$VIDEO" \
  -frames:v 1 "$FRAMES/shot01/b.png"
ffmpeg -nostdin -n -v error -ss "${LAST_IN_SHOT_S:?Set LAST_IN_SHOT_S}" -i "$VIDEO" \
  -frames:v 1 "$FRAMES/shot01/c.png"
```

The end boundary is exclusive: extracting exactly there can return the next
shot. Choose the final source frame strictly before it. For constant-rate
footage that may be one frame interval before the cut; for variable-rate
footage use actual frame timestamps rather than an average-frame-rate estimate.

### 4. Extract motion bursts

For motion-critical shots, set `DURATION_S` to the positive burst duration and
extract a short dense burst across the shot:

```bash
mkdir "$FRAMES/shot01-motion"
ffmpeg -nostdin -n -v error -ss "${START_S:?Set START_S}" -i "$VIDEO" \
  -t "${DURATION_S:?Set DURATION_S}" -vf fps=6 "$FRAMES/shot01-motion/m%02d.png"
```

Read consecutive burst frames together to observe direction, speed,
amplitude, and easing. Motion between sampled frames remains an inference —
say so when confidence is not high.

## Budget

- Read frames in small batches; keep the total working set near 30–40 images.
- Three frames per shot for the breakdown; add a 6-frame burst only for
  motion-critical shots (or all shots when the video is short).
- For long videos, analyze one scene at a time and summarize before moving on.

## Boundaries

- Frames are analysis scratch in source/run namespaces under
  `projects/<project>/frames/`. They are
  never uploaded, never listed as references, and never bound as `@Image N`
  inputs. Keep prior evidence untouched; remove only the current task's own
  disposable run when it is no longer needed. They are not deliverables.
- Extraction never uses filters, effects, transcoding, or assembly — only
  `ffprobe` inspection and plain frame extraction.
- The agent still has not *watched* the video continuously. Confirmed cut
  timestamps have measured evidence; unresolved boundaries remain estimates.
  Motion between sampled frames remains an inference, and frames provide no
  audible evidence.
- **Audio cannot be heard from frames.** Ask the user for a transcript or
  audio notes. Without them, set the analysis audio fields to explicit
  unknowns (`mode: "unknown (no audio access)"`, null music and dialogue,
  empty sfx) and flag the package audio-unverified — never guess.
