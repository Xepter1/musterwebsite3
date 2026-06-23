# AIGNER Holzbau — Muster-Referenz

Fiktive Premium-Zimmerei aus Niederbayern. Doppelter Zweck:
1. **Portfolio-Stück** für xepoter.de
2. **Wiederverwendbares Branchen-Template** — Basis, die du an echte Handwerker (Zimmerei, Dachdecker, Holzbau) verkaufst.

## Starten
Lokal mit einem statischen Server öffnen (wegen der Unterseiten & Fonts), z. B.:
```bash
python3 -m http.server 8473   # -> http://localhost:8473
```
Keine externen Abhängigkeiten: Die Schriften (Fraunces + Hanken Grotesk) sind **lokal gehostet** (`assets/fonts/`, eingebunden über `fonts.css`) — DSGVO-konform, keine Requests an Google.

## Dateien
- `index.html` — die Hauptseite (HTML/CSS/JS inline)
- `projekt-<slug>.html` — generierte Projekt-Detailseiten (nicht von Hand editieren)
- `content/projects.json` — Content-Modell der Projekte (= spätere CMS-Collection)
- `build.py` — Generator: `python3 build.py` erzeugt die Projektseiten aus der JSON
- `projekt.css`, `projekt.js` — Styling + Galerie-Lightbox der Projektseiten
- `impressum.html`, `datenschutz.html` — Rechtsseiten (Mustertexte, vor Echteinsatz prüfen lassen)
- `fonts.css` — `@font-face` für die lokalen Schriften
- `legal.css` — gemeinsames Stylesheet der Rechtsseiten
- `favicon.svg` — Favicon (basiert auf dem Dachstuhl-Logo)
- `assets/` — Web-Fotos + `assets/fonts/` · `assets/_full/` = Original-Fotos (nur Quelle)
- `Projektdoku.md` — Projektdokumentation

> **Projektseiten ändern:** `content/projects.json` anpassen → `python3 build.py` → fertig.

## Brand-Eckdaten (fiktiv – frei anpassbar)
- Name: **AIGNER Holzbau**, Meisterbetrieb seit 1989, Landshut / Niederbayern
- Inhaber: Martin Aigner, Zimmermeister
- Akzentfarbe: Säge-Ocker `#bd6b2c` · Dunkel: Espresso `#1b1409` · Hell: Knochen-Beige `#f1e9da`

## Echte / AI-Fotos einsetzen (nano-banana etc.)
Die Projekt-Kacheln nutzen aktuell Holz-Farbverläufe als Platzhalter. So tauschst du sie gegen Fotos:

Im `<style>`-Block die Klassen `.p1`–`.p5` ersetzen, z. B.:
```css
.p1{--ph:url("assets/wohnhaus-isarhang.jpg") center/cover}
```
Das `--ph` ist die Hintergrund-Variable jeder Kachel — Verlauf raus, Bild rein, fertig. Der dunkle Verlauf für die Textlesbarkeit liegt automatisch darüber.

**Empfohlene Motive für nano-banana:** Dachstuhl von unten (Sichtsparren), Holzrahmen-Rohbau, fertige Holzfassade in Lärche, Zimmerer bei der Montage, Carport, sanierter Dachstuhl im Altbau. Querformat, warmes Licht.

Optional auch die beiden großen SVG-Zeichnungen (Hero-Karte + „Über uns") gegen Fotos tauschen — die Architektur-Linien sind aber bewusst das unverwechselbare Markenzeichen.

## Struktur der Seite
Header · Hero (mit gezeichnetem Dachstuhl-Tragwerk) · Leistungs-Marquee · 6 Leistungen · Projekt-Galerie · Warum Holz · Ablauf in 4 Schritten · Über uns · Kennzahlen · Stimmen · **Karriere/Jobs** (Recruiting-Argument!) · Kontaktformular · Footer.

## Als Template wiederverwenden
Für den nächsten Kunden: Farben (`:root`-Variablen), Texte und Logo (das `<svg class="logomark">`) tauschen. Gerüst, Animationen und Layout bleiben.

---

## Deployment (Docker / Portainer)

Statische Seite, ausgeliefert über nginx. Läuft auch auf Raspberry Pi (ARM).

**In Portainer:**
1. *Stacks → Add stack → Repository*
2. Repository URL: `https://github.com/Xepter1/musterwebsite3`
3. Compose path: `docker-compose.yml`
4. *Deploy the stack* — Portainer baut das Image selbst, kein Registry nötig.

Danach erreichbar unter **`http://<raspberry-ip>:8473`**

**Port ändern:** in `docker-compose.yml` die erste Zahl bei `"8473:80"` anpassen (Container-Port 80 bleibt).

**Nach Änderungen:** Code pushen → in Portainer beim Stack *Pull and redeploy* (Häkchen „Re-pull image and rebuild" / „Re-build" setzen).

**Lokal testen:**
```bash
docker compose up -d --build   # -> http://localhost:8473
```

