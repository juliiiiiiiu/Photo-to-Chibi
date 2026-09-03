# Clean anime chibi recipe

Use this recipe as a visual control system, not as a request to measure pixels literally. Apply the hard gates in every generation, then select the target ranges for the current number of people. A result may move about 10% outside a target range when necessary to preserve identity, age, pose, or every visible person, except that one-person and couple body ratios must remain within their stated ranges.

## Priority order

When constraints conflict, preserve them in this order:

1. Correct person count and distinct identity cues, including the category and main colour of every visible garment.
2. The correct route-specific complete-figure body ratio.
3. The required three-colour outfit plan, including colour completion for unseen garments or a palette-completion accessory when necessary.
4. Extreme chibi silhouette and readable faces.
5. Clean anime line economy and flat cel rendering.
6. Appropriate interaction, expression, scenery, and minor finish preferences.

## Hard gates

- Redesign the subjects as anime characters; never apply a cartoon filter to realistic adult anatomy.
- Keep every requested or recognisable person exactly once. Do not invent, merge, hide, or remove people.
- For the one-person and couple routes, use only the 2.4–2.9-head body ratio. A complete figure's head must occupy 35–42% of its total height; do not use the family or group mascot ratios for these routes.
- Preserve all visible garment categories and main colours. Each person's final clothing-and-accessory design must contain at least three clearly distinguishable colour blocks under the clothing-colour completion rules below.
- Use a fully opaque, perfectly uniform pure-white (`#FFFFFF`) canvas by default, with no alpha transparency, floor, cast shadow, border, halo, or decoration. When the user explicitly requests a scenic background, this default is replaced by the scene requested in `SKILL.md`; do not retain white-canvas isolation clauses in the final prompt. Never depict a grey-and-white checkerboard, transparency grid, tiled pattern, or cutout-preview pattern. If the user explicitly requests transparency, use a real alpha channel rather than drawing a transparency pattern.
- Use flat cel colour. No watercolour, paper grain, painterly texture, realistic skin modelling, 3D gloss, or photographic lighting.
- Use a nearly invisible nose, simplified mouth, graphic anime eyes, and a short rounded chin. No nasolabial lines, realistic eyelids, pores, or individual beard hairs.
- Do not copy named characters, franchises, artists, costumes, logos, or supplied reference compositions.

## Route-specific body ratios

| Route | Total height | Head share of height | Shoulder span | Layout |
|---|---:|---:|---:|---|
| One person | 2.4–2.9 heads | 35–42% | 65–80% of head width | One complete figure |
| Couple | 2.4–2.9 heads each | 35–42% | 65–80% of head width | Two equal figures, heads close |
| Family or group, 3–6 | 1.65–1.90 heads each | 52–60% | 65–85% of head width | Compact staggered cluster |
| Group, 7+ | 1.80–2.10 heads each | 48–55% | 70–85% of head width | Readable multi-row lineup |

People in the same row should normally stay within about 10% of one another's head scale. Preserve meaningful child-versus-adult height differences without turning adults back into standard anatomy. For one-person and couple routes, show the complete torso, legs, and shoes clearly enough that the 2.4–2.9-head ratio is immediately readable.

## Face construction

- Use a wide rounded or softly squared head with a very short lower face. The chin should not project.
- Each open eye normally occupies about 18–24% of face width. Keep roughly one eye-width between the eyes, adapting for identity and expression.
- Build each iris from two or three flat colour zones with one large highlight and one small highlight. Use a strong upper lash line, a minimal lower line, and no glassy photographic reflections.
- **Iris colour:** use a luminous pale icy-blue palette for every character by default, regardless of the source eye colour: a cool blue-grey upper rim, a light aqua-blue main iris, and a very pale cyan lower zone. Add one large and one small clean white highlight; use deep blue-grey or near-black only for the pupil and upper lash line. Do not use brown, amber, hazel, green, purple, or red irises unless the user explicitly requests a different eye colour.
- Use no nose or one tiny dot or short mark. Do not shade a nose bridge.
- A closed mouth normally occupies about 8–15% of face width. An expressive open mouth may occupy about 20–35%.
- Use one soft cheek-blush shape per side when helpful. Do not airbrush the entire face pink.
- Simplify moustaches or beards into one or two clean flat shapes; omit stray hairs and realistic stubble.

## Silhouette and anatomy

- Keep the torso shorter than the head and visually subordinate to it.
- Use tiny simplified hands around 12–18% of head height and compact feet around 15–22% of head height.
- Keep fingers fused into mitten-like groups unless a gesture requires separation. Use no more finger detail than the gesture needs.
- Build hair from five to nine major clumps. Preserve the source hairstyle through the outer silhouette, parting, fringe direction, length, and one distinctive feature—not individual strands.
- Preserve clothing through two or three major colour blocks and signature features. Use only two to five structural fold lines per garment.

## Line recipe

