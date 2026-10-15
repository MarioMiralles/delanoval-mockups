# De La Noval, P.A. — homepage concepts

Four static homepage mockups for the redesign of [delanovalpa.com](https://delanovalpa.com/), plus a gallery page that links to them.
Each concept is a single homepage; menu links and buttons are placeholders.

| Path | Concept |
| --- | --- |
| `index.html` | Gallery of all four concepts |
| `counsel/` | 1 · Counsel: full-screen Brickell hero, Cormorant Garamond, dark practice-area gallery |
| `editorial/` | 2 · Editorial: DM Serif Display/Text, full-length portrait hero, angled shapes taken from the DN monogram |
| `other-side/` | 3 · The Other Side: dark, Fraunces, full-height portrait hero, interactive claim check |
| `advocate/` | 4 · Advocate: Marcellus, case review form in the hero, working EN/ES switch, Google Maps footer |
| `homepage/` | Merged homepage (Lazaro's pick, 2026-10-08): Concept 1 plus the guides (2), an injury and property claim check inside practice-area tabs (3), and the case review form and case types (4) |
| `about/` | About page (inner page 1, 2026-10-09): firm story, how we work, partners with credentials, reviews wall, case review form. Draft copy pending Lazaro's review |
| `about/lazaro-de-la-noval/`, `about/elizabeth-diaz-fernandez/` | Attorney profiles under About (same URLs as the current site). Generated from `about/index.html`'s shared CSS, header, form band and footer |
| `practice-areas/` + `property-damage/`, `personal-injury/`, `family-law/` | Practice overview and the three practice pages (same URLs as the current site): case types, claim check, steps, FAQ, case review form |
| `contact/`, `faqs/`, `blog/`, `blog/after-the-storm/` | Contact (ways to reach, form, map), FAQs (all topics), Blog index (filters) and one sample post. Same `/blog/` URL as the current site; in WordPress the article is the single-post template SiteStaffr posts will use |
| `es/` + `nosotros/`, `areas-de-practica/`, `contacto/`, `preguntas-frecuentes/` | Spanish version of the ten designed pages (2026-10-15), linked by the EN/ES switch on every page. **Generated, don't hand-edit:** built from the English pages by `delanoval-wp/tools/es/build_es.py` with the translation table `es.json`, which also builds the theme's Spanish templates |

Every concept uses the firm's existing brand: logo, navy `#051b34`, royal blue `#3957ff`, ice `#f5f7ff`, slate `#3b4855`, with Rubik for body text.

## Shared assets

- `assets/motion.css` + `assets/motion.js`: headline reveals on load, fade-up reveals on scroll, slow zoom on skyline heroes,
  count-up figures, header state on scroll and light parallax. All of it switches off under `prefers-reduced-motion`,
  and pages stay fully visible without JavaScript.
- `assets/chat.js`: a mockup of the SiteStaffr widget modeled on the plugin's own markup and CSS: the launcher and tooltip,
  the "How would you like to connect?" card, the text chat panel and a demo voice (listening) state.
  `data-style="refined"` on the script tag switches it to the plugin's Refined chat preset (used by `homepage/`).

## Shared menu and footer

`python tools/gen_site.py` (from the repo root) rewrites the menu and footer on every built page and rebuilds the
practice, Contact, FAQs and Blog pages from the content in `tools/gen_site.py` and `tools/gen_more.py`. Edit content there,
not in the generated HTML. The homepage, About and attorney profiles are hand-edited; the script only touches their menu and footer.

## Viewing

Plain HTML, no build step. Open `index.html` in a browser, or serve the folder:

```
python -m http.server 8000
```

Published with GitHub Pages from the `main` branch root (`.nojekyll` keeps the folders served as-is).

## Notes

- Attorney photos and the logo come from the firm's current website. Fonts load from Google Fonts.
- Pages carry `noindex` so the mockups stay out of search results.
- Text in `[brackets]` marks content the firm still needs to supply (ratings, case results, fee policy).
- "1,000+ cases resolved" and "$10M+ recovered" are the figures on the firm's current homepage.
- The merged homepage uses $25M+ recovered, per Lazaro (2026-10-08).

## Photo credits

All stock photography is public domain or CC0, so no attribution is required. Each license was confirmed at its source
on 2026-10-15 (the full list, with where each photo is used, is in the WordPress build repo's `docs/stock-photos.md`).

| File | Author | Source | License |
| --- | --- | --- | --- |
| `brickell-golden.webp` | Wilfredor | [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=165427769) | CC0 |
| `brickell-river.webp` | Carol M. Highsmith | [rawpixel](https://www.rawpixel.com/image/3094654/free-photo-image-miami-skyline) | Public domain |
| `brickell-night.webp` | Unknown | [rawpixel](https://www.rawpixel.com/image/5961024/free-public-domain-cc0-photo) | CC0 |
| `skyline-night.webp` | Unknown | [rawpixel](https://www.rawpixel.com/image/5961045/free-public-domain-cc0-photo) | CC0 |
| `skyline-storm.webp` | Unknown | [rawpixel](https://www.rawpixel.com/image/5947222/free-public-domain-cc0-photo) | CC0 |
| `library.webp` | Unknown | [rawpixel](https://www.rawpixel.com/image/3305593/free-photo-image-law-library-book) | CC0 |
| `pen.webp` | Unknown | [rawpixel](https://www.rawpixel.com/image/3298903/free-photo-image-cc0-creative-commons) | CC0 |
| `colonnade.webp` | Bob Richards | [StockSnap](https://stocksnap.io/photo/marble-pillars-IL9AITG3XV) | CC0 |
| `glass-tower.webp` | FOCA Stock | [StockSnap](https://stocksnap.io/photo/glass-building-CRXV0EN5I8) | CC0 |
| `storm-roof.webp` | Bob Epstein, FEMA | [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:FEMA_-_2440_-_Photograph_by_Bob_Epstein_taken_on_08-24-1992_in_Florida.jpg) | Public domain (U.S. government) |
| `blue-roof-keys.webp` | U.S. DHS | [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Operation_Blue_Roof_continues_in_Florida_Keys_(37478879700).jpg) | Public domain (U.S. government) |
| `i95-aerial.webp` | B137 | [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Miami_traffic_aerial_I-95_North_downtown.jpg) | CC0 |
| `biscayne-sunset.webp` | National Park Service | [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Biscayne_National_Park_H-adams_key_sunset.jpg) | Public domain (U.S. government) |
| `miami-waterfront.webp` | Gaetano Cessati | [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Miami_waterfront_skyline_(Unsplash).jpg) | CC0 |
| `brickell-day.webp` | Daniel Christensen | [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Brickell_skyline_2012.jpg) | Public domain |
| `everglades-storm.webp` | National Park Service | [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:WEA_glades_storm_1282,_NPSPhoto,_Haugen,_Oct_64_(9257940384).jpg) | Public domain (U.S. government) |

`hurricane-palms.webp` was removed on 2026-10-15: its CC0 status couldn't be confirmed at the source.
