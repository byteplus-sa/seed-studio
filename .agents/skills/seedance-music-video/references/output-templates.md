# Output Templates

Focused reference for `seedance-music-video`. Read [the entrypoint](../SKILL.md) for
mode selection and caller responsibilities.

- [Output formats](#output-formats)

## Output formats

Adapt the fields to the brief. Custom treatments, coherent hybrids and planned
section transitions do not need recipe labels. Summaries are optional; omit
redundant fields for scoped edits. Use only the shots or stages needed, with
no numeric shot-duration floor. Preserve requested timing; use assembly for
frame-exact cuts when authorized, and surface conflicts with locked workflows.

### Music-video block

Use when the user only wants the directing layer:

```text
[Music-Video Format]
<Format name, direct or indirect address, and performance-to-atmosphere ratio.>

[Song Map]
Section 1 (<verified time range or event cue>): <visual assignment, energy, end state>.
Section 2 (<verified time range or event cue>): <visual assignment, energy, end state>.
Final Section (<verified time range or event cue>): <closing assignment and final visible state>.

[Beat & Cut Contract]
<Which audio events the cuts and camera land on; cut density per section.>

[Audio Treatment]
<Audio intent: native brackets or silent picture for original-master assembly.
When timing conditioning is needed, use verified supported @Audio N or an
optional, selected black-sync @Video N carrier; leave unverified support open.
Record current-song permissions without inferring them from prior work.
For edits, @Video 1 remains the source scene.>

[Visual Treatment]
<Brief-derived palette, lighting, camera, cadence and tone; scope any transitions.>

[Treatment Summary] (optional)
<Compact continuity and transition summary; exclusions only for actual conflicts.>
```

### Full Seedance prompt

Use when the user asks for a complete prompt:

```text
[Song Timing Authority] (only with a selected, supported timing reference)
<@Audio N for supported direct song input, or @Video N for an optional
supported black-sync carrier> supplies the approved master segment.
Its vocals, pauses and accents guide pacing and requested lip sync during
designated performance shots. Render the directed scene imagery.
(For a black-sync carrier, ignore its black picture; neither route guarantees
exact mouth timing or a copied soundtrack.)
(For edits, @Video 1 is the existing scene instead; preserve its camera, cuts,
actions, duration, and mouth motion while applying the requested visual change.)

[Reference Roles] (only when references exist)
@Image 1 defines <performer>'s <appearance, wardrobe, or identity>.
@Image 2 defines <scene or venue>. Do not use <unwanted content>.

<Subject performs the primary action in <scene>.>
The visuals feature <brief-derived treatment: palette, lighting, lens, grade, look>.
Use <shot sizes, camera moves, and cuts>, with <beat contract>.
Audio: <silent picture for original-master assembly, or requested native
soundscape using brackets>. Any candidate soundtrack may differ from the master.

[Shot Plan] or [Stage Plan]
Shot 1 (<time range>): @Image <N> only — <location or subject>; <critical ordered
actions, reveals or sustained state and visible end state>; <requested shot size, angle and camera move>; <requested
lighting source and key side>.
Shot 2 (<time range>): @Image <N> only — <location or subject>; <critical ordered
actions, reveals or sustained state and visible end state>; <requested shot size, angle and camera move>; <requested
lighting source and key side>.
Final Shot (<time range>): @Image <N> only — <closing event and final visible
state>; <requested shot size, angle and camera move>; <requested lighting
source and key side>.
Scope each shot to its own references ("@Image N only") so no location or look
bleeds across a cut. Scope requested lens and pacing changes to the shot that
uses them. Omit unspecified axes; preserve the approved grade or scoped grade
transitions and stable performer identity. Each shot inherits only the shared choices it does not
explicitly change.

[Lip-Sync & Lyric Timing] (only when lip-synced vocals are requested)
In designated performance shots, <performer>'s mouth shapes align to every
syllable. Perform each assigned line in full,
in order, at its beat slot — no line skipped, shortened, mumbled, or reordered.
<X>-line timestamped timeline (<start>s–<end>s): <[X-Ys] { line }> per line.

[Maintain Consistency]
Preserve <source locks, approved identity, wardrobe, venue and exact audio>.
Keep shared choices consistent except for authorized section-specific changes.
For preservation-only edits, retain source camera, cuts, actions and mouth motion.

[Treatment Summary] (optional)
<Compact treatment, beat relationship, continuity and intended transitions.>
```

Return the prompt directly. Do not add production workflow, tool selection,
asset management, approval gates, or generation instructions unless the user
explicitly asks for them.
