# Shot plan format

Focused reference for `seedance-shot-design`. Read [the entrypoint](../SKILL.md)
for the procedure and the variety rules.

- [Where the plan lives](#where-the-plan-lives)
- [The plan record](#the-plan-record)
- [Field rules](#field-rules)
- [Carrying the plan into the prompt](#carrying-the-plan-into-the-prompt)

## Where the plan lives

Return the plan in chat by default. Save it only when explicitly requested,
under the requested project's prompt draft or brief. Existing user-confirmed
axes remain inputs; proposed axes stay proposals. No production-stage record
or review gate is required. Mark uncertain location or lighting facts as draft
and revalidate them when the user supplies the missing reference.

## The plan record

The example is a 12-second family-drama kitchen scene at standard energy with
full shot planning requested. For a narrower request, omit unrequested axes
and apply only their relevant variety rules.

```yaml
shot_plan:
  scene: scene-02
  status: draft
  energy: standard
  axis_carry: confirmed project axes (low camera for the child, slow motivated
    moves) appear in shots c (low angle) and a, b, d (slow moves)
  sources:
    - id: window
      position: kitchen window on the left wall, screen-left when the camera
        faces the front door; low late-afternoon sun
      switched_on_by: always on
    - id: door
      position: front door at screen-right; daylight from outside
      switched_on_by: the door opens at about 5 s
  shots:
    - id: s02_sh010_a
      duration_s: 3.0
      job: establish
      size: wide
      framing: single
      featured: [mother]
      angle: high
      angle_reason: show the mother and room; the visitors remain outside the closed door
      move: slow crane down from ceiling height to table height, left to right
      move_reason: lowers the viewer into the room as the mother crosses it
      lens_intent: deep focus; table and closed door both sharp
      light: {source: window, key_side: camera-left, quality: low sun, long soft shadows across the table}
      contrast_with_previous: n/a
    - id: s02_sh010_b
      duration_s: 2.5
      job: reveal
      size: medium close-up
      framing: insert
      featured: []
      angle: eye level
      move: slow push-in on the door handle, ending on her hand as the door opens
      move_reason: moves the viewer to the point of contact
      lens_intent: shallow depth of field; hand sharp, doorway soft
      light: {source: window, key_side: camera-left, quality: same sun, her face half in shade}
      contrast_with_previous: size family, angle class and move change; the light is unchanged on purpose
    - id: s02_sh010_c
      duration_s: 3.5
      turn: true
      job: emphasize
      size: close-up
      framing: single
      featured: [boy]
      angle: low
      angle_reason: the boy's sudden appearance at adult hip height gets presence
      move: static hold, no movement
      static_reason: contrast_hold
      lens_intent: the boy's face sharp against a soft doorway
      light: {source: door, key_side: behind the subject, quality: contre-jour halo on his hair with the face kept readable by window fill}
      contrast_with_previous: size family, angle class, move and key side all change
    - id: s02_sh010_d
      duration_s: 3.0
      job: release
      size: medium
      framing: two-shot
      featured: [mother, boy]
      angle: eye level
      move: slow drift right, ending on her smile with the boy at her side
      move_reason: releases the tension by sliding to the mother's reaction
      lens_intent: natural depth, mother and boy sharp
      light: {source: window, key_side: camera-left, quality: soft sun with a warm rim from the open door}
      contrast_with_previous: size family, angle class and move change
```

## Field rules

| Field | Rule |
| --- | --- |
| `status` | `draft` until the scene's locations are approved, then `ready` after revalidation |
| `energy` | restrained, standard or kinetic |
| `axis_carry` | Where each confirmed project axis appears (camera, lens, lighting, pacing, energy), or the scene override and its reason |
| `sources` | Every light source the scene uses, with a fixed world position and the event that switches it on |
| `cues` | Optional, per source. Each cue has `at_s` (scene time), `change` (`on`, `off`, `dim` or `flicker`), `trigger` (the visible or story event) and, when it lands inside a shot, that shot's `id`. A shot's `light` describes the state at its start and names any cue inside it |
| `duration_s` | Shot length from supplied speech, listening, action and rhythm; equal lengths are valid |
| `turn` | Optional `true` for a supplied turn; omit for sustained or observational scenes |
| `job` | One of establish, reveal, emphasize, connect, escalate, hold, release |
| `size` | Extreme wide, wide, medium, medium close-up, close-up, extreme close-up or insert |
| `framing` | Single, dirty single, two-shot, three-shot, group, over-the-shoulder, over-the-hip, point of view or insert, per [framing](framing.md). Required in a scene with two or more characters |
| `featured` | The subjects the shot is about, with screen sides when it matters; empty for an insert or an unpeopled point of view |
| `composition` | Optional. Balanced or deliberately unbalanced (isolation, tension), with the reason when unbalanced |
| `angle` | Physical camera elevation or tilt: eye level, low, high, overhead or canted. Preserve supplied angles independently of framing and viewpoint; a low-angle OTS remains low |
| `viewpoint` | Optional observer or first-person perspective, with its owner when relevant. POV framing does not erase the camera angle |
| `angle_reason` | Required for any angle other than eye level |
| `move` | The primary move with subject, start and end, or `static hold` |
| `move_reason` | What the move reveals or emphasizes |
| `static_reason` | Required with a static hold; a value from the entrypoint table |
| `lens_intent` | A visible result (sharp plane, soft background, compression), never a number alone |
| `light` | A declared `source`, the `key_side` relative to the lens, and the quality and contrast |
| `contrast_with_previous` | Which of size family, angle comparison class, move and key side change; `n/a` for the first shot |

For V1 and V2 only, derive one angle comparison class: use the actual
non-eye-level angle first; otherwise use first-person for POV or
over-the-shoulder for OTS/OTH/dirty-single framing, else eye level. Keep
`angle`, `viewpoint` and `framing` unchanged in the plan and prompt. This
comparison class is a craft scoring aid, never a replacement camera direction;
count it once rather than counting framing again. A supplied legacy
`angle: first-person` or `angle: over-the-shoulder` describes viewpoint or
framing; retain any separately supplied elevation or tilt when normalizing it.

A cue that lands inside a shot is written once on the source and named on the
shot's `light` line:

```yaml
sources:
  - id: hall-sconces
    position: wall sconces along both sides of the library, behind the subject
    switched_on_by: always on
    cues:
      - {at_s: 6.5, change: off, trigger: the Voice takes hold, shot: s01_sh030}
shots:
  - id: s01_sh030
    light: {source: hall-sconces, key_side: behind the subject, quality: dim rim
      that goes out at about 2 s into the shot, leaving his face just above black}
```

In Seedance 2.5 drafts a stated cue time is honoured closely (2 s asked, 2 s
delivered) and an `off` cue switches the source instantly. When a fade is
wanted, write it into the light line ("fades out over about one second"). An
untimed "partway through" switch lands at an unplanned moment.

A plan contains only requested axes, supplied durations and performance
readability notes. A turn, uneven timing or neighboring contrast is not
required when it conflicts with the approved rhythm. Supplied beat IDs connect
critical intent, listening and responses to the shots without a new schema.

## Carrying the plan into the prompt

The prompt author copies each shot's camera and light facts into the shot line
without softening them. The per-shot prompt block, the one-take variant and the
dialogue timing rules belong to the Seedance 2.5 prompt skill's shot-staging
reference. If the prompt cannot hold a planned fact, the author reports the
conflict to the plan owner instead of dropping it. A reviewer compares the plan
to the prompt, and the take review compares the plan to the footage.
