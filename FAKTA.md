# FAKTA.md: Kredithjørnet

Låst faktafil. Intet tal, ingen påstand og intet løfte på sitet, som ikke står her først.
Ændres en værdi, ændres den her, og hele repoet søges igennem efter den gamle.

Udarbejdet 14. oktober 2026 ud fra det, der stod på sitet den dag.
**[?]** = kan ikke bekræftes ud fra sitet eller offentlige kilder. Jakob svarer.
**[✓ kilde, dato]** = bekræftet.

---

## Virksomhed og kontakt

| Felt | Værdi på sitet | Status |
|---|---|---|
| Navn | Kredithjørnet | ✓ |
| Juridisk ejer / CVR | Intet CVR. Jakob driver sitet privat uden indtægt (svar fra Jakob 14.10.2026) | ✓ Intet CVR vises. Kommer der indtægt (affiliate), skal sitet registreres og CVR stå i footeren. Thordahls CVR bruges ikke. |
| Ejer / udgiver | »Jakob«, uafhængig udgiver fra Silkeborg (om-siden, privatlivspolitikken) | ✓ (kilde: Jakob). **[?] Må efternavnet stå på om-siden?** |
| Forfatter på guiderne | »Kredithjørnet« (byline og JSON-LD). Udgiveren Jakob står på om-siden | ✓ Kun Jakob skriver. Sitet taler som »vi« = Kredithjørnet, men påstår ikke en redaktion med flere personer. |
| By | Silkeborg, Danmark | ✓ |
| Telefon | +45 81 61 66 08 (`tel:+4581616608`) | **[?] Hvis nummer er det, og bliver det taget?** |
| E-mail | kontakt@kredithjornet.dk | **[?] Virker postkassen? (ikke testet med en rigtig mail)** |
| Domæne | kredithjornet.dk | ✓ |
| Hosting | GitHub Pages bag Cloudflare-proxy | ✓ svar-headers 14.10.2026 (`server: cloudflare`, `x-github-request-id`) |
| Besøgstal | Cloudflare Web Analytics (cookiefri) | ✓ script i alle sider |
| Skrifter | Selvhostet (DM Sans, Source Serif 4) | ✓ `assets/fonts/` |
| Cookies | Ingen | ✓ ingen script sætter cookies. Derfor intet cookiebanner. |
| Kontaktformular | Ingen. Kun mail og telefon | ✓ |

## Hvad sitet er og ikke er

- Uafhængig dansk vidensside om boligfinansiering. Generel information, ikke personlig rådgivning. ✓
- Ikke en bank, ikke långiver, ikke boligkreditformidler. Sitet henviser kun videre. ✓ (Se juridisk note i `intern/kreditmarkedsfoering.md`: en ren henviser er ikke kreditformidler efter boligkreditdirektivets definition, men det forudsætter, at sitet ikke selv rådgiver om eller formidler konkrete lån.)
- Har ingen indtægt. Ingen annoncer, ingen samarbejdspartnere. ✓ (Jakob, 14.10.2026)

## Samarbejdspartnere

**Ingen.** Ingen annoncer, ingen affiliate-links, ingen provision (Jakob, 14.10.2026: Mybanker har ikke svaret på ansøgningen i 2 til 3 måneder).
Partnerknapperne er erstattet af næste skridt på sitet (tjekliste, beregnere). Kommer der et samarbejde: mærk »Annonce«, `rel="sponsored nofollow"`, opdatér /affiliate-disclosure/, privatlivspolitikken og footeren, og registrér CVR.

## Tal og satser, der står på sitet

