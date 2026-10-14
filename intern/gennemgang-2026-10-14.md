# Kredithjørnet mod byggeregelsættet: gennemgang 14. oktober 2026

Målt, ikke gættet: `vaerktoej/sprogtjek.py`, `vaerktoej/sidetjek.py`, Playwright-skærmbilleder og -målinger af alle 26 sider i 320, 375, 390, 430 og 1440 px, og hjemmesidetjekket på thordahlstudio.dk/ai-tjek/ (81/100 før).

Størrelse: **S** = under en time · **M** = et par timer · **L** = en dag eller mere.
Rækkefølge = det, der betyder mest for besøgende og Google, først.

## Skal rettes

| # | Afsnit | Fund | Størrelse | Status |
|---|---|---|---|---|
| 1 | 8 Jura | **Kreditmarkedsføring:** ydelse og rente vist uden ÅOP på forsiden, i begge beregnere, i en illustration og i eksempler. Se `kreditmarkedsfoering.md`. | M | Rettet |
| 2 | 8 Jura | **Partnerknapper var døde** (`href="#"`) på 21 sider og ikke markeret som reklame. | S | Rettet: peger på Mybanker, mærket »Annonce« og med provisionstekst. Adtraction-link mangler (spørgsmål). |
| 3 | 4 Mobil | **Overskriften klippes** i højre side på 12 sider i 320 px og på 5 sider helt op til 430 px (fx »Boliglånsberegner: se en vejledende fordelin«). Vandret scroll på /enkeltmandsvirksomhed/ i 320 px. | S (fælles CSS) | Rettet |
| 4 | 6 Fakta | Privatlivspolitikken siger, at skrifterne hentes fra Google Fonts. De ligger på sitet. Hosting står som GitHub Pages, men Cloudflare sidder foran. | S | Rettet |
| 5 | 6 Fakta | »Mest søgt« uden data, »Ingen persondata her« passer ikke helt (Cloudflare ser IP), forsidens beskrivelse lover skilsmisse, som sitet ikke har. | S | Rettet |
| 6 | 8 Jura | Intet CVR på sitet (e-handelsloven § 7). | S | **Venter på svar** |
| 7 | 7 SEO | http:// sender ikke videre til https:// (samme side på to adresser). | S | **Jakob i Cloudflare**, se nederst |
| 8 | 7 SEO | Meta description over 165 tegn på 17 sider (bliver klippet i Google). | S | Rettet |
| 9 | 7 SEO | Title over 60 tegn på 6 sider, tankestreg i 14 titler. | S | **Venter på dit ja** (titler på sider, der kan ranke) |
| 10 | 3 Sprog | Overlines/kapitelmærker (små tekster over overskrifter) på alle sider. | M | Rettet |
| 11 | 3 Sprog | Ca. 350 tankestreger i synlig tekst. | M | Rettet (ikke i titler) |
| 12 | 3 Sprog | »ikke X, men Y« ca. 25 steder. | S | Rettet |
| 13 | 3 Sprog / 7 SEO | Spørgsmål som h2, og de samme skabelon-h2'er på alle guides (»Hvem er guiden for?«, »Klar til at se, hvad flere banker vurderer?«). | M | Rettet til udsagn. FAQ-spørgsmål (h3/summary) beholdes. |
| 14 | 5 CSS | `[hidden]{display:none!important}` manglede. | S | Rettet |
| 15 | 7 SEO | `sitemap.xml` lastmod er håndskrevet (juli). | S | Rettet: fra git |
| 16 | 7 SEO | Sikkerheds-headers mangler (HSTS, nosniff, X-Frame-Options, Referrer-Policy). GitHub Pages kan ikke sætte dem. | S | **Jakob i Cloudflare** |
| 17 | 1 | Ingen FAKTA.md. AGENTS.md uden faktafil og tone. | S | Rettet |
| 18 | – | Interne filer (AGENTS.md, README.md, værktøjer) blev serveret offentligt på kredithjornet.dk. | S | Rettet med `_config.yml` (exclude) |

## I orden

| Afsnit | Hvad |
|---|---|
| 3 | Ingen floskler fundet. »Absolut løfte«-fundene er nægtelser (»vi lover ikke garanteret godkendelse«). |
| 3 | »vi« er sitets egen stemme som medie. Bevares (se FAKTA.md, Tone). |
| 4 | Ingen vandret scroll i 375–1440 px. Hero ikke klippet på forsiden. Kort står under hinanden på mobil. |
| 5 | `prefers-reduced-motion` respekteres. |
| 6 | Ingen opdigtede anmeldelser, kunder eller tal. Alle eksempler er mærket »konstrueret eksempel«. »30+ banker« passer (Mybanker). |
| 7 | Canonical, og:image med mål, `lang="da"`, gyldig JSON-LD (Organization, WebSite, Article, FAQPage, BreadcrumbList) på alle sider, robots.txt, 404-side. |
| 8 | Ingen cookies → intet cookiebanner. Korrekt. |
| 8 | Tinglysningsafgiften (1.825 kr. + 1,25 %) passer med Skattestyrelsens 2026-sats. |
| 9 | Ingen formularer. Beregnerne sender intet. |

## Gør selv i Cloudflare (5 minutter)

1. SSL/TLS → Edge Certificates → **Always Use HTTPS: On**.
2. Samme sted: **HSTS** → max-age 6 måneder, uden preload til at begynde med.
3. Rules → Transform Rules → Modify Response Header → tilføj
   `X-Content-Type-Options: nosniff`, `X-Frame-Options: SAMEORIGIN`, `Referrer-Policy: strict-origin-when-cross-origin`.

Det løfter hjemmesidetjekket med op til 10 point (B9, G1, G3, G4, G5).
