# -*- coding: utf-8 -*-
"""Sprogtjek af al synlig tekst paa et site, maalt mod husets regler.

   Brug fra repoets rod (Thordahl) eller fra roden af et kundesite:
       python3 vaerktoej/sprogtjek.py            # alle .html-filer under mappen
       python3 vaerktoej/sprogtjek.py side.html  # kun de filer, der naevnes
       python3 vaerktoej/sprogtjek.py --kort     # kun antal pr. fil

   Finder: tankestreger, vi/vores/studie, »ikke X, men Y«, overlines og
   kapitelmaerker, h1/h2 formuleret som spoergsmaal, AI-floskler, absolutte
   loefter og tal i engelsk format. Hver linje er et fund, der skal ses
   efter. Nogle er falske alarmer (fx »vi« i et citat fra en kunde), saa
   laes dem, i stedet for at rette blindt.

   Springer over: intern/, worker/, vaerktoej/, .git/, node_modules/ og
   sider med <meta name="robots" content="noindex">."""
import os, re, sys
from html.parser import HTMLParser

SPRING_MAPPER = {"intern", "worker", "vaerktoej", ".git", "node_modules", ".claude", "reference", "partials"}

# Kredithjørnet: »vi« er sitets egen stemme som medie (se FAKTA.md, Tone).
# Thordahls »jeg«-regel gælder ikke her, saa »vi«-reglen er slaaet fra.
UDEN_REGLER = {"vi/vores", "studie"}

# (navn, regex, forklaring). Regex koeres paa synlig tekst, ikke kode.
REGLER = [
    ("tankestreg", r"—", "Ingen tankestreger i synlig tekst. Brug punktum, komma eller kolon."),
    ("vi/vores", r"\b(vi|vores|os)\b", "Thordahl er én person: »jeg«, aldrig »vi«. (Undtagelse: »vi« om dig og kunden sammen.)"),
    ("studie", r"\b(studie|studio)\b", "Ordet bruges ikke om Thordahl."),
    ("ikke X, men Y", r"\bikke\b[^.!?]{1,60}?,\s*men\b", "Kontrast-vending. Sig det, du mener, direkte."),
    ("floskel", r"\b(banebrydende|skræddersy\w*|i højsædet|sømløs\w*|næste niveau|digital rejse|passion\w*|unikke? løsning\w*|i en verden,? hvor|løft(er)? din\w*|game.?changer|state of the art|one.?stop|helhedsorienter\w*|værdiskabende|innovativ\w*|kvalitet i top|med fokus på kvalitet)\b", "Lyder som en skabelon eller en AI. Skriv det konkrete i stedet."),
    ("absolut løfte", r"\b(garanter\w*|altid øverst|nummer 1 på google|første plads|aldrig nede|går aldrig i stykker|ingen risiko)\b", "Absolutte løfter kan være vildledende. Brug noget, der kan holdes."),
    ("engelsk talformat", r"\b\d{1,3},\d{3}\s?kr|\b\d+\.\d+\s?(m³|m2|m²|kg|km)\b", "Dansk format: 1.300 kr., 1,6 m³."),
]
OVERLINE_KLASSER = re.compile(r'class="[^"]*\b(chapter|eyebrow|overline|kicker|pretitle|pre-title|tagline-top)\b', re.I)

class Laeser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.spring = 0
        self.tekst = []
        self.overskrifter = []
        self.i_h = None
        self.noindex = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style", "svg", "noscript", "template"): self.spring += 1
        if tag == "meta" and (a.get("name") or "").lower() == "robots" and "noindex" in (a.get("content") or ""):
            self.noindex = True
        if tag in ("h1", "h2"): self.i_h = [tag, ""]
        if tag in ("br", "p", "li", "div", "h1", "h2", "h3", "h4", "td", "th", "section", "article"):
            self.tekst.append("\n")
    def handle_endtag(self, tag):
        if tag in ("script", "style", "svg", "noscript", "template"): self.spring = max(0, self.spring - 1)
        if tag in ("h1", "h2") and self.i_h:
            self.overskrifter.append((self.i_h[0], re.sub(r"\s+", " ", self.i_h[1]).strip()))
            self.i_h = None
    def handle_data(self, d):
        if self.spring: return
        self.tekst.append(d)
        if self.i_h: self.i_h[1] += d

def filer(argv):
    navne = [a for a in argv if not a.startswith("--")]
    if navne: return navne
    ud = []
    for rod, mapper, fs in os.walk("."):
        mapper[:] = [m for m in mapper if m not in SPRING_MAPPER]
        for f in fs:
            if f.endswith(".html"): ud.append(os.path.join(rod, f)[2:])
    return sorted(ud)

def tjek(sti, kort):
    raw = open(sti, encoding="utf-8").read()
    p = Laeser(); p.feed(raw)
    if p.noindex: return 0
    linjer = [re.sub(r"[ \t\r\f\v]+", " ", l).strip() for l in "".join(p.tekst).split("\n")]
    linjer = [l for l in linjer if l]
    fund = []
    for navn, rx, hvorfor in REGLER:
        if navn in UDEN_REGLER: continue
        r = re.compile(rx, re.I)
        for l in linjer:
            for m in r.finditer(l):
                s = max(0, m.start() - 45); e = min(len(l), m.end() + 45)
                fund.append((navn, ("…" if s else "") + l[s:e] + ("…" if e < len(l) else "")))
    for tag, t in p.overskrifter:
        if t.endswith("?"): fund.append(("spørgsmål som overskrift", "<%s> %s" % (tag, t)))
    for m in OVERLINE_KLASSER.finditer(raw):
        fund.append(("overline/kapitelmærke", m.group(0)))
    if not fund: return 0
    if kort:
        tael = {}
        for n, _ in fund: tael[n] = tael.get(n, 0) + 1
        print("%-45s %s" % (sti, ", ".join("%s %d" % kv for kv in sorted(tael.items()))))
    else:
        print("=" * 72); print(sti)
        for n, uddrag in fund: print("  !! %-24s %s" % (n, uddrag))
    return len(fund)

if __name__ == "__main__":
    kort = "--kort" in sys.argv
    i_alt = sum(tjek(f, kort) for f in filer(sys.argv[1:]))
    print("\n%d fund i alt." % i_alt if i_alt else "Ingen fund.")
    sys.exit(1 if i_alt else 0)
