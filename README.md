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

Every concept uses the firm's existing brand: logo, navy `#051b34`, royal blue `#3957ff`, ice `#f5f7ff`, slate `#3b4855`, with Rubik for body text.

## Shared assets

- `assets/motion.css` + `assets/motion.js`: headline reveals on load, fade-up reveals on scroll, slow zoom on skyline heroes,
  count-up figures, header state on scroll and light parallax. All of it switches off under `prefers-reduced-motion`,
  and pages stay fully visible without JavaScript.
- `assets/chat.js`: a mockup of the SiteStaffr widget modeled on the plugin's own markup and CSS: the launcher and tooltip,
  the "How would you like to connect?" card, the text chat panel and a demo voice (listening) state.

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

## Photo credits

All stock photography is public domain (CC0); no attribution is required, but sources are listed here.

| File | Photographer | Source |
| --- | --- | --- |
| `brickell-golden.webp` | Wilfredor | [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=165427769) |
| `brickell-river.webp` | Carol M. Highsmith | [rawpixel](https://www.rawpixel.com/image/3094654/free-photo-image-miami-skyline) |
| `brickell-night.webp` | Unknown | [rawpixel](https://www.rawpixel.com/image/5961024/free-public-domain-cc0-photo) |
| `skyline-night.webp` | Unknown | [rawpixel](https://www.rawpixel.com/image/5961045/free-public-domain-cc0-photo) |
| `skyline-storm.webp` | Unknown | [rawpixel](https://www.rawpixel.com/image/5947222/free-public-domain-cc0-photo) |
| `hurricane-palms.webp` | Unknown | [rawpixel](https://www.rawpixel.com/image/8726597/photo-image-palm-tree-public-domain) |
| `library.webp` | Unknown | [rawpixel](https://www.rawpixel.com/image/3305593/free-photo-image-law-library-book) |
| `pen.webp` | Unknown | [rawpixel](https://www.rawpixel.com/image/3298903/free-photo-image-cc0-creative-commons) |
| `colonnade.webp` | Bob Richards | [StockSnap](https://stocksnap.io/photo/marble-pillars-IL9AITG3XV) |
| `glass-tower.webp` | FOCA Stock | [StockSnap](https://stocksnap.io/photo/glass-building-CRXV0EN5I8) |
