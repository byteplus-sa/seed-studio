# Frame Break Acceptance Check

Focused reference for `seedance-frame-break`. Read it when judging a returned
take. This workspace ships no pixel-measurement tooling, so the check is made by
eye from frames: the user runs it, or the agent runs it when it can inspect the
take. Judge bar motion, break-out timing, limb continuity and the camera from
frames, and treat a video-understanding model's summary as secondary evidence
only (observed upstream: it reported no overlap and a moving camera on clips
whose frames showed overlap and a locked camera).

- [Procedure](#procedure)
- [Frame extraction for inspection](#frame-extraction-for-inspection)
- [Hard gates](#hard-gates)
- [Soft gates](#soft-gates)
- [Telling bar motion from a subject over a bar](#telling-bar-motion-from-a-subject-over-a-bar)
- [Break-out check](#break-out-check)
- [Limits](#limits)

## Procedure

1. Watch the take once at full speed with sound, as a viewer would.
2. For every stage of the prompt, step through that stage's time window at about
   12 fps and read every frame in order. This step is mandatory: a sudden scale
   jump or limb swap inside a stage is found only this way. Sparse sampling (a
   frame every 0.5 s, or an 8 fps scan) did not flag the observed bar-edge
   failure and would hide a one-second limb pop-in.
3. Inspect the frames at every overlap moment and at each stage End state, and
   inspect the backdrop in several frames for lettering, logos, glow or flare.
4. Listen to the audio.
5. Apply the gates. A take that fails a hard gate is not selectable. Among takes
   that pass, rank by the soft gates; plan a few takes and pick the cleanest.
6. The user records the decision. If a hard gate fails, write a revised prompt
   from [failure modes](failure-modes.md) and keep the original as the earlier
   version. Do not retouch a take; regenerate from a revised prompt.

## Frame extraction for inspection

A video editor or player with frame stepping is enough for the user. When the
agent inspects a take it cannot watch, local `ffmpeg` frame extraction is
permitted as read-only analysis: the output is scratch under
`projects/<project>/frames/`, never a deliverable, and never a transcode or edit.
Never claim to have watched footage you could not access.

```bash
mkdir -p projects/<project>/frames
ffmpeg -ss 3 -t 3 -i take.mp4 -vf "fps=12,scale=320:-1,tile=6x6" -frames:v 1 projects/<project>/frames/stage2_sheet.png
```

Replace `-ss 3 -t 3` with the stage's start and length in seconds. At 12 fps a
3 s window gives 36 tiles, which a 6x6 grid holds. The tiles are unlabelled and
run left to right, top to bottom, one every 1/12 s from the window start. For a
single frame at full size, use `-ss <seconds> -i take.mp4 -frames:v 1 frame.png`.

## Hard gates

| Gate | Evidence |
| --- | --- |
| Bars do not move: no black growing into the window, no tilt, no curved bow, no whole-edge jump, and no bar sliding toward the frame edge while the subject is away from it. A subject covering a bar is never a violation | Stage frames at 12 fps, bar edges compared frame to frame; see below |
| Bars are present, solid black, flat and unmarked at the top and bottom throughout | Frames |
| The subject starts completely inside the window and break-outs are intermittent events, not a state | First frames and the break-out check below |
| The subject is drawn on top, never clipped or hidden behind a bar at a break-out | Frames at every overlap moment and each peak |
| Every break-out the brief requires occurs; by default at least one on each bar. A clip with no overlap at all is the effect-absent case | Stage frames |
| No sudden scale jump or limb swap inside a stage; the limb that arrives at the lens is the limb that crosses | Every frame of each stage window at 12 fps, read in order |
| The camera is locked: background features do not pan, zoom or shift | Compare fixed background features across frames |
| No on-screen text, logos, stray lettering or watermarks, including on background objects | Frames |
| Identity matches the approved reference, including soles, markings and colours; one subject only (one product, never a pair, for a product hero) | Frames against the reference |
| No unrequested held props, hands or people (product hero: none) | Frames |

## Soft gates

| Gate | Target | Evidence |
| --- | --- | --- |
| Bar thickness | Near 12 percent of frame height, about 130 px on a 1920x1080 frame; upstream takes ran 9.4 to 18.9 percent, and 17 to 21 percent in a rejected take (observed) | Measure the bar height in an image viewer and divide by the frame height |
| Top and bottom match | Within about 1 point of frame height, about 11 px on 1080p | Same measurement |
| Break-out moments | Drawn subject 3 to 5, photoreal 1 to 3 (observed) | Count the separate overlap moments |
| Backdrop | Calm, darker than the subject, no bar-like objects | Frames |
| Timing | End states within about 0.5 s of the stage budget; timestamps are allocations | Frames |
| Unrequested effects | No glow arcs or flare around near-lens parts | Frames |
| Audio | Requested sound arc; no music when none was asked (effects-only may still add light music or a chime) | Listening |

## Telling bar motion from a subject over a bar

Both change what is visible at the bar's inner edge, so separate them by
direction and shape. Compare the edge at the far left and far right of the frame,
where the subject rarely reaches, with the centre, and compare the frames just
before and after any suspect moment.

| What you see | Reading |
| --- | --- |
| A limb, hem or boot sits over the bar and the straight edge is back at the same height once it withdraws | Overlap: the intended effect, not bar motion |
| The edge at both far ends moves toward the frame edge together, with no subject near either end | Bar motion: the bar is opening. Fail the take; the exposed picture is not a break-out |
| The black grows into the window: the bar gets thicker, bows into the window as a smooth bar-shaped curve, or the whole edge jumps for a few frames | Bar motion. Fail the take |
| The edge is level in one frame and tilted or bowed in another | Bar motion. Fail the take |
| The edge is tilted by the same amount in every frame | A constant tilt is not motion; note it as a soft-gate flaw and ask for a cleaner take |
| A dark costume, robe or shorts merges with the bar so the bar looks thicker for a moment | Ambiguous: dark clothing against black cannot be separated from a thicker bar by eye alone. Check the far ends and the frames either side; if it is still unclear, treat it as needing another take |
| A flare, glow or light streak reaches a bar | An unrequested effect (soft gate), not bar motion |

Bar-edge distortion appeared when a limb or head came very close to the lens, so
look hardest at the frames of each near-lens peak.

## Break-out check

A take whose bars are perfectly static can still fail if the subject starts over
a bar or stays over one for most of the clip: it reads as standing outside the
frame, not as a frame break.

- **Starts inside**: in the first quarter second, nothing of the subject covers
  either bar. A subject over a bar at the first frame fails.
- **Intermittent**: the subject is over a bar for part of the clip, not most of
  it. Upstream, accepted takes overlapped a bar in about 15 to 65 percent of
  frames and a take rejected for standing outside the window overlapped in about
  80 percent. Treat more than about 70 percent as a fail and 60 to 80 percent as
  a judgement call to settle by reading the frames. This is a small-sample
  calibration, not a proven default.
- **Absent**: a clip with no overlap at any frame is the effect-absent case and
  fails the required break-outs gate.

## Limits

- A dark subject or costume over a black bar is easy to miss; read the frames
  rather than trusting a glance at the thumbnail.
- Glow, flare or backdrop light inside a bar band can look like a break-out.
- Limb continuity and the camera lock are judged only by reading the stage
  frames in order.
- The tolerances above are small-sample guidance from upstream takes, not a
  verified standard.
