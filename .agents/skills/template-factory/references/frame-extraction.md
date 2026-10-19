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

```bash
VIDEO="<path to the user-provided video>"
FRAMES="projects/<project>/frames"
mkdir -p "$FRAMES"
```

### 1. Probe the source

```bash
ffprobe -v error -select_streams v:0 \
  -show_entries stream=duration,duration_ts,time_base,width,height,r_frame_rate,avg_frame_rate:format=duration \
  -of json "$VIDEO"
```

Record the picture stream's duration, dimensions and frame-rate metadata.
Use stream duration, or duration ticks multiplied by time base, for the last
picture boundary. Container duration can include a longer audio tail. If
picture duration is unavailable, mark a container-duration fallback provisional
and verify the final picture timestamp before locking the cut list. An average
frame rate does not establish constant frame timing for variable-rate footage.

### 2. Detect shot boundaries

```bash
ffmpeg -v info -i "$VIDEO" -vf "select='gt(scene,0.3)',showinfo" \
  -fps_mode vfr "$FRAMES/cut_%04d.png" -y 2>&1 | rg -o "pts_time:[0-9.]*"
```

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

For each shot, extract start, middle, and last-in-shot frames by timestamp:

```bash
ffmpeg -v error -ss <start_s> -i "$VIDEO" -frames:v 1 "$FRAMES/shot01_a.png" -y
ffmpeg -v error -ss <mid_s>   -i "$VIDEO" -frames:v 1 "$FRAMES/shot01_b.png" -y
ffmpeg -v error -ss <last_in_shot_s> -i "$VIDEO" -frames:v 1 "$FRAMES/shot01_c.png" -y
```

The end boundary is exclusive: extracting exactly there can return the next
shot. Choose the final source frame strictly before it. For constant-rate
footage that may be one frame interval before the cut; for variable-rate
footage use actual frame timestamps rather than an average-frame-rate estimate.

### 4. Extract motion bursts

For motion-critical shots, extract a short dense burst across the shot:

```bash
ffmpeg -v error -ss <start_s> -i "$VIDEO" -t <duration_s> -vf fps=6 \
  "$FRAMES/shot01_m%02d.png" -y
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

- Frames are analysis scratch under `projects/<project>/frames/`. They are
  never uploaded, never listed as references, and never bound as `@Image N`
  inputs. Delete them or leave them local; they are not deliverables.
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
