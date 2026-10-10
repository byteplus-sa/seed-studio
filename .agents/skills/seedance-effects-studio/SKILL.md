---
name: seedance-effects-studio
description: >-
  Write Seedance 2.5 prompts for 45 named visual effects, including street
  colossus, incline, clones, melting, world morphing, eyes in, bullet time,
  earth zoom and smash and grab. Match a photo, product or source clip to a
  recipe and deliver its prompt, reference roles, parameters, post needs and
  observed limitations. Use for a named effect or an effects menu. Prompt
  composition only; never generates, submits or loads sibling skills.
---

# Seedance Effects Studio

**One capability: compose a named effect prompt.** Deliver the frozen prompt
package in chat for Lumina or another Seedance UI. Save it only when the user
explicitly asks. The calling agent owns any separately authorized generation
under [Generation transport](../../contracts/generation-transport.md).

## Origin and evidence

Adapted from the [pinned upstream skill](https://github.com/byteplus-sa/ark-director/tree/4b7bbade2de83eb5fd8bd26f50655983ed99a2a6/.agents/skills/seedance-effects-studio),
merged through PR #22.

The menu adapts 45 visual mechanics from example footage on a third-party
public effects page, analysed upstream on 2026-10-08. These descriptive labels
are not official Seedance presets or an endorsement. Recipes retain upstream
reported tests on invented subjects; none was re-rendered in this workspace.
See [evidence status](references/evidence-status.md) for outcomes and limits.

## Composition boundaries

| Need | Composition hint |
| --- | --- |
| General Seedance grammar | `seedance-prompt-25` |
| Whole-clip medium change | `seedance-restyle` |
| Swap one kept element | `seedance-object-swap` |
| Identity, real products and reference roles | [Element identification](../../contracts/element-identification.md) |
| Source inspection, muted master and original post audio | [Video-to-video inputs](../../contracts/video-to-video-inputs.md) |
| Exact text, logos, HUD, UI or fixed layouts | Added in post by the destination workflow; out of scope for this leaf |

Sibling names are composition hints, not instructions to load another skill.
A `composite` recipe supplies only its generated-footage prompt and a post
handoff. The full signature effect may depend on that post work.

## Menu

If the user names an effect, go directly to its recipe. For a broad request,
show the relevant groups with labels, looks and start inputs; ask which effect
they want. If their input is vague, offer three compatible choices.

### Camera and motion

Recipes: [effects-camera-and-motion.md](references/effects-camera-and-motion.md)

| id | Label | Route | Duration | Start input |
| --- | --- | --- | --- | --- |
| `wild-ride` | Wild ride | `i2v-first-frame` | 10 s | Car with a person leaning out, open space |
| `incline` | Incline | `i2v-first-frame` | 7 s | Calm person, visible floor, some clutter |
| `street-colossus` | Street colossus | `i2v-first-frame` | 10 s | Full-body standing person, outfit clearly visible |
| `tracking` | Tracking | `composite` | 5 s | Performer in motion, hands and face clear |
| `bullet-time` | Bullet time | `i2v-first-frame` | 15 s | Seated person holding a drink, medium shot |
| `high-flip` | High flip | `i2v-first-and-last` | 9 s | Person in a distinctive place, headroom above |
| `floating-fall` | Floating fall | `i2v-first-frame` | 12 s | Person holding 2-4 clear items outdoors |
| `moonwalk` | Moonwalk | `i2v-first-and-last` | 15 s | Full-body person, clean side-on stance |
| `studio-slide` | Studio slide | `i2v-first-frame` | 8 s | Full-body fashion photo, plain solid backdrop |

### Clones and identity

Recipes: [effects-clones-and-identity.md](references/effects-clones-and-identity.md)

| id | Label | Route | Duration | Start input |
| --- | --- | --- | --- | --- |
| `clones` | Clones | `i2v-first-frame` | 7 s | Full-body, standing, wide open location |
| `infinite-clones` | Infinite clones | `reference-images` | 7 s | Full-body, distinctive outfit and headwear |
| `selfception` | Selfception | `i2v-first-frame` | 5 s | Standing, open palm holding a tiny copy |
| `act-natural` | Act natural | `i2v-first-frame` | 6 s | Person caught mid-action, busy location |
| `stop-world` | Stop world | `i2v-first-frame` | 8 s | Standing figure inside a crowded space |
| `eyes-in` | Eyes in | `i2v-first-frame` (+ optional second clip) | 7 s | Portrait, open eye toward camera, well lit |
| `lacewalker` | Lacewalker | `reference-images` | 8 s | Full-body outfit, readable face with glasses or hat |
| `superstar` | Superstar | `reference-images` | 15 s | Clear face, distinctive outfit, waist-up |
| `vanish` | Vanish | `i2v-first-frame` | 5 s | Loose shape-holding clothes, kneeling or leaning |

### World and transformation

Recipes: [effects-world-and-transform.md](references/effects-world-and-transform.md)

| id | Label | Route | Duration | Start input |
| --- | --- | --- | --- | --- |
| `world-morphing` | World morphing | `i2v-first-frame` | 8 s | Centered person, open street, tall surroundings |
| `architecture-wave` | Architecture wave | `i2v-first-frame` | 7 s | Low-angle person, big rigid structure behind |
| `melting` | Melting | `i2v-first-frame` | 7 s | Full-body standing person, flat clear ground |
| `burning-man` | Burning man | `i2v-first-frame` | 7 s | Full-body person, empty space beside, dusk |
| `particles` | Particles | `composite` | 5 s | Single subject, dark high-contrast scene |
| `lidar` | Lidar transition | `i2v-first-and-last` | 7 s | Person outdoors, distinct posts and skyline |
| `earth-zoom` | Earth zoom | `i2v-first-and-last` | 10 s | Eye-level person on a plausible city street |
| `blue-depth` | Blue depth | `i2v-first-frame` | 8 s | Waist-up person in front of dark blue water |
| `desktop-glitch` | Desktop glitch | `composite` | 5 s | Cool-toned action shot with negative space |

### Art and style

Recipes: [effects-art-and-style.md](references/effects-art-and-style.md)

| id | Label | Route | Duration | Start input |
| --- | --- | --- | --- | --- |
| `comic` | Comic | `v2v-restyle` | source length (typ. 5 s) | user's clip, one central subject |
| `canvas` | Canvas | `v2v-restyle` | source length (typ. 5 s) | user's clip, one separable moving subject |
| `palette` | Palette | `v2v-restyle` | source length (typ. 5 s) | any clip, wide-angle or fast motion |
| `lsd` | LSD | `v2v-restyle` | source length (typ. 5 s) | clip, people close to camera |
| `scrapbook-collage` | Scrapbook collage | `composite` | 6 s | full-body standing, plain background |
| `cutout` | Cutout | `i2v-first-and-last` | 8 s | person small in structured environment |
| `pearl-earring` | Pearl earring | `composite` | 7 s | head-and-shoulders face, plain background |
| `cyclope` | Cyclope | `composite` | 7 s | one person, full body, outdoor |
| `fallen-angel` | Fallen angel | `composite` | 7 s | clear upper-body portrait, one person |

### Product, creature and spectacle

Recipes: [effects-product-and-spectacle.md](references/effects-product-and-spectacle.md)

| id | Label | Route | Duration | Start input |
| --- | --- | --- | --- | --- |
| `smash-and-grab` | Smash and grab | `i2v-first-frame` | 10 s | Product alone on a car seat, shot through window |
| `boarding-pass` | Boarding pass | `i2v-first-frame` | 9 s | Full-body person on plain white floor |
| `monster-dab` | Monster dab | `i2v-first-frame` | 10 s | Person walking toward camera, open sky behind |
| `pigeons` | Pigeons (animal ride) | `composite` | 8 s | Full-body person on a city pavement |
| `skatedog` | Skatedog (animal ride) | `composite` | 8 s | Full-body person on smooth street or promenade |
| `agamemnon` | Agamemnon | `i2v-first-frame` | 15 s | Selfie taken seated in a dark cinema |
| `mighty-fighter` | Mighty fighter | `composite` | 11 s | Clear face-forward portrait, head and shoulders |
| `fairytale-castle` | Fairytale castle | `i2v-first-frame` | 15 s | Person in profile in an empty dusk meadow |
| `frozen-in-motion` | Frozen in motion | `i2v-first-frame` | 7 s | Full-body person mid-jump on a busy street |

## Procedure

1. **Resolve the effect.** Read its section from one group reference. Clarify
   missing choices that affect the result; never guess unseen asset details.
2. **Inspect the supplied input.** Check the recipe's start-photo or source-clip
   requirements. Read images directly; inspect video by an agent video pass
   when available, or by extracted frames read as images. State the access
   boundary. Missing assets remain open items, with a concrete description of
   the required first frame, last frame or empty environment plate.
3. **Fill the slots.** Use observed subject, wardrobe, scene and prop facts.
   Preserve canonical descriptors and explicit counts. Name limbs by anatomy
   and frame side. Identify visible props; lock references only when qualified
   under element identification. Keep rights questions separate from creative
   choices for real likenesses or brands.
4. **Compose.** Keep the recipe's signature mechanics, camera path and timed
   beats. Adapt requested duration proportionally when necessary. The effect's
   camera choreography belongs to the recipe; omit incidental template lens,
   lighting, grade or acting defaults unless requested. Keep appearance or
   light changes that define the chosen effect itself. Resolve alternatives and delete unused
   slots. Keep duration, ratio and resolution in the parameter note rather
   than repeating clip length in the prompt.
5. **Handoff.** Deliver the exact paste-ready prompt, ordered reference roles,
   parameter suggestions, missing inputs, destination post needs and material
   evidence limits. Do not promise exact counts, cut frames or identity.
   Freeze the text; a revision is a new version with its named change.
6. **Returned take, when supplied.** Compare its signature mechanics against
   the recipe's acceptance observations, state how it was inspected, and
   propose one concrete repair. Technical inspection and sampled frames do
   not establish full visual quality or audio quality.

## Input routes

| Route | Prompt reference roles | Handoff |
| --- | --- | --- |
| `i2v-first-frame` | One `@Image 1` as opening frame | Ratio follows that image |
| `i2v-first-and-last` | Opening and ending images | Matching ratio; both frames needed |
| `reference-images` | Identity or appearance references | State roles and ignored pose/background; do not mix with first-frame roles |
| `v2v-restyle` | Source `@Video 1`, empty environment `@Image 1` when needed | Muted source and original audio restored in post under local video-to-video contract |
| `composite` | Recipe's footage roles | Full effect requires destination post work |

Route compatibility and provider restrictions quoted in recipes are dated
upstream observations, not universal current capability claims. The caller
checks destination support before any authorized submission. A provider
rejection needs diagnosis; changing the role is not permission to bypass it.
Virtual Portrait anchors apply only to invented identities, as specified by
the local video-to-video contract.

## Prompt rules

- **No overlay text in generation.** Captions, city names, labels, tickets,
  readable UI, logos and HUD copy are destination post needs.
- **Audio follows the brief.** Recipes generally recommend native audio off.
  Remove conditional audio lines when off; when requested, use explicit sound
  brackets and the requested arc. Upstream tests leaked music or vocals even
  with exclusions, so a clean audio master needs separate verification.
- **Counts and continuity are observable.** State copy counts at each change;
  all copies share one face and outfit. Count foreground arrivals too; adapt
  the recipe when the user requests a total count. Prompt counts remain
  probabilistic.
- **No hidden workflow.** This leaf neither submits nor prepares requests,
  creates projects, enforces a draft ladder or saves files automatically.
- **Evidence stays bounded.** Report `canvas`, `palette` and `lsd` as not
  achieved in the cited run; a recipe's presence is not proof it works.

## Reference loading

Read only the selected effect's group reference and, when its reliability
matters, [evidence status](references/evidence-status.md). Recipe acceptance
observations are for user-supplied takes; they do not trigger a separate
review workflow or gate prompt delivery.
