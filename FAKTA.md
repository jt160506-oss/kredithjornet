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
| Juridisk ejer / CVR | Vises ikke nogen steder på sitet | **[?] Hvilket CVR driver sitet? (Thordahl, CVR 46698584, eller et andet?) E-handelsloven § 7 kræver navn, adresse, e-mail og CVR synligt.** |
| Ejer / udgiver | »Jakob«, uafhængig udgiver fra Silkeborg (om-siden, privatlivspolitikken) | ✓ (kilde: Jakob). **[?] Må efternavnet stå på om-siden?** |
| Forfatter på guiderne | »Kredithjørnet-redaktionen« | **[?] Er der flere end dig? Ellers er »redaktionen« et udsagn, der ikke passer helt.** |
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
- Finansieres af affiliate-provision fra samarbejdspartnere. Det koster ikke læseren noget ekstra. ✓ (kilde: Jakob, om-siden)

## Samarbejdspartner

| Felt | Værdi | Status |
|---|---|---|
| Partner | Mybanker A/S | ✓ nævnt på alle sider med knap |
| Hvad Mybanker er | Godkendt boligkreditformidler under tilsyn af Finanstilsynet | ✓ mybanker.dk, sidefod, 14.10.2026 |
| »30+ banker« (forsiden) | Mybanker skriver »samarbejder med 30+ banker og 500+ rådgivere« | ✓ mybanker.dk, 14.10.2026 |
| Mybankers side for boliglån | https://www.mybanker.dk/skift-bank/boliglaan-tilbud/ | ✓ 14.10.2026 |
| Affiliate-netværk | Adtraction | **[?] Er Mybanker-programmet godkendt? Hvad er trackinglinket?** Indtil da peger knapperne direkte på Mybankers side (uden provision), så de ikke er døde. |
| Gratis og uforpligtende hos partneren | Mybanker skriver »gratis og uforpligtende at bruge« | ✓ mybanker.dk, 14.10.2026 |

## Tal og satser, der står på sitet

| Påstand | Hvor | Status |
|---|---|---|
| Realkredit op til 80 % af en helårsbolig | flere guides | ✓ realkreditloven (lånegrænse 80 % for ejerboliger) |
| Udbetaling mindst 5 % »som udgangspunkt« | flere guides | ✓ Finanstilsynet, orienteringsbrev om inspektioner af boliglån (linket på /hvad-er-realkreditlaan/) |
| 80/15/5-modellen | forside, beregner, guides | ✓ som »typisk fordeling« (ikke en regel) |
| Tinglysningsafgift pant: 1.825 kr. + 1,25 % fra 1. januar 2026 | /skifte-bank-boliglaan/omkostninger/ | ✓ skat.dk, nyhedsbrev »Tinglysningsafgift: ny afgiftssats pr. 1. januar 2026« |
| Rådighedsbeløb »i omegnen af 5.000–7.000 kr. for en enlig og 9.000–12.000 kr. for et par« | /raadighedsbeloeb-boliglaan/ | **[?] Ingen kilde. Sekundære kilder (Tænk) nævner ca. 7.250 kr. for enlige og 12.250 kr. for par som Finanstilsynets vejledende minimum. Hvor kommer tallene fra?** |
| Nedkonvertering: »tommelfingerregel omkring 1,5 procentpoint« | omlægning, beregner | ✓ som udbredt tommelfingerregel (ikke en regel), formuleret forsigtigt |
| Startværdier i boliglånsberegneren: realkreditrente 4,0 %, banklånsrente 7,5 %, bidrag 0,65 %, 30 år | /boliglaan-beregner/ | Illustrative antagelser, ikke markedssatser. Står som »illustrative startværdier«. ÅOP vises nu ved siden af. |
| Alle kronebeløb i eksempler | guides | Konstruerede eksempler, mærket som sådan. Ikke kunder eller cases. |

## Påstande, der må bruges

- »Uafhængig«: ingen bank eller långiver ejer eller styrer indholdet (kilde: Jakob).
- »Gratis at bruge«, »uden login«: sitet har ingen konti eller betaling.
- »Beregningen sker i din egen browser«: beregnerne sender intet (✓ koden, 14.10.2026).
- »30+ banker« kun om Mybanker og kun med Mybanker som kilde.

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
