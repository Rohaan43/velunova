# Velunova Creative Studio

Next.js App Router website with React components, a custom plushies showcase, self-hosted fonts, and optimized artwork.

## Develop

Requires Node.js 20.9 or newer.

```sh
npm ci
npm run dev
```

Visit the local URL printed by Next.js. Pages live at `/` and `/custom-plushies`.

## Build and verify

```sh
npm run build
npm test
npm start
```

The Next.js build generates the static website in `out/`. `npm start` previews that output at `http://127.0.0.1:3000`. Generated `out/` and `.next/` directories are ignored by Git.

## Source layout

- `app/`: pages, shared layout, SEO metadata, and styles.
- `components/`: shared header and footer, mobile navigation, privacy and project dialogs, and the brief form.
- `lib/`: project descriptions and the project brief formatter.
- `public/assets/`: local images, icons, and the Outfit font.
- `public/robots.txt` and `public/sitemap.xml`: search discovery for the public domain.

Native details elements preserve service and FAQ behavior. React owns interactive navigation, dialogs, and form submission. The project form validates answers and downloads a brief locally; it does not send an inquiry or store visitor data. Contact details were intentionally omitted by the user.

## Deployment

Vercel configuration selects Next.js, runs `npm run build`, and serves `out/`. The old `/custom-plushies.html` URL redirects permanently to `/custom-plushies`. Keep the production branch selection in Vercel aligned with the branch intended for publication.

The existing Sites manifest also points to `out/` for static hosting. Source code and assets are versioned; build output is regenerated for deployment.

Tests cover project brief contents, exported assets, cross-page links, section anchors, unique IDs, one H1 per page, and structured metadata. Run the build before testing.

Image provenance and generation prompts are in `ASSETS.md`. Outfit's license is included at `public/assets/OFL.txt`.
