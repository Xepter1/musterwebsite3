# Projektdokumentation — AIGNER Holzbau (Muster-Referenz)

> Stand: 22.06.2026 · Status: voll ausgebautes Muster mit Farbwelt-System & Premium-Effekten

## 0. Weiterarbeiten / Handoff (z. B. auf einem anderen Rechner)

Claude-Code-Chats sind **lokal pro Gerät** — auf einem neuen Rechner startet die Session frisch. Diese Datei ist der Einstieg: einfach „lies `Projektdoku.md`" sagen.

**Lokal starten**
```bash
python3 -m http.server 8473      # -> http://localhost:8473
```
**Projektseiten neu bauen** (nach Änderung an `content/projects.json`)
```bash
python3 build.py
```

**Dateikarte:** `index.html` (Startseite, CSS/JS inline) · `projekt-<slug>.html` (generiert) · `content/projects.json` + `build.py` (Generator) · `projekt.css`/`projekt.js` · `fonts.css` (+ `assets/fonts/`) · `legal.css` + `impressum.html`/`datenschutz.html` · `favicon.svg`.

**Offene Entscheidung (vom letzten Mal):** Effekt-Pegel — aktuell bewusst *edel-zurückhaltend*. Option, alles **auffälliger** zu drehen (kräftigere Farbwelten, sichtbarere Atmosphäre, größerer Hero-Hingucker). Noch nicht entschieden.

**Mögliche nächste Schritte (aus der Ideenliste):** Signatur-Detail je Gewerk (Dachdecker-Ziegelreihe etc.), Bildoptimierung WebP/srcset, sitemap.xml + 404, echtes Formular-Backend, weitere Vorher/Nachher-Paare (Nanobanana).

## 1. Zweck & Kontext

Fiktive Premium-Zimmerei aus Niederbayern. Das Projekt dient **doppelt**:

1. **Portfolio-/Muster-Stück** für xepter.de (Webdesign-Referenz, die Interessenten überzeugt).
2. **Wiederverwendbares Branchen-Template** — Basis für echte Handwerkskunden (Zimmerei, Dachdecker, Holzbau, allgemeines Handwerk).

Zielgruppe der dargestellten Firma: private Bauherren & Sanierer in Niederbayern + Fachkräfte (Recruiting).

## 2. Technischer Aufbau

- **Eine Datei:** `index.html` — komplettes HTML, CSS (im `<style>`) und JS (im `<script>`) inline. Kein Build, keine Frameworks.
- **Externe Abhängigkeit:** nur Google Fonts (Fraunces + Hanken Grotesk) per CDN.
- **Auslieferung:** statisch über nginx (Docker). Läuft auch auf Raspberry Pi (ARM).
- **Lokaler Dev-Server:** `python3 -m http.server 8473` → http://localhost:8473/

### Verzeichnis
```
index.html              ← die ganze Seite
assets/                 ← optimierte Projektfotos (~0,5 MB, im Web genutzt)
assets/_full/           ← Original-Fotos (~10 MB, NUR Quelle, nicht verlinkt)
Dockerfile · default.conf · docker-compose.yml · .dockerignore   ← Deployment
README.md               ← Setup, Brand-Eckdaten, Deployment-Anleitung
Projektdoku.md          ← dieses Dokument
```

## 3. Design-System (Tokens in `:root`)

- **Farben:** Säge-Ocker `#bd6b2c` (Akzent) · Espresso `#1b1409` (dunkel) · Knochen-Beige `#f1e9da` (hell) · Creme `#faf6ec`.
- **Schrift:** Fraunces (Display/Serif, leichte Schnitte + Italic) · Hanken Grotesk (Body/Sans).
- **Stil-Signatur:** gezeichnete Dachstuhl-/Tragwerk-SVGs mit Strich-Animation (`draw`), Korn-Overlay, warme Verläufe, großzügige Typo.
- **Interaktion:** Scroll-Reveal (IntersectionObserver), Zähler-Animation bei Kennzahlen, Marquee, Header-Scroll-State.

## 4. Seitenstruktur (Reihenfolge)

Header (fixiert) · Hero (mit gezeichnetem Pfettendach) · Leistungs-Marquee · 6 Leistungen · Projekt-Galerie (6 Fotos, Bento-Grid) · Warum Holz (dunkles Band) · Ablauf in 4 Schritten · Über uns (Split + Meister-Stempel) · Kennzahlen-Strip · Stimmen (3 Testimonials) · Karriere/Jobs · Kontaktformular · Footer.

## 5. Brand-Eckdaten (fiktiv, frei anpassbar)