| Påstand | Hvor | Status |
|---|---|---|
| Realkredit op til 80 % af en helårsbolig | flere guides | ✓ realkreditloven (lånegrænse 80 % for ejerboliger) |
| Udbetaling mindst 5 % »som udgangspunkt« | flere guides | ✓ Finanstilsynet, orienteringsbrev om inspektioner af boliglån (linket på /hvad-er-realkreditlaan/) |
| 80/15/5-modellen | forside, beregner, guides | ✓ som »typisk fordeling« (ikke en regel) |
| Tinglysningsafgift pant: 1.825 kr. + 1,25 % fra 1. januar 2026 | /skifte-bank-boliglaan/omkostninger/ | ✓ skat.dk, nyhedsbrev »Tinglysningsafgift: ny afgiftssats pr. 1. januar 2026« |
| Rådighedsbeløb 2026: 7.880 kr. for en voksen, + 5.480 kr. for ægtefælle/samlever, + 2.150 / 2.740 / 3.950 kr. pr. barn (under 2 / 2–6 / 7–17 år) | /raadighedsbeloeb-boliglaan/ | ✓ Skatteforvaltningen, regulering af gældsinddrivelsesbekendtgørelsen for 2026 (info.skat.dk, oid=2460007). Brugt som pejlemærke for minimum, ikke som bankens krav. De gamle intervaller uden kilde er fjernet. |
| Opkonvertering: »7 kurspoint pr. procentpoint« | /omlaegge-realkreditlaan/opkonvertering/ | Fjernet (ingen kilde). Erstattet af, at kursen bevæger sig mere, jo længere løbetiden er. |
| Nedkonvertering: »tommelfingerregel omkring 1,5 procentpoint« | omlægning, beregner | ✓ som udbredt tommelfingerregel (ikke en regel), formuleret forsigtigt |
| Startværdier i boliglånsberegneren: realkreditrente 4,0 %, banklånsrente 7,5 %, bidrag 0,65 %, 30 år | /boliglaan-beregner/ | Illustrative antagelser, ikke markedssatser. Står som »illustrative startværdier«. ÅOP vises nu ved siden af. |
| Alle kronebeløb i eksempler | guides | Konstruerede eksempler, mærket som sådan. Ikke kunder eller cases. |

## Påstande, der må bruges

- »Uafhængig«: ingen bank eller långiver ejer eller styrer indholdet (kilde: Jakob).
- »Gratis at bruge«, »uden login«: sitet har ingen konti eller betaling.
- »Beregningen sker i din egen browser«: beregnerne sender intet (✓ koden, 14.10.2026).

## Påstande, der ikke må bruges

- »Mest søgt« (stod på forsiden): ingen data bag. Fjernet.
- »Ingen persondata her« (stod i forsidens hero): Cloudflare behandler IP-adresser i drift og statistik. Erstattet af »Ingen login«.
- Skilsmisse som emne (stod i forsidens beskrivelse): sitet har ingen side om det. Fjernet.
- Laveste rente, sikker besparelse, garanteret godkendelse, »bedste lån«.
- Anmeldelser, kundeantal, »X har brugt Kredithjørnet«, medielogoer.

## Tone

Fundet i teksterne, som de står i dag:
- Sitet taler som et medie: **»vi« = Kredithjørnet**, og læseren er **»du«**. Det er gennemført på alle sider og er sitets eget valg, ikke Thordahls »jeg«-regel. Sprogtjekkets »vi«-fund rettes derfor ikke. (Afhænger af svaret om »redaktionen« ovenfor.)
- Rolig, forklarende, uden bankjargon. Gennemgående ord: »roligt«, »overblik«, »næste skridt«, »forberedt«.
- Eksempler mærkes »Eksempel · illustrativt« og slutter med »Tallene er et konstrueret eksempel, ikke et tilbud.«

## Søgeordskort (som sitet er bygget i dag)

| Side | Søgning |
|---|---|
| `/` | boliglån uafhængig guide |
| `/boliglaan-selvstaendig/` | boliglån selvstændig |
| `/boliglaan-selvstaendig/freelancer/` | boliglån freelancer |
| `/boliglaan-selvstaendig/dokumentation/` | dokumentation boliglån selvstændig |
| `/boliglaan-selvstaendig/nyt-firma/` | boliglån nyt firma |
| `/boliglaan-selvstaendig/svingende-indkomst/` | boliglån svingende indkomst |
| `/boliglaan-selvstaendig/enkeltmandsvirksomhed/` | boliglån enkeltmandsvirksomhed |
| `/boliglaan-selvstaendig/selskab/` | boliglån eget selskab / ApS |
| `/boliglaan-selvstaendig/frivaerdi/` | lån i friværdi selvstændig |
| `/skifte-bank-boliglaan/` | skifte bank boliglån |
| `/skifte-bank-boliglaan/omkostninger/` | hvad koster det at skifte bank |
| `/tjekliste-bankmoede-boliglaan/` | tjekliste bankmøde boliglån |
| `/omlaegge-realkreditlaan/` | omlægge realkreditlån |
| `/omlaegge-realkreditlaan/nedkonvertering/` | nedkonvertering |
| `/omlaegge-realkreditlaan/opkonvertering/` | opkonvertering |
| `/omlaegge-realkreditlaan/beregner/` | konverteringsberegner / opkonvertering beregner |
| `/hvad-er-realkreditlaan/` | hvad er realkreditlån |
| `/bidragssats/` | bidragssats |
| `/raadighedsbeloeb-boliglaan/` | rådighedsbeløb boliglån |
| `/boliglaan-beregner/` | boliglånsberegner |

**[?]** Hvilke sider ranker i dag (Search Console)? Titler og adresser på dem ændres ikke uden dit ja.
