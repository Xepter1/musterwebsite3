#!/usr/bin/env python3
"""
Projektseiten-Generator für AIGNER Holzbau.

Liest content/projects.json und erzeugt pro Projekt eine statische Seite
projekt-<slug>.html aus einem gemeinsamen Template.

Dieses Datenmodell (content/projects.json) bildet 1:1 eine spätere
CMS-Collection (z. B. Payload "Projekte") ab — Felder bleiben identisch,
nur die Quelle wechselt von JSON-Datei zu CMS-API.

Aufruf:  python3 build.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
DATA = ROOT / "content" / "projects.json"
SITE = "https://aigner-holzbau.de"

LOGO = (
    '<svg class="logomark" viewBox="0 0 40 40" fill="none" aria-hidden="true">'
    '<rect x="1.5" y="1.5" width="37" height="37" rx="9" stroke="#a3551e" stroke-width="1.5"/>'
    '<path d="M8 27 L20 9 L32 27" stroke="#bd6b2c" stroke-width="2" stroke-linejoin="round"/>'
    '<path d="M13 27 L20 16 L27 27 M20 9 V20" stroke="#a3551e" stroke-width="1.6"/>'
    '<line x1="8" y1="27" x2="32" y2="27" stroke="#bd6b2c" stroke-width="2"/></svg>'
)

ZOOM_IC = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
    'stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3M11 8v6M8 11h6"/></svg>'
)


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render(p, prev, nxt):
    facts = "\n".join(
        f'        <div class="fact"><div class="fl">{esc(f["label"])}</div>'
        f'<div class="fv">{esc(f["value"])}</div></div>'
        for f in p["facts"]
    )
    blocks = []
    for label, key in (("Die Aufgabe", "aufgabe"), ("Unsere Lösung", "loesung"), ("Das Ergebnis", "ergebnis")):
        blocks.append(
            f'      <div class="block reveal">\n'
            f'        <span class="eyebrow">{label}</span>\n'
            f'        <p>{esc(p[key])}</p>\n'
            f'      </div>'
        )
    story = "\n".join(blocks)

    ba = p.get("beforeAfter")
    ba_section = ""
    if ba:
        ba_section = f"""
  <!-- BEFORE / AFTER -->
  <section class="beforeafter">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="eyebrow">Vorher · Nachher</span>
        <h2>Aus alt wird <em>wertvoll.</em></h2>
        <p>{esc(ba.get('caption', ''))}</p>
      </div>
      <div class="ba reveal" aria-label="Vorher-Nachher-Vergleich">
        <img class="ba-after" src="{ba['after']}" alt="Nachher: saniert" />
        <img class="ba-before" src="{ba['before']}" alt="Vorher: Bestand" />
        <span class="ba-tag before">Vorher</span>
        <span class="ba-tag after">Nachher</span>
        <div class="ba-handle"><span class="ba-grip"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 7 3 12l5 5M16 7l5 5-5 5"/></svg></span></div>
        <input class="ba-range" type="range" min="0" max="100" value="50" aria-label="Vergleich Vorher/Nachher verschieben" />
      </div>
    </div>
  </section>