- Name: **AIGNER Holzbau**, Meisterbetrieb seit 1989, Landshut / Niederbayern
- Inhaber: Martin Aigner, Zimmermeister
- Kontakt (fiktiv): Sägewerkstraße 4, 84028 Landshut · servus@aigner-holzbau.de

## 6. Finalisierung — erledigt (21.06.2026)

| # | Punkt | Status |
|---|-------|--------|
| 1 | **Impressum + Datenschutz** als eigene Seiten (`impressum.html`, `datenschutz.html`), im Footer + Formular verlinkt | ✅ erledigt |
| 2 | **Favicon** (`favicon.svg`, Dachstuhl-Logo) + Apple-Touch-Icon | ✅ erledigt |
| 3 | **Open-Graph / Twitter-Meta** inkl. Vorschaubild, Theme-Color, Canonical | ✅ erledigt |
| 4 | **Performance/DSGVO:** Schriften lokal gehostet (latin-Subset, Variable Fonts, ~180 KB), kritische Fonts vorgeladen | ✅ erledigt |
| 5 | **Telefon-Format** vereinheitlicht → `0871 123 45 67` (kein Umbruch im Header) | ✅ erledigt |
| 6 | **Projekt-Galerie:** vollwertige Lightbox (Klick/Tastatur, Pfeile, Esc, Zähler, Fokus-Falle) | ✅ erledigt |
| 7 | **Domain-Konsistenz:** Footer korrigiert auf `xepter.de` | ✅ erledigt |
| 8 | **A11y:** `<main>`-Landmark, Skip-Link, Fokus-Styles, Formular-Labels (`for`/`id`), `aria` an Galerie | ✅ erledigt |
| 9 | **Deployment:** Dockerfile kopiert nun alle neuen Dateien; `.dockerignore` ergänzt | ✅ erledigt |

### Bewusst NICHT geändert
- Bilder bleiben CSS-Hintergründe (`--ph`) → kein `loading="lazy"` nötig; LCP ist der Hero-Text (schnell).
- Die signatur­hafte SVG-Tragwerk-Zeichnung bleibt als Markenzeichen erhalten.

### Vor Echteinsatz für einen realen Kunden
- Impressums-/Datenschutz-Daten ersetzen und **rechtlich prüfen** lassen.
- `og:url`, `canonical` und `og:image` auf die echte Domain setzen (aktuell `aigner-holzbau.de` als Platzhalter).
- Formular an ein echtes Backend / einen Mail-Endpoint anbinden (aktuell nur Frontend-Demo).

## 6b. Ausbaustufe 2 (21.06.2026) — Projektseiten, CMS-Modell, Holz-Details

| Punkt | Status |
|-------|--------|
| **Projekte über Leistungen** platziert (Reihenfolge getauscht) | ✅ |
| **Banner-Stopp beim Hover** entfernt — Marquee läuft durchgehend | ✅ |
| **Eigene Projekt-Detailseiten** (`projekt-<slug>.html`) mit Hero, Eckdaten, Projektbericht (Aufgabe/Lösung/Ergebnis), eigener **Galerie + Lightbox**, Vor/Zurück-Navigation, CTA | ✅ |
| Homepage-Kacheln sind jetzt **Links** in die Projektseiten (statt Einzelbild-Lightbox) | ✅ |
| **Holzbalken-Trenner** (`.beam`) als handwerklicher Abschnittswechsel — CSS-only, mit Maserung + Holznägeln | ✅ |
| Jede Projektseite mit eigenem `<title>`, `description`, Open-Graph, `canonical` → **SEO pro Projekt** | ✅ |

### Architektur der Projektseiten (CMS-fertig)
- **`content/projects.json`** — das Content-Modell. Jedes Objekt = ein Projekt (slug, title, tag, location, year, hero, lead, facts[], aufgabe, loesung, ergebnis, gallery[]). **Dieses Schema bildet 1:1 eine spätere Payload-Collection ab** — beim echten Kundenauftrag wird nur die Quelle (JSON-Datei → CMS-API) getauscht, Template & Felder bleiben.
- **`build.py`** — Generator (nur Dev-Zeit, kein Runtime-Dependency). Liest die JSON, rendert pro Projekt eine statische `projekt-<slug>.html` aus dem Template. Aufruf: `python3 build.py`.
- **`projekt.css` / `projekt.js`** — gemeinsames Styling + Galerie-Lightbox für alle Projektseiten.

