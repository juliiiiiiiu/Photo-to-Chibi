# Original textual style specification

This specification is composed from generic chibi illustration and visual-design principles. It must not be attributed to, named after, or presented as an imitation of any artist, franchise, character, or supplied sample image.

## Shared visual language

- **Proportion:** use the adaptive ranges in [chibi-recipe.md](chibi-recipe.md). Single people and couples normally use 1.55–1.75 heads with the head occupying 58–65% of total height. Use a tiny torso, narrow shoulders, miniature hands and feet, and short rounded limbs.
- **Shape language:** soft ovals, flowing tapers, rounded corners, and a compact silhouette balanced by one elegant diagonal or S-curve. Avoid rigid front-facing symmetry, long adult anatomy, pronounced musculature, or fashion-illustration proportions.
- **Face:** use a wide rounded face, very short chin, nearly invisible nose, large graphic eyes, soft cheeks, and one unmistakable expression. Preserve identity through hairstyle, colouring, glasses, a simplified facial mark, and accessories rather than realistic facial anatomy. Remove eyelid anatomy, nose modelling, nasolabial structure, pores, and individual beard hairs.
- **Linework:** use sparse, clean, controlled anime linework. Set the visible character silhouette contour to `#A6A3A5`; keep internal construction lines at the same colour or lighter. The outer silhouette may be about 1.4–1.8 times stronger than internal lines, but never black or near-black. Eyes, lashes, brows, and filled hair masses may use deeper local colours. Group hair into five to nine major clumps and keep only two to five structural fold lines per garment. Never add scratch texture or a white die-cut sticker border.
- **Palette:** set the flat skin base to `#FAE8DD` with a restrained peach-rose or cool rose-beige shadow. Use five to eight main colour families per character. Keep most of the figure at low-to-medium saturation and reserve peak saturation for the eyes and one small focal accent occupying no more than about 10–15% of the figure. Do not shift skin toward yellow-orange, grey, or brown.
- **Value and temperature:** organise the figure into three broad value groups: light skin or fabric, middle-value local colours, and a limited dark hair or clothing anchor. Keep the face clear and luminous. Use a restrained cool or rose-violet shadow rather than neutral grey or muddy brown.
- **Rendering:** use one hard-edged cel-shadow step per material, normally covering about 15–30% of that material. Allow a small second shadow only in deep hair or clothing overlaps. Use one large and one small eye highlight and at most one simple highlight shape on each major hair mass. Avoid gradients on skin, watercolour wash, paper grain, painterly blending, realistic reflected light, pearlescent effects, plastic gloss, uncontrolled bloom, or photographic texture.
- **Isolation:** render only the character and any requested held prop on a fully opaque, perfectly uniform pure-white (`#FFFFFF`) canvas. Do not request alpha transparency by default. Never depict a grey-and-white checkerboard, transparency grid, tiled pattern, or cutout-preview pattern. No scene, floor, cast shadow, colour field, gradient, framing shape, halo, ribbon, sparkle, icon, border, or decorative motif is permitted. When the user explicitly requests transparency, return a real alpha channel and do not draw any transparency pattern.
- **Detail hierarchy:** use high detail at the face, eye, hand, and key prop; medium detail in hair groups and clothing seams; restrained detail on the remaining figure. Keep exactly one literal hero prop and do not repeat or echo it outside the character silhouette.

## Expression system

Choose one dominant emotion per character and make it readable at thumbnail size. Coordinate eyebrow angle, eye state, mouth shape, blush, head tilt, and body lean. Prefer anime shorthand such as closed-eye smiles, simple open mouths, tiny curved mouths, and restrained cheek colour. Do not rely on realistic facial modelling or generic identical smiles.

## Subject dominance

- The character or couple is the unmistakable focal point and normally occupies about 55–70% of the useful canvas area.
- The face and eye hold the sharpest edges and strongest light-dark contrast. The hero prop is the secondary focal point.
- All lighting, colour variation, texture, and decorative detail must remain inside the character and requested prop silhouettes.
- Preserve depth through internal overlaps, coloured shadows, hair grouping, and fabric layering—not through surrounding graphics.

## Styling routes

### Feminine

Use a soft rounded silhouette, gentle lashes or rounded eye corners, small decorative accents, and a cheerful or tender expression. Keep the user's actual hairstyle, clothing category, and accessories. Do not add dresses, bows, animal ears, or jewellery unless supported by the identity source or requested.

### Masculine

Use a compact rounded silhouette, slightly simpler eye treatment, clean brows, restrained decorative accents, and a friendly or calmly confident expression. Keep the user's actual hairstyle, clothing category, and accessories. Do not add suits, ties, hoodies, or masculine-coded props unless supported by the identity source or requested.

### Neutral

Use the shared visual language without adding gender-coded clothing, accessories, lashes, poses, or props. Let the identity source determine appearance cues.

### Couple

Give both characters matching scale, rendering, and visual weight. Preserve each person's hair, colouring, accessories, and clothing separately. Use one simple readable interaction: holding hands, standing shoulder-to-shoulder, a light side embrace, or presenting one shared prop. Keep limbs and hands visibly separate.

### Family

Keep all visible family members individually recognisable and age-appropriate. Use a compact, affectionate but non-romantic arrangement such as standing together, holding hands, or a gentle shared pose. Give adults, children, and older relatives equal identity care; do not turn any person into a background decoration or invent family members who are not in the source.

### Group

Keep all visible people individually recognisable with clear head separation, individual hair and clothing cues, and balanced visual weight. For three to six people, use a compact staggered arrangement. For seven or more, use a readable multi-row lineup with enough plain-white margin. Do not infer or state relationships, and do not remove visible people unless the user asks.

## Composition defaults

- Single person: square 1:1 canvas, complete character with a comfortable plain-white margin and a clear diagonal or S-curve through the pose.
- Couple: square 1:1 canvas, two complete characters, balanced side-by-side arrangement, equal prominence.
- Family: square 1:1 canvas for three to six people, or 4:5 if needed to preserve every person; use a compact shared pose and equal identity care.
- Group: square 1:1 canvas for three to six people, or 4:5 multi-row composition for seven or more; keep every visible person recognisable.
- Phone wallpaper: vertical opaque white canvas with the complete compact character or couple in the central safe area and generous plain-white space above and below.
- Preserve one meaningful source action, such as holding a strawberry or camera, and refine the prop for chibi readability. Do not repeat literal copies of it elsewhere.

## Outfit completion

When a source photo is cropped above the waist or does not show the lower garment, retain the visible top and invent a coordinated lower garment in a clearly different primary colour. Use hue separation or an approximate 15–25% lightness difference so the figure does not become a single-colour block. When shoes are hidden, prefer simple canvas sneakers with at least two distinct colours across the body, toe cap, laces, and sole. Preserve clearly visible source clothing and footwear instead of replacing them.

## Hard exclusions

Avoid any designed background, scenery, floor, cast shadow, colour field, gradient, vignette, border, panel, badge, halo, ribbon, star, sparkle, petal, icon, decorative motif, generic sticker or mascot-template aesthetics, white die-cut outlines, thick uniform black linework, excessive hair strands, beard hairs, facial anatomy, decorative clothing folds, duplicated literal props, rigid centred poses, standard anime portrait composition, adult body proportions, realistic anatomy, watercolour, children's-book illustration, semi-realistic painting, plastic gloss, uniform oversaturation, uniform desaturation, muddy grey-brown shadows, a yellow-orange skin cast, crushed dark hair, uncontrolled bloom, photographic bokeh, copied costumes, named characters, artists, franchises, signatures, logos, watermarks, invented people, merged people, or hidden group members.