"""

    gal = []
    for n, img in enumerate(p["gallery"], 1):
        gal.append(
            f'      <button class="gal-item span2 reveal" data-full="{img}" aria-label="Bild vergrößern">\n'
            f'        <img src="{img}" alt="{esc(p["title"])} — Ansicht {n}" loading="lazy" />\n'
            f'        <span class="zoom">{ZOOM_IC}</span>\n'
            f'      </button>'
        )
    gallery = "\n".join(gal)

    prev_card = (
        f'      <a class="pnav-card prev" href="projekt-{prev["slug"]}.html">\n'
        f'        <span class="dir">← Vorheriges Projekt</span>\n'
        f'        <span class="nm">{esc(prev["title"])}</span>\n'
        f'      </a>'
    )
    next_card = (
        f'      <a class="pnav-card next" href="projekt-{nxt["slug"]}.html">\n'
        f'        <span class="dir">Nächstes Projekt →</span>\n'
        f'        <span class="nm">{esc(nxt["title"])}</span>\n'
        f'      </a>'
    )

    title = esc(p["title"])
    lead = esc(p["lead"])
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title} — AIGNER Holzbau</title>
<meta name="description" content="{lead}" />
<link rel="canonical" href="{SITE}/projekt-{p['slug']}.html" />
<meta name="theme-color" content="#1b1409" />
<script>(function(){{try{{var t=localStorage.getItem('aigner-theme');if(t&&t!=='holz')document.documentElement.dataset.theme=t;}}catch(e){{}}}})();</script>
<link rel="icon" href="favicon.svg" type="image/svg+xml" />
<meta property="og:type" content="article" />
<meta property="og:locale" content="de_DE" />
<meta property="og:site_name" content="AIGNER Holzbau" />
<meta property="og:title" content="{title} — AIGNER Holzbau" />
<meta property="og:description" content="{lead}" />
<meta property="og:url" content="{SITE}/projekt-{p['slug']}.html" />
<meta property="og:image" content="{SITE}/{p['hero']}" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="preload" href="assets/fonts/fraunces-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/hanken-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="fonts.css">
<link rel="stylesheet" href="projekt.css">
</head>
<body>

<header>
  <div class="wrap nav">
    <a href="index.html" class="brand" aria-label="AIGNER Holzbau Startseite">
      {LOGO}<span>AIGNER</span><b>Holzbau</b>
    </a>
    <div class="nav-right">
      <a href="index.html#projekte" class="back">← Alle Projekte</a>
      <a href="index.html#kontakt" class="btn">Angebot anfragen <span class="arr">→</span></a>
    </div>
  </div>
</header>

<main>
  <!-- HERO -->
  <section class="phero" style="--hero:url('{p['hero']}')">
    <div class="wrap">
      <div class="crumb"><a href="index.html">Start</a> · <a href="index.html#projekte">Projekte</a> · {title}</div>
      <span class="ptag">{esc(p['tag'])} · {esc(p['location'])} · {esc(p['year'])}</span>
      <h1>{title}</h1>
      <p class="lead">{lead}</p>
    </div>
  </section>

  <!-- FACTS -->
  <section class="facts">
    <div class="wrap">
      <div class="facts-grid">
{facts}
      </div>
    </div>
  </section>

  <!-- STORY -->
  <section class="story">
    <div class="wrap">
      <div class="beam-sep" aria-hidden="true"><span class="beam"></span></div>
      <div class="story-grid" style="margin-top:46px">
{story}
      </div>
    </div>
  </section>
{ba_section}
  <!-- GALLERY -->
  <section class="gallery">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="eyebrow">Galerie</span>
        <h2>Bilder vom <em>Projekt</em></h2>
      </div>
      <div class="gal-grid">
{gallery}
      </div>
    </div>
  </section>

  <!-- NEXT / PREV -->
  <section class="pnav">
    <div class="wrap">
      <div class="pnav-grid">
{prev_card}
{next_card}
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="cta">
    <div class="wrap">
      <h2>Planen Sie <em>Ähnliches?</em></h2>
      <p>Erzählen Sie uns von Ihrem Vorhaben — wir melden uns innerhalb von 24 Stunden mit einer ehrlichen ersten Einschätzung.</p>
      <a href="index.html#kontakt" class="btn">Projekt besprechen <span class="arr">→</span></a>
    </div>
  </section>
</main>

<!-- Farbwelt-Umschalter (Materialvorschau) -->
<div class="theme-switch" role="group" aria-label="Materialwelt wählen">
  <span class="theme-switch__label">Materialwelt</span>
  <button type="button" class="tsw tsw-holz" data-theme-set="holz" aria-label="Holz & Espresso" aria-pressed="true"><i></i></button>
  <button type="button" class="tsw tsw-schiefer" data-theme-set="schiefer" aria-label="Schiefer & Kupfer" aria-pressed="false"><i></i></button>
  <button type="button" class="tsw tsw-kalk" data-theme-set="kalk" aria-label="Kalk & Eiche" aria-pressed="false"><i></i></button>
</div>

<footer>
  <div class="wrap">
    <span>© <span id="yr"></span> AIGNER Holzbau GmbH</span>
    <span class="links"><a href="index.html#projekte">Projekte</a><a href="impressum.html">Impressum</a><a href="datenschutz.html">Datenschutz</a><a href="index.html">Startseite</a></span>
  </div>
</footer>

<!-- LIGHTBOX -->
<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Bildansicht" aria-hidden="true">
  <div class="lb-stage">
    <button class="lb-btn lb-close" id="lbClose" aria-label="Schließen">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg>
    </button>
    <button class="lb-btn lb-prev" id="lbPrev" aria-label="Vorheriges Bild">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18 9 12l6-6"/></svg>
    </button>
    <button class="lb-btn lb-next" id="lbNext" aria-label="Nächstes Bild">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
    </button>
    <figure class="lb-figure">
      <img id="lbImg" src="" alt="" />
      <figcaption class="lb-cap"><span></span><span class="count" id="lbCount"></span></figcaption>
    </figure>
  </div>
</div>

<script src="projekt.js"></script>
</body>
</html>
"""


def main():
    projects = json.loads(DATA.read_text(encoding="utf-8"))
    n = len(projects)
    for i, p in enumerate(projects):
        prev = projects[(i - 1) % n]
        nxt = projects[(i + 1) % n]
        out = ROOT / f"projekt-{p['slug']}.html"
        out.write_text(render(p, prev, nxt), encoding="utf-8")
        print(f"  ✓ {out.name}")
    print(f"{n} Projektseiten erzeugt.")


if __name__ == "__main__":
    main()
