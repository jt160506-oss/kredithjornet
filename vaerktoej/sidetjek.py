# -*- coding: utf-8 -*-
"""Kvalitetstjek af en faerdig side, maalt mod husets regler i AGENTS.md.

   Brug fra repoets rod:
       python3 vaerktoej/sidetjek.py blog/en-side/index.html [flere filer ...]

   Tjekker: title- og description-laengde, canonical og og-felter, at hver
   JSON-LD-blok kan laeses, antal overskrifter, h2 formuleret som spoergsmaal,
   ord i broedteksten, tomme links, interne links der peger paa en fil der ikke
   findes, billeder uden width/height/alt, fodnoter mod kildelisten, forbudte
   vendinger og antal tankestreger.

   Linjer med OK er i orden. Linjer med !! skal ses efter. Et par af dem kan
   vaere falske alarmer: ordet "studie" i en kildetitel og "vi" i en replik,
   hvor Jakob og kunden er sammen om noget, er begge i orden."""
import json, os, re, sys
from html.parser import HTMLParser

FORBUDT = [r"Den gode nyhed", r"Det er ikke en fjern fremtid", r"en opskrift fra 2015",
           r"fordel at hente", r"gennemtænkt", r"skaber handling",
           r"\bstudie\b", r"\bstudio\b"]
# Kredithjørnet: »vi« og »vores« er sitets egen stemme (se FAKTA.md, Tone).

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.spring = 0           # inde i script/style/svg
        self.i_artikel = False
        self.dybde_artikel = 0
        self.tekst = []
        self.titel = None
        self.i_titel = False
        self.ld = []
        self.i_ld = False
        self.meta = {}
        self.links = []
        self.overskrifter = []
        self.i_overskrift = None
        self.billeder = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style", "svg"):
            if tag == "script" and a.get("type") == "application/ld+json":
                self.i_ld = True
            self.spring += 1
        if tag == "title" and self.spring == 0: self.i_titel = True
        if tag == "meta":
            n = a.get("name") or a.get("property")
            if n: self.meta[n] = a.get("content", "")
        if tag == "link" and a.get("rel") == "canonical": self.meta["canonical"] = a.get("href", "")
        if tag == "a" and "href" in a: self.links.append(a["href"])
        if tag == "img": self.billeder.append((a.get("src", ""), a.get("width"), a.get("height"), a.get("alt")))
        if tag == "article": self.i_artikel = True
    # </article> lukker opsamlingen, saa footeren ikke taeller med.
        if tag in ("h1", "h2", "h3"):
            self.i_overskrift = [tag, ""]
    def handle_endtag(self, tag):
        if tag in ("script", "style", "svg"):
            self.spring = max(0, self.spring - 1); self.i_ld = False
        if tag == "title": self.i_titel = False
        if tag == "article": self.i_artikel = False
        if tag in ("h1", "h2", "h3") and self.i_overskrift:
            self.overskrifter.append((self.i_overskrift[0], self.i_overskrift[1].strip()))
            self.i_overskrift = None
    def handle_data(self, d):
        if self.i_titel: self.titel = (self.titel or "") + d
        if self.i_ld: self.ld.append(d); return
        if self.spring: return
        if self.i_overskrift: self.i_overskrift[1] += d
        if self.i_artikel: self.tekst.append(d)

def tjek(sti):
    raw = open(sti, encoding="utf-8").read()
    p = P(); p.feed(raw)
    print("=" * 68); print(sti); print("=" * 68)
    t = (p.titel or "").strip()
    d = p.meta.get("description", "")
    flag = lambda ok: "OK " if ok else "!! "
    print(flag(50 <= len(t) <= 62) + "title %d tegn: %s" % (len(t), t))
    print(flag(120 <= len(d) <= 165) + "description %d tegn" % len(d))
    print(flag(bool(p.meta.get("canonical"))) + "canonical: %s" % p.meta.get("canonical", "MANGLER"))
    for n in ("og:image", "og:image:width", "og:image:height", "og:title", "og:url", "robots", "author"):
        if n not in p.meta: print("!! mangler meta: " + n)
    # JSON-LD
    typer = []
    for i, blok in enumerate(p.ld):
        try:
            o = json.loads(blok)
            for x in (o if isinstance(o, list) else [o]): typer.append(x.get("@type"))
        except Exception as e:
            print("!! JSON-LD blok %d er ugyldig: %s" % (i + 1, e))
    print(flag(len(typer) >= 2) + "JSON-LD: %s" % ", ".join(str(x) for x in typer))
    # Tekst
    ord_ = re.sub(r"\s+", " ", " ".join(p.tekst)).split()
    print("   brødtekst i <article>: %d ord" % len(ord_))
    h1 = [x for x in p.overskrifter if x[0] == "h1"]
    print(flag(len(h1) == 1) + "h1: %d  ·  h2: %d  ·  h3: %d" % (
        len(h1), len([x for x in p.overskrifter if x[0] == "h2"]),
        len([x for x in p.overskrifter if x[0] == "h3"])))
    sp = [x[1] for x in p.overskrifter if x[0] == "h2" and x[1].endswith("?")]
    print(flag(len(sp) == 0) + "h2 formuleret som spørgsmål: %d %s" % (len(sp), sp if sp else ""))
    # Links
    doede = [l for l in p.links if l.strip() in ("#", "")]
    print(flag(not doede) + "tomme links: %d" % len(doede))
    interne = sorted({l for l in p.links if l.startswith("/") and not l.startswith("//")})
    for l in interne:
        rute = l.split("#")[0].split("?")[0]
        if rute in ("/", ""): continue
        m = rute.lstrip("/")
        findes = os.path.exists(m) or os.path.exists(os.path.join(m, "index.html")) or os.path.exists(m.rstrip("/"))
        if not findes: print("!! internt link uden fil: %s" % l)
    # Billeder
    for src, w, h, alt in p.billeder:
        if not (w and h): print("!! billede uden width/height: %s" % src)
        if alt is None: print("!! billede uden alt: %s" % src)
    # Fodnoter mod kildeliste
    kilder = len(re.findall(r'<li>(?=[^<]*<a )', raw.split('class="sources"')[-1])) if 'class="sources"' in raw else 0
    noter = sorted({int(x) for x in re.findall(r"<sup>\[(\d+)\]</sup>", raw)})
    print(flag(all(n <= max(kilder, 0) for n in noter) if noter else True) +
          "fodnoter %s mod %d kilder med link" % (noter, kilder))
    # Tone
    synlig = " ".join(ord_)
    for f in FORBUDT:
        if re.search(f, synlig, re.I): print("!! forbudt vending i brødtekst: »%s«" % f)
    streger = synlig.count("—")
    print(flag(streger <= 12) + "tankestreger i brødtekst: %d" % streger)

for a in sys.argv[1:]: tjek(a)
