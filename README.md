# Velunova Creative Studio

A responsive, dependency-free digital marketing and creative studio website built from the supplied Velunova brand reference. The site uses the original brand artwork, an extracted logo, a violet celestial palette, self-hosted Outfit typography, and optimized WebP images.

## Run and check

```sh
npm run dev
npm test
```

Open the URL printed by the server. The deployable website is `dist/`; no build or package installation is needed. The Node server is for local preview, while production uses static hosting.

## Included

- Responsive layout, mobile navigation, service accordions, and project dialogs.
- Original supplied artwork plus clearly labeled illustrative campaign and website concepts.
- A project brief form that validates answers and downloads a text file. It does not send an inquiry or save visitor data.
- Semantic HTML, skip navigation, labeled inputs, native keyboard-accessible dialogs and accordions, visible focus, and reduced-motion support.
- Search title and description, canonical URL, Open Graph and Twitter metadata, ProfessionalService structured data, robots.txt, and sitemap.xml.
- Local assets, responsive hero images, lazy-loaded below-fold images, and no client-side framework or third-party runtime requests.

## Before a public business launch

The user elected to skip business contact details. Supply a verified email, WhatsApp number, or form endpoint to enable direct inquiries. Keep the download-only copy accurate until delivery is connected.

New Sites are private by default. Search engines cannot index an authenticated private preview. Public access and a public domain are required for search visibility. If the domain changes, update absolute URLs in `dist/index.html`, `dist/sitemap.xml`, and `dist/robots.txt`. SEO rankings and production latency depend on hosting, the domain, competition, and ongoing content; no score or ranking is promised.

Confirm final service offerings with the business. Digital marketing services follow the user's brief; creative production services follow the supplied image. There are no invented clients, testimonials, results, or business contact details.

## Verification

Automated checks cover brief contents, asset references, section links, one H1, and structured metadata. Browser checks covered 320, 390, 768, 1024, and 1440 pixel widths, service expansion, project dialogs, service selection, mobile navigation, and successful local brief download. No browser JavaScript errors were observed. A public Lighthouse run, search indexing, and real-device network measurements have not been performed.

Generated asset provenance and prompts are in `ASSETS.md`. Outfit is licensed under the SIL Open Font License included in `dist/assets/OFL.txt`.
