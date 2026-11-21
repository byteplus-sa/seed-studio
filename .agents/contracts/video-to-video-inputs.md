# Video-to-Video Inputs

This contract covers identity references, source footage and audio preservation
for Seedance video-to-video prompts: Motion Transfer
(`seedance-motion-recast`), Object Swap (`seedance-object-swap`) and Restyle
(`seedance-restyle`). These skills write prompts only. In prompt-only mode,
the package describes only the steps required by the selected, verified route.
The calling agent owns authorized execution under
[generation transport](generation-transport.md) and the root permissions;
this contract does not expand a leaf's prompt-only boundary.

- [Human likeness: Virtual Portrait assets](#human-likeness-virtual-portrait-assets)
- [Source footage](#source-footage)
- [Audio preservation](#audio-preservation)
- [Scoped audio changes](#scoped-audio-changes)
- [Provider rejections](#provider-rejections)

## Human likeness: Virtual Portrait assets

Classify each person in source footage and target references separately. Use
Virtual Portrait only for an invented likeness eligible for the selected
binding. For an identifiable real person, confirm likeness and performance
rights and verify a separate provider-authorized real-person route for this
account and operation. Consent alone does not establish eligibility. An
unknown identity, missing authorization or rejected asset stays unresolved.
The following registration steps apply only to eligible invented people.
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
- **Package.** Identify the verified route and binding position for each
  eligible source or target. The user handles any external registration.
  Keep actual asset identifiers and credentials out of prompts and records.
- **Prompt wording.** Refer to each asset by its binding position
  (`@Image 1`), never by asset ID. A short production label tied to that
  binding (`Mara: @Image 1 and @Image 2`) may name the character in later
  lines.

Non-identity references (products, props, locations, style frames) need no
asset library; choose views without people. When a garment or product exists
only on a model, use a flat-lay, mannequin or packshot view, or verify the appropriate identity route for that person.

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
- **Length.** Verify the exact destination's supported source length. Earlier
  4-30 s limits and under-20 s edit recommendations are not universal constraints.
  Preserve the selected span; splitting needs explicit agreement.
- **Source preparation.** Bind the original source without preprocessing when
  compatible. Any required preparation needs independently verified exact model,
  operation and transport constraints plus explicit authorization for a separate
  copy. Record the reason, change, original hashes and independent picture/audio
  spans and offsets. Unknown requirements stay unresolved.
  - *Reference routes* use currently supported duration increments. Do not
    round or trim the source silently; explain any required timeline
    adaptation and obtain approval for the specific span.
  - *Edit routes* (Object Swap, Restyle) preserve the selected source timeline.
    Check the current destination's documented frame-count constraints before
    preprocessing. Do not pad or trim to an empirical `8n+1` pattern from a
    previous run. If the current route requires it, disclose the timing change
    and obtain authorization; measure output duration rather than promising
    exact frame-count preservation.
- **Source video identity.** Check every visible person against the identity
  rules above, including performers who will later be replaced. For mixed
  casts, verify that the destination accepts the full source and all roles.
  A registered target image does not authorize a source video. An unresolved
  or rejected source stays unbound. For footage without people, use the
  ordinary source input when the selected operation supports it.

## Audio preservation

Preserve generated or supplied audio unchanged by default. Native audio is
sufficient when it satisfies the brief, without an exception or mandatory
mute/extract/mux sequence. Finalization alone does not authorize audio editing.
Do not disable native sound solely to build a bed in post.

Source-audio passthrough and native generation are different capabilities and
are not guaranteed for every model or operation. Verify the selected exact
model, operation, transport and reference roles independently before choosing
controls. If an exact-source lock cannot be met, report it as unresolved;
generated similar sound is not an exact copy. A verified input restriction may
justify an adapted source only with explicit authorization for that separate
copy, never a routine preprocessing step or a promise of preservation.

State the brief's sound intent in the package: unchanged native sound, exact
source/master, explicit silence, or a specified audio edit. Bind an `@Audio`
reference only when its role is selected and supported. Keep separate lip-sync
audio opt-in under [audio-video alignment](audio-video-alignment.md).

## Scoped audio changes

Only an explicit request or approval selects these capabilities. Existing
acceptable audio requires none of them.

| Route | Use when | Method |
| --- | --- | --- |
| **Original** | Exact source sound is required | Retain it unchanged; if separate assembly is necessary, disclose the method and use compatible stream copy within the authorized scope |
| **New** | New music, SFX, ambience or voice is requested | Use supported native generation or an explicitly selected separate track |
| **Mixed** | Only named sound layers may change | Describe the authorized separation/mix; preserve all locked layers |
| **Re-voiced** | New words or voice are requested | Scope the new performance and verify voice consent and lip-sync support |
| **Silent** | The user requests silence | Use a supported silent-output control or scoped removal; never add a bed |

For authorized assembly, preserve source masters and use compatible stream copy
where possible. Disclose necessary transcoding; obtain approval for any changed
sound or timeline. Do not pad, fade, normalize or truncate audio automatically.
Do not use `-shortest` to remove a longer audio tail or force shorter sound to
picture length. If the destination cannot preserve independent spans, retain
both masters and leave combined delivery unresolved.

Before assembling, measure the selected picture and audio streams on their
presentation timeline, including start offsets and the last displayed frame or
audible sample. Agree on the container and independent end times first. If the
approved delivery cannot represent them, pause before muxing.

For a single approved picture stream starting at zero in `picture.mov` and a
single exact PCM recording starting at the same zero in `recording.wav`, this
authorized MOV example retains both independent ends when their codecs and the
destination player support them. A different start offset, multiple intended
tracks, or an incompatible container requires separate mapping and verification.

```bash
ffmpeg -n -i picture.mov -i recording.wav -map 0:v:0 -map 1:a:0 -c copy delivery.mov
```

Checks to hand over with the package:

- Measure decoded frame timestamps and duration against the approved source
  or requested timeline. Preserve independent audio spans and tails. Report
  differences and request a scoped decision;
  do not assume a previous run's frame-count behavior holds.
- Output frame rate may differ from the source. Audio aligns by time; check two
  or three sync points (hits, claps, plosives) by playback.
- When a person speaks on screen, the mouth follows the source mouth motion.
  Check plosives and open vowels. Report visible drift; a re-voice, word splice
  or new take needs separate explicit authorization.
- Read-only stream checks and full decode do not replace actual listening.
  If listening is unavailable, mark sound quality unresolved, not repaired.
- For exact sound, compare the full decoded samples in the same lossless
  representation, channel order and sample rate. Verify stream start, sample
  count, end time and offset relative to picture as separate timing checks.
  Stream-copy packet equality alone cannot demonstrate sync. Listen through
  the final word or cue and inspect visible mouth timing.
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
