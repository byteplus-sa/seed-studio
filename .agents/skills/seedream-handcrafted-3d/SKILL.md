---
name: seedream-handcrafted-3d
description: >
  Write Seedream prompts for handcrafted stylized 3D characters, portraits,
  superheroes, and wardrobe material studies with expressive proportions,
  painterly matte surfaces, pencil hatching, and tactile fabrics. Use when
  this visual treatment is requested or a supplied reference shows it; not
  for every character sheet, photorealism, animation, or exact graphic layouts.
---

# Seedream Handcrafted 3D

Translate a character concept into a coherent handcrafted 3D visual treatment.
Return a prompt package, not a generation, selection, or publishing workflow.
Deliver Lumina-paste-ready prompts in chat. Do not call an API, generate media,
select candidates, publish, or load another skill. Save prompt drafts only when
the user explicitly asks; the caller owns any later generation and persistence.

## Inputs and output

Use the supplied character concept, cultural context, wardrobe, palette,
reference images, and requested format. Ask for information only when it
materially affects the result; otherwise state a reasonable creative assumption.
Do not require reference images for a text-only concept.

Return:

1. A concise design description separating identity, costume, and style.
2. A ready-to-use prompt with only relevant sections: References, Task,
   Subject, Setting, Style, Lighting, Composition, and Constraints.
3. Ordered reference roles, destination-UI settings outside the prompt, and a
   short visible-design checklist for the user's later candidates.
4. Any unresolved inputs or visible deviations that affect later reuse.

When several prompts are requested, keep the character and wardrobe descriptors
consistent across them. Provide the requested number of creative alternatives;
do not invent a paid sampling count or approval state.

## Visual treatment

Use this adaptable style block:

> Handcrafted stylized 3D with a painterly finish. Appealing expressive anatomy,
> clearly sculpted hair, matte painted surfaces, fine drawn hatch marks, and
> dimensional cloth. Resolve knit loops, woven fibers, stitched seams, layered
> footwear, and restrained scuffs. Soft neutral lighting keeps the surface
> texture readable without glossy plastic highlights.

Adapt the block to the subject. Skin and hair belong in portraits and character
views, not garment-only macros. Use elongated necks and limbs, larger eyes, and
simplified anatomy as optional choices; preserve supplied age, body shape,
accessibility features, and locked proportions. Describe two or three deliberate
craft details rather than covering every surface with damage or noise.

Beauty comes from silhouette, facial structure, expressive design, and harmonious
color. Do not equate beauty with lighter skin, thinness, or one facial template.
Keep culturally specific identity grounded in the user's descriptions and
references; do not invent traditional meanings, sacred motifs, or a stereotyped
costume. Original heroes use newly described silhouettes and abstract motifs.

## Reference binding

Separate style, identity, wardrobe, and material roles, even when one image has
more than one role. Label images in their actual input order and bind each role
again in the prompt where it applies.

- For a new character, say that the style reference guides rendering and
  craftsmanship while the new subject description supplies identity and outfit.
- For an existing character, preserve its approved face, hair, silhouette,
  clothing, accessories, and palette. A style change does not authorize redesign.
- For a material study, use the selected character sheet as the costume source
  when available. A generic textile reference supplies texture, not a new outfit.

Use T2I when there are no images and I2I when any image guides the result. Do not
invent image bindings, approved selections, or unsupported provider parameters.
Inspect accessible supplied images before describing visible details. If a named
image is missing or unreadable, ask for it and mark its details unresolved; do not
claim to have inspected it. A text-only exploration may still be offered when it
does not depend on matching that image, clearly labeled as an exploration.

## Output formats

Read [format recipes](references/format-recipes.md) for the requested format.
This skill supplies art direction within a format, not a mandatory turnaround
layout. A prose composition hint can be combined by the caller with an identity
sheet workflow such as `seedream-character-sheet`; this skill stays independent.

- **Portrait or hero image:** prioritize an identifiable face, strong silhouette,
  and the requested expression or pose. Use the user's environment and lighting.
- **Character sheet:** preserve the requested views and framing. For an
  unspecified three-panel sheet, use back full-body, front full-body, and face
  close-up with a neutral studio background and even light.
- **Material study:** show only the requested cloth, seams, ornament, and footwear
  details. Put garment surfaces across the upper frame edge to avoid accidental
  chin fragments. Keep portraits and full figures outside this format.

Do not automatically remove heads from character sheets. A downstream single-face
policy is a separate caller decision and does not apply to ordinary turnarounds.

## Candidate checklist

Give the user checks for the requested views, complete head-to-foot framing
where applicable, consistent face/hair/outfit, readable material scale, and
coherent lighting.
Check hands, footwear, costume closures, accessories, and left/right placement.
For a collection, compare facial structure, hair, silhouette, and palette so the
characters have distinct identities rather than only recolored clothing.

Include checks for face fragments and invented costume changes in material
studies.
Character sheets govern exact costume geometry; macros support texture and
palette unless their construction has also been checked against the sheet.
When the user shares a candidate and asks for feedback, inspect it and declare
differences instead of claiming exact consistency. Retain the source when
proposing a correction and describe the specific visible change needed.

## Destination-UI settings

Keep settings outside the copy-paste prompt. Carry forward the user's selected
Seedream model, aspect ratio or dimensions, and format. If unspecified, say
"Seedream model available in your destination UI" and recommend an aspect ratio
for the requested composition: square portrait, landscape three-panel sheet,
or landscape three-panel material study. These are composition suggestions,
not verified model limits. Do not invent model IDs, prices, sampling counts,
or unsupported toggles.

## Scope and provenance

Captions, labels, taglines, logos, UI, and exact graphic layouts are outside this
prompt's scope. Keep the image text-free; any overlay text is added later by the
destination workflow. Do not add animation, 3D modeling, or assembly instructions.

Adapted from [ark-director PR #28](https://github.com/byteplus-sa/ark-director/pull/28)
at revision `cd2a85c9ff9529181c27a464a31dbbae9f220ac3`. This local bundle contains
prompt recipes, not rendered examples or generation evidence. Recipes and crop
wording are artistic suggestions; they do not guarantee a candidate's quality.
