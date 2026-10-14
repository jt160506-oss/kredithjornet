# Kredithjørnet

Komplet statisk website i ren HTML, CSS og JavaScript til `kredithjornet.dk`.
Sitet har intet byggeværktøj og ingen runtime-afhængigheder.

## Struktur

- Hver side ligger i sin egen mappe som `index.html`, så URL'erne bliver læsevenlige.
- Det fælles design ligger i `css/style.css`.
- Den fælles header og footer ligger i `partials/` og indlæses af `js/include.js`.
- Beregnerne kører lokalt i brugerens browser; indtastninger sendes ikke til sitet.
- `sitemap.xml`, `robots.txt`, `CNAME`, 404-side, metadata og strukturerede data er inkluderet.

## Udgivelse

1. Pak zip-filen ud.
2. Kopiér hele indholdet ind i roden af den mappe, der udgives som website.
3. Bevar en eventuel eksisterende skjult `.git`-mappe; den er ikke med i pakken.
4. Gennemgå ændringerne, før de udgives.

Mappen `konvertering-realkreditlaan/` er en bevidst kompatibilitets-redirect til
`/omlaegge-realkreditlaan/beregner/`. Den er markeret `noindex`, så gamle links
fortsat virker uden at skabe en konkurrerende indekserbar side.

## GitHub Pages + domæne
- Settings → Pages → Source: "Deploy from a branch" → main / root.
- Settings → Pages → Custom domain: kredithjornet.dk (CNAME-filen sikrer den binding).
- DNS hos simply.com peger allerede på GitHub Pages — det skal ikke ændres.

## Samarbejdspartnere
Sitet har i dag ingen annoncer eller affiliate-links. Knapperne fører til
tjeklisten og beregnerne. Se FAKTA.md og AGENTS.md, før et samarbejde sættes ind.