- Set the visible outer character contour to light cool grey `#B8B7BA`. Keep internal construction lines at `#B8B7BA` or a lighter related grey. Do not use black, charcoal, deep brown, or deep blue for the complete outer silhouette.
- Use one clean, thin, continuous outer contour with sparse internal lines. It must be a single stroke only: never stack dark and light outlines, offset a second stroke, or add a white outline, rim, halo, glow, sticker edge, or anti-aliased-looking pale fringe outside the silhouette.
- Make the outer contour only about 1.1–1.25 times stronger than internal facial, hair, and garment lines; it should remain delicate rather than reading as a graphic border.
- Allow darker local colour only inside eyes, lashes, brows, pupils, and filled hair masses when it is needed for anime readability. These darker details must not replace the `#B8B7BA` silhouette contour.
- Keep the face and hands crisp. Remove scratch marks, hatching, fibre texture, repeated hair strokes, decorative seams, and non-structural folds.

## Colour and value recipe

- Set the flat skin base to `#FAE8DD`. Use a restrained peach-rose or cool rose-beige shadow close to the base; keep highlights near ivory. Do not apply a yellow-orange, grey, or brown global skin cast.
- Clothing palette: preserve every visible garment's main colour, then ensure that each person's final clothing-and-accessory design contains at least three clearly distinguishable colour blocks. Count only garments, shoes, and the single palette-completion accessory permitted below; never count skin, hair, eyes, scenery, shadows, or highlights. The required contrast applies to the completed outfit, not to a recolouring of visible source garments. Keep peak saturation limited to clothing, shoes, and the palette-completion accessory; keep skin, hair, eyes, and scenery within their separate restrained palette rules.
- Keep non-clothing areas at low-to-medium saturation. Do not spread peak saturation across skin, hair, eyes, or scenery.
- Use three broad value groups: light, middle, and limited dark. Do not distribute equal contrast everywhere.
- Keep skin light and neutral-warm. Avoid yellow-orange global grading and realistic red-brown facial shadows.
- Use a cool, violet, or restrained rose-violet shadow where compatible with the local colour. Avoid neutral grey and muddy brown.
- For black hair, use a very dark blue-grey, violet-grey, or brown-black base with readable separation from the outline.

## Clothing-colour completion recipe

- Preserve every visible garment and footwear category, main colour, and identity-defining detail; never recolour visible source clothing merely to satisfy the palette rule.
- First count the distinct, clearly visible outfit colours in the source. If fewer than three are present, supply only the missing colour blocks, using the minimum necessary completion.
- When a lower garment or shoes are not visible, retain the visible upper garment colour, use a clearly contrasting second colour for the lower garment, and use a third clearly contrasting colour in the shoes. The invented lower garment and shoes must not merely extend a visible white, beige, taupe, grey, black, or near-adjacent hue.
- When the complete outfit is visible but has fewer than three colours, preserve it unchanged and add exactly one small, natural palette-completion accessory—such as a belt, scarf, hair accessory, socks, shoelaces, or small bag—with only the missing contrast colour or colours. This accessory exists to complete the outfit palette; it is not a hero prop, decoration set, or additional character cue.
- Use strong, clearly visible hue and/or value contrast for every supplied colour block. Do not make the completion colours tonally adjacent, low-contrast, hidden, or so small that they fail to read at normal viewing size.
- Default unseen lower garments to straight-leg or gently tapered trousers, an A-line skirt, or shorts; do not invent flared, bell-bottom, or excessively wide-leg trousers unless the source supports them. When shoes are unseen, prefer simple canvas sneakers unless the clothing context strongly calls for another shoe type. For invented shoes, keep both shoes consistent as a pair and render each shoe with at least two visibly distinct colour areas across its body, toe cap, laces, and sole.

## Cel-rendering recipe

- Give each material one flat base colour and one hard-edged shadow step.
- Keep the main shadow around 15–30% of each material. Do not cover an entire face or garment in soft modelling.
- Allow a small second dark shape only in deep hair overlaps, under a collar, or between tightly overlapping figures.
- Limit highlights to the eyes and one or two designed shapes on a major hair or fabric mass.
- Use no skin gradient, bloom, rim-light aura, reflective environment colour, watercolour edge, paper grain, or brush texture.

## Expression recipe

- Assign one dominant emotion to each person: joyful, gentle, shy, excited, calm, or playful.
- Coordinate at least three expression signals: eyebrows, eye state, mouth shape, blush, head tilt, or body lean.
- For couples, use complementary expressions rather than duplicated smiles. Keep head sizes within about 5%, bring heads within about 0–25% of one head width, and use one clear shared interaction.
- For families and groups, vary expressions lightly while keeping the emotional tone coherent. Do not make every face identical.

## Controlled flexibility

Treat person count, identity separation, visible-garment preservation, the opaque uniform white default canvas, anime facial simplification, and flat cel rendering as absolute. Treat group numeric ratios as target ranges. For one-person and couple routes, the stated 2.4–2.9-head and 35–42%-head ranges are mandatory and may not be relaxed into a family-or-group mascot proportion. Relax only the minimum necessary range for a crowded group, a distinctive source pose, mobility equipment, cultural clothing, or an age-related identity cue. Never relax several categories at once merely to imitate the source photograph.

Do not paste every number into the generation prompt. Include the applicable route ratio, face simplification, line economy, cel-shading rule, palette hierarchy, expression, and isolation. Use the remaining measurements during review and retry.
