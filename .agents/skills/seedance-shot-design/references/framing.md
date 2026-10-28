# Framing

Focused reference for `seedance-shot-design`. Read [the entrypoint](../SKILL.md)
for the procedure and the variety rules, and [shot plan
format](shot-plan-format.md) for the `framing` field.

- [Source and status](#source-and-status)
- [What framing decides](#what-framing-decides)
- [Framing types](#framing-types)
- [Choosing a framing](#choosing-a-framing)
- [Framing in the plan](#framing-in-the-plan)
- [Failure shapes](#failure-shapes)

## Source and status

The framing definitions follow the StudioBinder article "Camera Framing
Techniques" (SC Lannom, 2025-05-20, accessed 2026-10-17:
https://www.studiobinder.com/blog/types-of-camera-shot-frames-in-film/): single
and dirty single, two-shot, three-shot, over-the-shoulder, over-the-hip, point
of view and insert, with size, relationships and balance as the factors. The
group shot, the balance reading, the "Use when" column, the mapping to plan
fields, the variety rule and the wording notes are this workspace's own craft
heuristics. None is a verified Seedance control: the
model's official vocabulary names shot sizes, `low angle`, `overhead view` and
`first-person view`, and the other terms below are common film language that the
model may or may not honour. Check framing in a 480p draft before relying on it
in a final render.

## What framing decides

Framing is the placement and position of subjects in the frame, not merely where
the camera points. Three decisions carry it:

| Decision | Meaning | Plan field |
| --- | --- | --- |
| Size | Scale controls readable detail and the subject's relationship to the surroundings | `size` |
| Relationship | Several featured subjects in one frame are read as related (romantic, contentious and so on) | `framing`, `featured` |
| Balance | A balanced frame holds elements on both the left and right sides; reading an unbalanced frame as tension or isolation is a workspace heuristic | `composition` |

A subject is *featured* when the shot is about it: in focus, in the plane the
viewer reads. A foreground shoulder that only gives perspective is not featured.

## Framing types

`featured` counts the subjects the shot is about. Size is chosen independently of
the framing type.

| Framing | Featured | Job | Use when | Wording notes |
| --- | --- | --- | --- | --- |
| Single | 1 | Isolate one subject's face, body or reaction | A performance beat needs one readable face; any size works | Say that only the subject is in frame |
| Dirty single (over-the-shoulder single) | 1 | Keep a relationship alive while showing one person | A dialogue or confrontation where the listener's presence must stay felt | Name the foreground character's side of frame and keep that character soft and unfeatured |
| Two-shot | 2 | Let a performance play out in one take; show two people as related | Comedy timing, intimacy, a pair reacting together, a release after singles | Name who is screen-left and screen-right |
| Three-shot | 3 | Show a trio without paying for three singles | Adventure, family, any small group | Name the left-to-right order |
| Group shot (workspace addition) | 4 or more | Place an ensemble in one space | Establishing a crowd, a family table, a team | Name the grouping and the front or center subject |
| Over-the-shoulder (OTS) | 1 featured, 1 foreground | Orient the scene and connect two characters emotionally; it echoes what one of them sees | Conversation scenes | The foreground shoulder and back of the head sit soft at one side of frame |
| Over-the-hip (OTH) | 1 featured, 1 foreground | Like OTS, but a hip in the foreground; when one stands and the other sits or kneels, the uneven terrain often suggests a power imbalance | Interrogation, a child and an adult, a patient and a doctor | Describe the foreground hip and hand as soft and the featured subject as sharp, at a lower or higher level than the foreground character |
| Point of view (POV) | 0 or more | Show exactly what a character, or an object such as a bullet or a rolling ball, sees | A reveal that the viewer must read as the character's discovery | No part of the looker is visible except hands or limbs they would see |
| Insert | 0 | Direct attention to a detail, or show the viewer something the characters miss (dramatic irony) | A prop, a screen, a hand, a note, an environmental clue | The detail fills the frame; add a face only when the beat needs it |

Notes on the types:

- Name screen positions as frame-left and frame-right. Bare side wording can
  confuse anatomy with screen position, so name a hand or shoulder by both
  ("her right hand, frame-left" for a front-facing pose). Reassess frame side
  after a turn or cut.
- A single can be framed at any size. Only the count of featured subjects makes
  it a single.
- A dirty single technically has two people in the frame. It remains a single
  because only one is featured.
- A look, POV, reaction sequence can clarify viewpoint ownership and response.
  A standalone POV is also valid when its owner and intended evidence are clear;
  the sequence is an optional technique, not required coverage.
- An insert is only as useful as how it presents the information. Choose the
  detail, its size and its move for what the viewer must learn, and keep it to
  props and details the canon approves (the prop threshold applies).

## Choosing a framing

Decide the framing from the beat, then confirm the size.

| Beat | Framing | Why |
| --- | --- | --- |
| One character's private reaction | Single, close-up | Isolation and readable cues |
| Confrontation, one side dominates | Dirty single on the weaker side; over-the-hip instead when their heights differ | The pressure stays in frame |
| Two people playing a joke or an intimate moment | Two-shot, held | The timing needs both in the same take |
| A small group reacts together | Three-shot | Avoids three equal singles |
| A character discovers something | Looker, POV, reaction | The viewer shares the discovery |
| A detail the characters cannot see | Insert | Dramatic irony |
| Orienting a new space with its people | Group shot or wide | Places everyone |

Choose size for the evidence and spatial relationship the beat needs. A small
subject in a wide can carry the scene through isolation or sustained attention;
importance does not require a close-up.

## Framing in the plan

- Every shot in a scene with two or more characters carries a `framing` value
  and its `featured` subjects. Other scenes may omit it.
- Framing type is checked by V10 for readable relationships, not a variety
  score. A single and a two-shot may serve different attention even with
  unchanged size, angle, move and key side. Preserve physical `angle`,
  `viewpoint` and `framing` independently:
  a low-angle OTS remains low, and an overhead POV remains overhead. Derive
  the single V1/V2 comparison class per [field rules](shot-plan-format.md#field-rules)
  without overwriting these directions or counting framing a second time.
- Preserve standalone POVs without an exception record. If ownership or a
  required response is unreadable, clarify the owner or propose looker/reaction
  coverage within the requested scope; do not silently add shots.
- Use an unbalanced frame on purpose and record it in `composition`.

## Failure shapes

None of these framings is inherently flat. Apply a repair only when the
supplied intent or readable evidence is lost, not to meet a coverage quota.

| Shape | Why it reads as flat or confusing | Repair |
| --- | --- | --- |
| Clean singles lose a relationship the brief needs visible | Partner responses are omitted | Retain the needed response in singles or propose shared coverage; clean singles alone are not a defect |
| A two-shot where one subject faces away and is not featured | It reads as a dirty single with a dead foreground | Name the intended framing and soften the foreground subject |
| POV ownership or a required response is unclear | The intended evidence is missing | Name the owner or propose looker/reaction coverage within locks; a standalone POV is not itself a defect |
| Three singles omit a required simultaneous trio response | The shared timing is lost | Consider a three-shot; retain singles when isolation or separate reactions serve the brief |
| Foreground framing hides a required response | The intended relationship is unreadable | Adjust framing within locks; an OTH does not require inventing a height difference or power imbalance |
| A critical cue is unreadable in the wide | Its scale or occlusion hides the intended evidence | Use readable body or spatial cues within locks; a sustained wide can deliberately show isolation |
