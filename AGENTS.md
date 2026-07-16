# AGENTS.md — Arbejdsguide for Kredithjørnet

Denne fil læses af AI-assistenter (Claude, ChatGPT Codex m.fl.), der arbejder på sitet.
**Læs den, før du ændrer noget.** Den samler de spilleregler og erfaringer, vi har lært.

## Om projektet
Uafhængig dansk vidensside om boligfinansiering. Statisk HTML/CSS/JS på GitHub Pages.
Ingen build-step, intet framework. Introducér ikke framework/build uden Jakobs udtrykkelige ønske.

## Teknisk baseline
- Header og footer ligger i `partials/header.html` og `partials/footer.html` og hentes ind via `js/include.js`. Ret menu/footer **ét sted** — det slår igennem på alle sider.
- Alle sider linker til `css/style.css` (ét fælles designsystem).
- Sidespecifik CSS/JS (fx beregnere) ligger inline i den enkelte side.

## Designsystem — hold dette præcist
- **Indholdskolonne:** `.article-wrap` = max 820px med 24px sidepadding → indhold ~772px, venstrekant ~254px på desktop.
- **ALT indhold** (hero-tekst, brødtekst, illustrationer, CTA, fotobånd) skal ligge i denne kolonne. **Kun hero-baggrunde** må gå i fuld skærmbredde.
- `.editorial-illustration` og `.photo-band`: `max-width:772px`, centreret. Tjek det efter hver indsættelse.
- Fonte: DM Sans (brødtekst), Source Serif 4 (overskrifter).
- Farver via tokens i `style.css`: papir/creme baggrunde, mørk navy tekst, grøn/skovgrøn til handlinger, guld som accent.
- Bevar den varme, lyse skandinaviske finansæstetik. Ingen store mørke flader (undtagen footer).

## Navigation (IA)
Fem dropdowns: **Selvstændig · Skifte bank · Realkredit · Værktøjer · Om.**
- **Værktøjer** = Boliglånsberegner, Opkonverteringsberegner (`/omlaegge-realkreditlaan/beregner/#op`), Nedkonverteringsberegner (`.../beregner/#ned`).
- Beregner-siden læser `#op`/`#ned` og forudvælger retning (`setMode`).
- Guidesiderne op-/nedkonvertering hører under **Realkredit**.
- Sitemap, privatlivspolitik og affiliate-disclosure ligger **kun i footeren**.

## Fotos & illustrationer
- Brug fotos **varieret**: subtile hero-baggrunde (opacitet ~36%, roligt så teksten er læsbar), sidefotos i teksten, og et enkelt fotobånd. Undgå samme formel på alle sider.
- Ikke for mange visuelle elementer pr. side (typisk én illustration + evt. ét foto).
- Stockfotos gives en ensartet, varm, mat grade, så de fremstår som ét sæt.
- Vigtig tekst i HTML, ikke inde i billeder.

## Indhold & compliance
Se også brand- og indholds-dokumenterne. Kort:
- Generel information, ikke individuel finansiel eller juridisk rådgivning.
- **Ingen kategoriske jura-udsagn** (fx "lovkrav") uden opdateret kilde. Verificér satser, renter, afgifter og regler før publicering (fx Finanstilsynet, Skattestyrelsen).
- Mærk beløb og beregninger som **eksempler** med antagelser.
- Vis tydeligt, når brugeren sendes til en samarbejdspartner. Provisions-/affiliate-links: `rel="sponsored nofollow"`.
- Opfind aldrig ratings, cases, kundeantal eller tal.

## Før publicering — tjekliste
- [ ] Visuel gennemgang af **hver** side top-til-bund (ikke kun overflow/teknik)
- [ ] Ingen vandret scroll fra 320 til 1280 px
- [ ] Teknisk SEO: title ~55–60 tegn, meta description, canonical, `og:image`, billeddimensioner (`width`/`height`)
- [ ] Fakta, jura og satser verificeret mod officielle kilder
- [ ] Beregner-logik funktionstestet
- [ ] Ingen placeholders — fx `href="#"` skal have rigtige links (Adtraction/partner) før live
- [ ] Tilgængelighed: kontrast, synligt fokus, alt-tekster, `prefers-reduced-motion`

## Arbejdsmetode (erfaringer)
- Arbejd altid på en **branch**, aldrig direkte på `main`. Flet + push, når Jakob har godkendt.
- Ved subjektive valg (farve, fotoniveau, placering): vis **2–3 konkrete varianter** frem for at gætte.
- **Rene leverancer:** ingen `.DS_Store`/`.fuse_hidden`/junk i zips (`zip ... -x "*.DS_Store" -x "*.fuse_hidden*"`).
- Til preview af hele sitet: brug en **rigtig staging-URL** (fx Cloudflare/Netlify på branchen), ikke sammensyede enkeltfiler.
- Håndter assets konsistent: fotos som filer i `assets/img/`, ikke som base64 inline.
