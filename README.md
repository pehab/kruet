# KRÜT — BlackCore aus Meißen

Statische Bandwebsite für https://kruet-band.de/. HTML und CSS ohne Framework,
Build-Schritt, JavaScript, externe Schriftarten, Tracker oder eingebettete Player.

## GitHub Pages aktivieren

1. Ein Repository anlegen und den Inhalt dieses Ordners auf `main` hochladen.
   Die Ordner `.github` und `site` müssen im Repository-Hauptverzeichnis liegen.
   Mit GitHub Free muss das Repository öffentlich sein. Private Repositories
   benötigen für GitHub Pages einen passenden kostenpflichtigen GitHub-Tarif.
   Ein privates Repository macht die Website selbst nicht privat.
2. Unter **Settings → Pages → Build and deployment → Source** `GitHub Actions` wählen.
3. Unter **Custom domain** `kruet-band.de` setzen. Die Datei `site/CNAME` dokumentiert
   ebenfalls die Domain; bei Actions ist die Einstellung in GitHub maßgeblich.
4. Im persönlichen GitHub-Konto unter **Settings → Pages** die Domain möglichst
   zuerst per GitHub-vorgegebenem TXT-Eintrag verifizieren.
5. In der zuständigen DNS-Zone bei INWX folgende Einträge setzen, sofern die
   Domain die INWX-Nameserver verwendet. INWX kann den Hostnamen als vollständigen
   Namen oder relativ zur Zone anzeigen; das Ergebnis muss diesen Namen entsprechen:

| Vollständiger Name | Typ | Wert |
| --- | --- | --- |
| kruet-band.de | A | 185.199.108.153 |
| kruet-band.de | A | 185.199.109.153 |
| kruet-band.de | A | 185.199.110.153 |
| kruet-band.de | A | 185.199.111.153 |
| www.kruet-band.de | CNAME | pehab.github.io. |

Der letzte Wert gilt beim Hosting im Konto `pehab`. Bei anderem Kontoinhaber
anpassen. TTL z. B. 3600 Sekunden. Bestehende widersprüchliche Website-A/AAAA-
oder www-CNAME-Einträge ersetzen. MX, Mail-TXT und andere Mail-Einträge erhalten.
Die Nameserver müssen nicht gewechselt werden.

6. Der Einrichtungscommit mit `[skip pages]` prüft die Dateien, veröffentlicht aber noch nichts. Nach der
   Pages-Aktivierung: **Actions → Publish band website
   → Run workflow** ausführen. Nach erfolgreichem DNS-Check **Enforce HTTPS** setzen.
   Alle späteren Pushes auf `main` prüfen und veröffentlichen automatisch.
   DNS-Änderungen und Zertifikatsausstellung können bis zu 24 Stunden dauern.
   Danach auch https://www.kruet-band.de/ und die Weiterleitung kontrollieren.

Quellen: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
und https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

## Lokal ansehen

Im Repository-Hauptverzeichnis `python3 -m http.server 8080 --directory site`
starten, dann http://localhost:8080 öffnen. Alternativ `site/index.html` öffnen.

## Prüfung

`python3 scripts/check_site.py` prüft lokale Dateiverweise, Sprungmarken,
Bildbeschreibungen und grundlegende HTML-Struktur. Der Check läuft auch in Actions.

## Inhalte ändern

- Texte, Besetzung, Social-Links, Termine: `site/index.html`.
- Design und responsive Layouts: `site/styles.css`.
- Rechtliche Angaben: `site/impressum.html` und `site/datenschutz.html`.
- Bilder: `site/assets/`. WebP-Dateien aus den fünf bereitgestellten Originalen;
  Bildmetadaten werden beim Export nicht übernommen. M./P./L. entsprechen der
  Bildzuordnung auf der bisherigen Website.
- Neue Termine: den Hinweis im Abschnitt `id="live"` durch echte Termine ersetzen.
- Ein Push auf `main` veröffentlicht automatisch den aktuellen Stand.

## Vor der öffentlichen Freischaltung

- Name und Anbieteranschrift wurden mit ausdrücklicher Freigabe des Inhabers
  aus der bisherigen Website übernommen. Bei Änderungen beide rechtlichen Seiten aktualisieren.
- Foto-/Logorechte und eventuelle Fotografen-Nennung prüfen; die Vorlage nennt KRÜT.
- Datenschutz ist auf das geplante GitHub-Pages-Hosting angepasst und als Entwurf
  zu prüfen, insbesondere Anbieterrollen und Grundlage einer Übermittlung in die USA.
- Gmail bleibt Kontaktanbieter. Bei Wechsel des Postfachs Datenschutzhinweise ändern.
- Es wurden keine Auftritte, Veröffentlichungen oder Musikdateien erfunden.
  YouTube und Instagram entsprechen den Links der bisherigen Seite.

## Rechte

Keine Open-Source-Lizenz für Bandname, Fotos, Logo oder Inhalte eingeräumt.
Öffentliches Hosting/Repository bedeutet keine Freigabe zur beliebigen Nachnutzung.