### Neues Projekt anlegen
1. Objekt in `content/projects.json` ergänzen (+ Fotos in `assets/`).
2. `python3 build.py` ausführen → neue `projekt-<slug>.html` entsteht.
3. Kachel in `index.html` (Sektion „Projekte") verlinken.

### Bilder (Platzhalter)
Aktuell nutzen Galerien die vorhandenen 6 Fotos gemischt. Später durch **Nanobanana-Pro**-Motive je Projekt ersetzen (Galerie-Pfade in `content/projects.json`, dann `build.py`).

## 6c. Ausbaustufe 3 (21.06.2026) — Conversion-Booster

| Punkt | Status |
|-------|--------|
| **Vorher/Nachher-Schieberegler** (Drag, Touch & Tastatur via `range`-Input; `clip-path`-Technik) — auf der Homepage als eigene Sektion *und* datengesteuert auf Sanierungs-Projektseiten | ✅ |
| **FAQ-Sektion** mit native `<details>`-Akkordeon (barrierefrei, kein JS) — 6 handwerksnahe Fragen, Anker `#faq` | ✅ |

### Vorher/Nachher — Technik & CMS
- Komponente `.ba`: zwei deckungsgleiche Bilder, das obere (`.ba-before`) wird per `clip-path:inset(0 calc(100% - var(--pos)) 0 0)` beschnitten. `--pos` steuert die Trennlinie.
- Bedienung: Pointer-Drag (Maus/Touch) + unsichtbarer `range`-Input für Tastatur/Screenreader.
- **CMS-Feld:** Projekte können optional `beforeAfter: { before, after, caption }` haben (siehe `content/projects.json`, Beispiel: Denkmal-Dachsanierung). `build.py` rendert die Sektion nur, wenn das Feld gesetzt ist.
- Bilder aktuell Platzhalter (vorhandene Fotos) → später echte Vorher/Nachher-Paare (Nanobanana).

## 6d. Ausbaustufe 4 (22.06.2026) — WOW-Effekte & Farbwelt-System

Konzepte aus einer Multi-Agent-Design-Runde (5 Pakete, je adversarial geprüft); nur die geschmackssicheren, bruchfreien Gewinner eingebaut.

### Farbwelt-System (das Verkaufs-Feature)
- **3 Welten** über `data-theme` auf `<html>`: **Holz** (`:root`, Default) · **Schiefer & Kupfer** · **Kalk & Eiche**. Tauscht ~18 Farb-Token → die *ganze* Seite wechselt die Marke, Layout bleibt.
- **Voraussetzung erfüllt:** hartcodierte Dunkel-Flächen tokenisiert (`--on-dark`, `--on-dark-soft`, `--career-bg`, `--on-career`), damit der Wechsel wirklich alles erfasst.
- **FOUC-frei** (Inline-Script im `<head>` setzt Theme vor dem Paint), **localStorage**, **seitenübergreifend** (auch alle Projektseiten), `theme-color`-Meta wird mitgesetzt, `aria-pressed`.
- **Material-Crossfade** beim Wechsel via View-Transitions-API (Progressive Enhancement, reduced-motion-sicher).
- **Umschalter** als dezenter „Materialwelt"-Sampler unten rechts (3 Material-Chips) — bewusst *kein* lauter Header-Switcher (Kritik-Empfehlung), mobil sauber.
- Erweiterbar: neue Welt = ein `html[data-theme="…"]{…}`-Block + ein `.tsw`-Chip. Pitch: „Ihre Farbwelt live."

### Atmosphäre (dunkle Bänder)
- `.band-atmo`-Layer auf „Warum Holz" & Kennzahlen: warme Vignette (Deckenlicht oben, abgedunkelte Ecken) + dezente Holzmaserung-Textur → Tiefe statt flacher Fläche. Nötige z-index/overflow-Fixes gesetzt (`.stats>.wrap`, `position/overflow`).

### Editorial-Glanz
- Geprägte **Sektions-Ziffern** (Wasserzeichen-Versalziffer, `data-index`, text-stroke) auf Leistungen/Ablauf/Stimmen/FAQ.
- **Drop-Cap** im „Über uns"-Leitartikel, **Pull-Quote**-Anführung + **Letterpress-Sterne** in den Stimmen, **kinetische Link-Linie** (`.ulink`).

### Hero & Buttons
- **„bleibt."-Tusche-Reveal**: das kursive Wort schreibt sich per clip-path frei, mit Ember-Unterstrich (vom h1-Fade entkoppelt).
- **Ember-Sheen**: dezenter Licht-Sweep über Buttons beim Hover.

Alle Effekte respektieren `prefers-reduced-motion`, sind CSS-getrieben/performant und nutzen die Tokens.

## 7. Als Template wiederverwenden

Für den nächsten Kunden: `:root`-Farben, Texte und Logo (`<svg class="logomark">`) tauschen. Gerüst, Animationen, Layout bleiben.

## 8. Deployment (Kurzfassung)

Statisch via nginx-Docker. In Portainer als Repo-Stack deployen → erreichbar unter `http://<ip>:8473`. Details in `README.md`.
