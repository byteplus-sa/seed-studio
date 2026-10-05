# Video-to-Video Inputs

This contract covers identity references, source footage, the muted source
master and post audio for Seedance video-to-video prompts: Motion Transfer
(`seedance-motion-recast`), Object Swap (`seedance-object-swap`) and Restyle
(`seedance-restyle`). These skills write prompts only. In prompt-only mode,
every upload, asset registration, trim, submission and mux below is a step the
user takes in their own tools, and the prompt package states what each step
needs. When the user explicitly asks to generate,
[generation transport](generation-transport.md) governs submission; asset
registration, trimming and muxing stay user-side.

- [Human likeness: Virtual Portrait assets](#human-likeness-virtual-portrait-assets)
- [Source footage](#source-footage)
- [Muted source master](#muted-source-master)
- [Post audio](#post-audio)
- [Provider rejections](#provider-rejections)

## Human likeness: Virtual Portrait assets

When a video-to-video job involves a realistic human likeness, recommend that
the user upload those assets to the BytePlus private Virtual Portrait library
and bind them as `asset://<asset_id>` references. This covers performers in
the source footage, target characters, and AI avatars or other photoreal
invented people. Seedance rejects realistic faces in raw image and video
inputs (see [Provider rejections](#provider-rejections)).

- **Where.** In the ModelArk console: Model Playground > My assets > Virtual
  Portrait. The library is isolated by project, and an asset works only with an
  endpoint in the same project. The account needs Advanced Creation Rights, and
  the user signs the console authorization when creating the first group. The
  user waits until the asset is active before binding it.
- **One subject per group.** Never mix two characters in one asset group. A
  medium-specific design, such as a clay or anime version of a character, is
  its own subject (`"Mara (claymation)"`).
- **Sources.** One image per view, never a collage or turnaround strip. The
  best set is a front-facing close-up plus a full-body view in portrait
  orientation.
- **Order of work.** Seedream does not accept `asset://` inputs, so design and
  approve the sheet first, then upload the approved views.
- **Review outcome.** BytePlus reviews every upload, and its documentation says
  a Virtual Portrait asset must not resemble any real person's likeness, so an
  upload of a real, identifiable person may be rejected. When an asset is
  rejected, report the outcome the user shares and follow the
  [production policy](production-policy.md); never alter the asset to get it
  accepted. For a real performer whose likeness is rejected, BytePlus's
  separate authorized real-person asset route (invite-only, verified with the
  person's own liveness check) applies; it sits outside this workspace.
- **Package.** List each identity reference with its binding position and mark
  it as a Virtual Portrait asset for the user to upload. The agent never
  registers assets, never asks for credentials, and never writes asset IDs or
  `asset://` URIs into prompts, packages or saved files.
- **Prompt wording.** Refer to each asset by its binding position
  (`@Image 1`), never by asset ID. A short production label tied to that
  binding (`Mara: @Image 1 and @Image 2`) may name the character in later
  lines.

Non-identity references (products, props, locations, style frames) need no
asset library; choose views without people. When a garment or product exists
only on a model, use a flat-lay, mannequin or packshot view, or upload that
model as a Virtual Portrait.

Rights and consent for real people still follow the
[production policy](production-policy.md); the asset route does not replace
them.

## Source footage

- **Rights.** The user confirms rights that cover the footage and the people
  visible in it, with its scope (for example, private test or client
  delivery). Unknown rights stop the work.
- **Inspection.** Note duration, frame rate, aspect ratio, resolution, audio
  streams and cut times before writing a prompt. Watch the clip with an agent
  video pass when the client can; otherwise read local `ffprobe` output and
  `ffmpeg` frame extractions as images. Never claim to have watched footage
  you could not access.
- **Length.** Sources run 4–30 s. Edit routes (Object Swap, Restyle) are most
  stable under 20 s; split longer takes into shots.
- **Trim by route.** The package tells the user which span to trim to, and the
  muted master and saved audio come from that trimmed file so all three share
  one timeline.
  - *Reference routes* set `duration`, which takes whole seconds. Trim to a
    whole-second span.
  - *Edit routes* (Object Swap, Restyle) lock duration to the source. The
    official Seedance 2.5 guide says the output comes back up to about 0.3 s
    shorter unless the input frame count is 8n+1 (for example 121 frames at
    24 fps, 5.04 s). Ask for an 8n+1 frame trim. Upstream probes confirmed it:
    a 120-frame input returned 113 frames, and a 121-frame input returned
    exactly 121 frames.
- **Source videos that show a person are `asset://` videos.** Seedance rejects
  a realistic person in a video input, including an invented person in a
  text-generated clip, with `InputVideoSensitiveContentDetected.PrivacyInformation`
  before a task is created, and image assets of that person do not clear it.
  Recommend that the user upload the muted master as a video asset in the
  Virtual Portrait library and bind `@Video 1` as its `asset://` URI. A source
  with no people binds as an ordinary upload.

User-side trim recipe, for the package (the agent does not run it):

```bash
ffmpeg -ss <start> -i <source>.mp4 -frames:v <8n+1> -map 0:v:0 -map 0:a:0? \
  -c:v libx264 -crf 16 -preset slow -c:a pcm_s24le <stem>_trim.mov
```

For a reference route, replace `-frames:v <8n+1>` with `-t <whole seconds>`.

## Muted source master

The user submits only a muted master, never the source with its audio, and
keeps the audio as a separate file for post.

1. The parameter block sets `generate_audio: false` and binds no `@Audio`
   input.
2. The prompt's audio block reads:

   ```text
   [Audio]
   Silent output. Sound is added in post.
   ```

3. The package names the post-audio route (below).

User-side recipe (skip the first command when the source has no audio
stream):

```bash
ffmpeg -i <source>.mp4 -map 0:a:0 -vn -c:a pcm_s24le <stem>_audio.wav
ffmpeg -i <source>.mp4 -map 0:v:0 -an -c:v copy <stem>_muted.mp4
```

Native audio generation, or a supplied `@Audio` track for opt-in lip-sync (see
the [audio-video alignment contract](audio-video-alignment.md)), is not the
default for these workflows. Use it only when the user explicitly asks for it on
a named take, write it as its own prompt block, and note the exception in the
package.

## Post audio

Pick one route per shot from the brief and state it in the package.

| Route | Use when | Method |
| --- | --- | --- |
| **Original** | Timing is preserved and the source sound stays | The user muxes the saved source audio |
| **New** | The brief asks for new music, SFX, ambience or voice | A Seed Audio prompt (`seed-audio-prompt`) or an approved library track, then mux |
| **Mixed** | Keep one layer (usually dialogue) and replace the rest | The user separates the saved audio into stems in their audio tool and mixes the kept stem with the new one |
| **Re-voiced** | New words or a new voice over the same picture | A Seed Audio TA2A prompt (`seed-audio-prompt`); lip-sync work follows the [audio-video alignment contract](audio-video-alignment.md) and is opt-in |

User-side mux recipe:

```bash
ffmpeg -i <generated>.mp4 -i <audio>.wav -map 0:v:0 -map 1:a:0 \
  -c:v copy -af apad -c:a aac -b:a 192k -shortest <final>.mp4
```

Checks to hand over with the package:

- Edit outputs land within about 0.3 s of the source length (exact for an 8n+1
  frame input); reference-route outputs match the requested whole seconds.
- Output frame rate may differ from the source. Audio aligns by time; check two
  or three sync points (hits, claps, plosives) by playback.
- When a person speaks on screen, the mouth follows the source mouth motion.
  Check plosives and open vowels. A visible drift routes to Re-voiced or to a
  new take; it is never accepted silently.
- Voice reuse or timbre cloning of a real person needs that person's confirmed
  voice consent, separate from footage rights.

## Provider rejections

A `PrivacyInformation` or other sensitive-content rejection the user reports is
evidence to diagnose. Ask for the request ID and the flagged input, and follow
the moderation rule in the [production policy](production-policy.md).

- When the flagged input is an invented or AI-generated character (an AI
  avatar included) bound as a raw image or video, recommend the Virtual
  Portrait route above and write a fresh prompt package for the new bindings.
- When the flagged input is source footage or a likeness of a real person,
  stop. Do not retry the same footage or likeness through another route to get
  past the check. Offer owned or generated source footage, or an invented
  Virtual Portrait cast, and revise only on the user's explicit decision.
- Never blur, crop, stylize, re-encode or swap inputs to get a likeness or
  footage past the check.
