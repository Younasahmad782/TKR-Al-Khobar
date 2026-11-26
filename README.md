# TKR Al Khobar — bilingual website (EN / AR, RTL-ready)

Static site (HTML + CSS + vanilla JS) — no build step and no secrets. It continues the stack of the supplied menu page
(static HTML), so it deploys anywhere (Vercel, Netlify, Cloudflare Pages, any web server).

## Run locally
    python3 -m http.server 8000        # then open http://localhost:8000
(The menu loads `data/menu.json` with fetch(), so open it through a server, not by double-clicking the file.)

## Deploy
Upload this folder as-is. `404.html` is picked up automatically by Vercel/Netlify/Cloudflare Pages.
Before launch, replace `https://tkr-al-khobar.vercel.app` (canonical, hreflang, og:image, JSON-LD, robots.txt, sitemap.xml) with the real domain.

## Environment variables / API keys
None required. Map = keyless Google Maps embed; directions, reviews and WhatsApp are plain links.
Optional later: Google Places API key (server-side only) for live reviews; Place ID for a direct "Write a review" link.

## Structure
- `index.html` page + SEO + JSON-LD · `styles.css` (CSS logical properties; one stylesheet serves LTR and RTL)
- `app.js` — translations, language switch (`?lang=ar|en`, remembered in localStorage), menu search/filter, gallery lightbox, reviews, WhatsApp reservation
- `data/menu.json` — all 17 sections / 119 dishes · `tools/build_assets.py` regenerates menu.json + optimised images from the data pack
- `img/` optimised photos, `img/menu/` the 13 printed-menu photos (shown via "View printed menu")

## What is real vs. what is not built
- **Menu:** 119 dishes, prices and Arabic names exactly as in your data pack. 6 items show "Price to be confirmed" (4 sauces, Mash Potato, Sauteed Vegetable). Calories were deliberately left out (not fully verified).
- **Reviews:** only the 5 public Google reviews you collected + 4.5 / 346 and the star breakdown. No schema.org rating markup (deliberately).
- **Ordering:** NO online ordering/checkout — no official ordering link was found (HungerStation blocked). Site says to call/message. **Reservations:** a form that opens WhatsApp (050 900 9474) with a prefilled request; it never claims a booking is confirmed.
- **Photos:** only supplied photos; no stock images. No item-level dish photos exist, so none are shown.

## Needs your / the owner's confirmation
1. Permission from TKR to use the photos/logo publicly (data pack notes they belong to TKR and reviewers).
2. Two numbers: Google listing +966 54 599 0754 vs menu reservations 050 900 9474 — both shown with labels; confirm which is primary.
3. Hours (Daily 12 PM–1 AM) come from Google Maps only.
4. Prices for the 6 unpriced items; a native-Arabic review of the Arabic dish names marked as translated (all except the ones printed on the menu/bill).
5. Official ordering link (HungerStation/Jahez/etc.) or confirmation ordering by WhatsApp is accepted.
6. Google Place ID (for "Write a review" deep link) and a branch email, if any. The chain email info@tkrrestaurants.com was not used.
7. Real domain; tagline is mine (not an official slogan).
8. Menu has 3 platters/Dum Pukht items with advance-order rules — kept exactly as printed.
