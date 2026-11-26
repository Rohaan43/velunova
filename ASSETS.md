# Asset provenance

Built-in ImageGen was used for the selected hero and transparent logo extraction. Project assets are stored locally in `dist/assets/`. The original user-supplied image remains unchanged.

## Celestial hero

Files: `dist/assets/celestial-hero.webp`, `dist/assets/celestial-hero-640.webp`.

Final selected prompt:

> Use case: stylized-concept. Asset type: premium creative digital marketing agency website hero art, horizontal 3:2. Create an exquisite cinematic 3D sculptural lavender satin-chrome planet with a broad impossibly thin elliptical orbital ring, floating over soft sculpted violet cloud forms. One small luminous four-point champagne star in upper right. Deep solid midnight plum background #160f25, subtle lavender and blush edge lighting. Planet central-right, sculptural smooth form, sophisticated art direction, surreal but minimal, physically rendered, editorial studio lighting, balanced negative space, no grain. Premium digital design studio, nod to dreamy celestial creative branding. Large main planet with lavender-to-silver iridescent material; ring arcs diagonally around it. No text, no lettering, no UI, no watermark, no humans.

## Logo

File: `dist/assets/velunova-logo.webp`.

Reference: the user-supplied Velunova image. The extracted logo is a raster interpretation; the supplied artwork is also displayed unchanged in the creative-world section.

Final selected prompt:

> Use case: background-extraction. Input image is the edit target. Extract ONLY the central Velunova company script wordmark with its sweeping orbital swash, star above, little cat-ear outline above the final letters, and small spaced CREATIVE STUDIO subtitle. Preserve the exact readable brand word Velunova, elegant flowing italic calligraphic lettering and orbit design from the input. Make all extracted logo elements uniformly warm white. Remove all other image content, all anime characters, backgrounds, unrelated text, tagline, clouds, castle and icons. Isolated company logo on genuinely transparent background. Tight horizontal canvas, logo large and crisp, no drop shadow, no color glow. This is an extraction of the provided logo, not a new logo.

## Other assets

- `dist/assets/velunova-banner.webp` and `velunova-banner-768.webp`: optimized copies of the user-supplied `Velunova_banner_clean.png`. The banner's animation uses CSS; the original image is preserved.
- `dist/assets/plushies/*.webp`: images extracted from the user-supplied `Custom-Character-Plushies (1).pdf` for the plushies showcase, labeled as illustrative concepts.

- `dist/assets/brand-universe.webp`: optimized copy of the supplied image.
- `dist/assets/outfit-latin.ttf`: self-hosted Outfit variable font from the Google Fonts repository. License: `dist/assets/OFL.txt`.
- Campaign and Bloom visuals: native HTML/CSS concept studies, explicitly labeled as illustrative, not client projects.
- `dist/assets/favicon.svg`: small companion V and star favicon.
