# Multi-Subject Mapping

Focused reference for `seedance-motion-recast`. Read [the entrypoint](../SKILL.md)
for mode selection, gates and the prompt-only boundary.

- [Source analysis](#source-analysis)
- [Descriptor rules](#descriptor-rules)
- [Dispositions](#dispositions)
- [Crowds and background extras](#crowds-and-background-extras)
- [Reference budget](#reference-budget)
- [More than eight subjects](#more-than-eight-subjects)
- [Multi-cut consistency](#multi-cut-consistency)

## Source analysis

Inspect the source yourself before writing a mapping. This workspace has no
analysis tooling to run for you:

1. Probe duration, fps, resolution, aspect ratio and audio streams when the
   file is local (`ffprobe` is permitted for read-only analysis).
2. Watch the clip with an agent video pass when the client can. When it cannot,
   extract frames with local `ffmpeg` into `projects/<project>/frames/` and read
   them as images; never claim to have watched footage you could not access.
3. Record the cuts with approximate timestamps; every person and swappable
   object per cut, with screen position, clothing and action; occlusion and
   hand-contact windows; who speaks when; any on-screen text or logos.
4. Look at at least one keyframe per cut. Confirm every descriptor against the
   pixels and count people in each cut.
5. Flag any two subjects that one descriptor could match, any uncertain count
   and any unconfirmed timestamp as an open ambiguity. Resolve each with the
   user or by further frame inspection, never by guessing. While any ambiguity
   is open, prompt writing does not start.
6. Record each decision in the package's disposition table: **Map**,
   **Remove**, **Background extra** or **Generic object**, per the next
   sections.

Never name real people from the footage, and never infer identity, age,
ethnicity or gender from appearance. Describe only what is visible.

## Descriptor rules

A descriptor picks exactly one source subject for the whole clip. Build it from
three observable parts:

| Part | Good | Weak |
| --- | --- | --- |
| Screen position | screen-left, foreground center, far right by the door | "the main one" |
| Clothing | red windbreaker, grey cap | "casual clothes" |
| Action | starts the arm wave, carries the tray, jumps the rail | "dancing" when both dance |

- Use the position where the subject first appears, and add the action that
  separates them from similar subjects.
- When two subjects wear similar clothing, lean on position and action.
- When subjects swap sides, name the start position and the crossing:
  `the skater who starts screen-right and crosses to the left at about 0:03`.
- Keep the descriptor identical in every block and every cut.
- Objects get descriptors too: `the white ceramic mug in the right-hand
  performer's hand`, with a count per cut.

## Dispositions

Every visible source subject and every swappable object gets exactly one.

| Disposition | Use when | Mapping line |
| --- | --- | --- |
| **Map** | The subject becomes a named new character or product | `<descriptor> becomes <Name>: @Image N ...` |
| **Remove** | The subject should not exist in the new world | `<descriptor> is removed; that space shows <location detail>.` |
| **Background extra** | The subject stays as an unnamed person, restyled for the new world, with no locked identity | `<descriptor> remains as a background extra in <wardrobe for the new world>.` |
| **Generic object** | An incidental object restyled in text, under the prop threshold | `<descriptor> becomes a plain <object> matching the location.` |

Notes:

- Removing a subject whose motion drives contact (a partner lift, a handoff)
  leaves the other subject's motion unexplained. Prefer mapping or background
  extra, or trim the clip.
- A background extra has no reference image and no identity continuity across
  shots. If the same extra recurs or matters to the story, map them instead.
- Branded, recurring or story-critical objects need a locked reference; generic
  one-off objects can be described in text, following the prop threshold in
  the [element-identification contract](../../../contracts/element-identification.md).
- Real brand products and logos in the new world come from authorized
  downloads, not invented look-alikes.

## Crowds and background extras

A crowd may take one group disposition when no member is individually
featured:

```text
The spectators behind the barrier remain as background extras: about twenty
people in rain jackets and knit hats, standing and clapping.
```

Rules:

- Map every featured subject individually first; the group line covers only
  the remainder.
- State an approximate count and a region, so the crowd neither grows nor
  empties.
- Anyone who enters the foreground, speaks, touches a mapped subject or holds a
  mapped product is not "crowd". Give them their own disposition.
- Crowded sources are where extra people appear most. Pair the group line with
  the people-count guard in the guards reference.

## Reference budget

Count before writing:

| Item | Recommended | Hard limit |
| --- | --- | --- |
| Distinct mapped subjects (R2V) | 1–8 | 30 images total |
| Reference images per subject | 1–3 views (front, profile, back when needed) | — |
| Reference images in edit mode (plan B) | 1–5 | 30 images total |
| Source video | under 20 s for edit mode; 4–30 s for R2V | 10 videos, combined 30 s |
| Total materials | — | 50 |

Background extras, removed subjects and generic objects add no images. The
location usually takes one image.

When a count exceeds the recommended range, the package carries a warning:

```text
Reference-count warning: 9 mapped subjects and 16 images exceed the
recommended 1–8 subjects. Stability decreases as the count grows. Proposed
split: shots A (0:00–0:06, subjects 1–4) and B (0:06–0:12, subjects 5–9),
assembled in post. Alternatively, move subjects 7–9 to background extras.
```

The warning goes to the user; the agent does not silently proceed above the
range or silently drop subjects.

## More than eight subjects

When more than eight subjects must keep individual identities:

1. **Split by time.** Cut the source at its own hard cuts, or at a moment where
   the featured group changes. Each piece maps only the subjects visible in it.
2. **Split by priority.** Keep the featured subjects mapped and move the rest to
   background extras.
3. **Assemble.** Write one prompt block per piece, each at its natural
   duration with the same location and style references; the user generates the
   pieces and assembles them in post. Check the seams for identity, wardrobe and
   lighting continuity.

Never fold several subjects into one collage image to save slots.

## Multi-cut consistency

Hard cuts in the source are inherited, so the recast must keep who-is-where
across them.

- List per-cut presence in the Guards block when it varies:
  `In the first shot (about 0:00–0:04) Mara and Theo appear; in the close-up
  (about 0:04–0:06) only Mara appears; in the wide (about 0:06–0:09) both.`
- A subject keeps one name and one reference set across every cut, even when
  framing changes from wide to close-up. Add a close-up-friendly front view if
  the source cuts to a close-up of that subject.
- Keep one location reference for all cuts that happen in one place. If the
  source cuts between places, map each place to its own location reference and
  name which cuts use it.
- Timestamps allocate time; they are not frame-accurate edit points. Use the
  source cut times as approximate anchors.
