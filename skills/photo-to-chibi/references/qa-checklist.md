# Quality checklist

Review the generated image before presenting it.

## All routes

- The number of characters matches the request or, in zero-text automatic mode, every recognisable person in the uploaded photo.
- Each character falls within the applicable route range in [chibi-recipe.md](chibi-recipe.md): 1.55–1.75 heads for one person or a couple, 1.65–1.90 for three to six, or 1.80–2.10 for seven or more.
- The head share, shoulder span, tiny hands, compact feet, and group layout satisfy the applicable recipe range. The torso is shorter than the head and no figure returns to adult anatomy.
- The person remains recognisable through high-signal cues: hairstyle and colour, skin tone, key accessories, facial marks, and clothing colours.
- The default composition is square and shows the complete character with a comfortable plain-white margin and no sticker border.
- The face is a redesigned anime symbol system: wide short face, tiny or absent nose, graphic eyes, simple mouth, short chin, and no realistic eyelids, nose bridge, skin texture, or beard hairs.
- The visible outer character contour uses `#A6A3A5`, not black or a near-black substitute. Internal construction lines use the same colour or a lighter related grey. Darker local colours remain confined to eyes, lashes, brows, pupils, and filled hair masses.
- The linework is clean and sparse. Outer contours are visibly stronger than internal lines without becoming darker than `#A6A3A5`; hair uses about five to nine major clumps; each garment has only a few structural fold lines. There is no scratch texture, hatching, white sticker border, or uniform heavy outline.
- Flat skin base uses `#FAE8DD`. Skin shadow is a restrained peach-rose or cool rose-beige close to the base, with no yellow-orange, grey, or brown global cast.
- The palette uses approximately five to eight main colour families per person. Most areas are low-to-medium saturation, with peak saturation limited to eyes and one small accent.
- The figure reads in three broad value groups. Shadows are chromatic rather than neutral grey or muddy brown, and dark hair retains separation from its outline.
- Each material uses one flat base and one hard-edged shadow step. A second shadow is limited to deep overlaps. There is no watercolour, paper grain, painterly blending, realistic skin modelling, pearl effect, plastic gloss, or uncontrolled bloom.
- The character or couple occupies about 55–70% of the useful area and remains unmistakably dominant. Faces have the sharpest edges and strongest contrast; the hero prop is secondary.
- The default output is fully opaque and every empty area, including all four corners, is perfectly uniform pure white (`#FFFFFF`) with no tonal variation. There is no alpha transparency unless the user explicitly requested it.
- There is no grey-and-white checkerboard, transparency grid, tiled pattern, cutout-preview pattern, or simulated transparency anywhere in the pixels.
- There is no scenery, floor, cast shadow, colour field, gradient, vignette, panel, badge, halo, circle, star, sparkle, ribbon, petal, icon, border, or foreground decoration outside the figure.
- Isolated edges are clean and antialiased, with no white matte, coloured fringe, accidental cutout, or die-cut sticker outline.
- Exactly one literal hero prop is present. A strawberry, flower, camera, or other key object is not duplicated or echoed as surrounding decoration.
- When the source does not show the lower garment, the invented lower garment has a clearly different but coordinated primary colour from the visible top, separated by hue or approximately 15–25% lightness. It does not create an unintended one-colour jumpsuit.
- When the source does not show footwear, the invented shoes are context-appropriate; canvas sneakers are preferred. Each canvas sneaker uses at least two visibly distinct colours across its body, toe cap, laces, and sole. Clearly visible source footwear is preserved.
- Detail follows a clear hierarchy: highest at the eyes, expression, identity-defining hair silhouette, hand gesture, and hero prop; lower everywhere else.
- Every character has one dominant emotion expressed through at least three coordinated signals. Faces do not use the same generic smile unless that is intentional.
- Hands, eyes, and facial features are not duplicated, fused, or malformed.
- The style reads immediately as an original, clean, highly super-deformed anime chibi rather than a realistic caricature, painterly portrait, generic cartoon, sticker template, or imitation of a specific reference character.
- There is no readable text, caption, logo, signature, or watermark.

## Couple route

- The couple route was explicitly requested or automatically selected for a two-person zero-text Try it upload.
- Each person keeps their own hairstyle, face, accessories, and clothing; no identity details are swapped.
- Both characters are equally prominent and visibly separate.
- The interaction is warm and appropriate to the request, with no unwanted sexualisation.

## Family and group routes

- Every recognisable person in the source appears once, with separate faces, limbs, hair, accessories, and clothing cues.
- Family composition is used only for an explicitly requested family or a source that clearly shows a mixed-age family. Otherwise use a relationship-neutral group composition.
- A family or group composition is never romantic or sexualised, and it does not add or omit people.
- Three to six people use a compact staggered arrangement. Seven or more use a readable multi-row arrangement, with no face hidden behind another figure.

## Retry rule

Treat a failure of route-specific proportion, anime face simplification, `#A6A3A5` contour colour, `#FAE8DD` skin base, line economy, flat cel rendering, colour hierarchy, unseen-outfit completion, multicolour shoe construction, expression clarity, uniform opaque white background, identity, person count, or prop uniqueness as material style drift. A checkerboard or transparency-grid pattern is always a material failure. Issue one corrective generation that repeats only the failed recipe checks. Do not retrieve or reuse artwork from the skill directory or a previous task. If the second result still fails, present the best result and ask the user which specific element they want adjusted.
