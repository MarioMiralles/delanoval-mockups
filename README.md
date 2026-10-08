# De La Noval, P.A. — homepage concepts

Four static homepage mockups for the redesign of [delanovalpa.com](https://delanovalpa.com/), plus a gallery page that links to them.

| Path | Concept |
| --- | --- |
| `index.html` | Gallery of all four concepts |
| `counsel/` | 1 · Counsel: quiet, traditional, all-caps headings, serif body |
| `editorial/` | 2 · Editorial: Bodoni display type, angled shapes taken from the DN monogram |
| `other-side/` | 3 · The Other Side: dark navy, "Then / Now" story, interactive claim check |
| `advocate/` | 4 · Advocate: lead-focused, intake form in the hero, working EN/ES switch |

Every concept uses the firm's existing brand: logo, navy `#051b34`, royal blue `#3957ff`, ice `#f5f7ff`, slate `#3b4855`.
`assets/chat.js` is a mockup of the SiteStaffr chat widget shared by all pages.

## Viewing

Plain HTML, no build step. Open `index.html` in a browser, or serve the folder:

```
python -m http.server 8000
```

Published with GitHub Pages from the `main` branch root (`.nojekyll` keeps the folders served as-is).

## Notes

- Images come from the firm's current website. Fonts load from Google Fonts.
- Pages carry `noindex` so the mockups stay out of search results.
- Text in `[brackets]` marks content the firm still needs to supply (ratings, case results, fee policy).
