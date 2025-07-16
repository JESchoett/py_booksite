# 📚 Bücher-Funktionen
- Anzeige aller Bücher {cm:2025-05-19}
- Anzeige nur der nicht versteckten Bücher  {cm:2025-05-19}
- Anlegen eines neuen Buchs {cm:2025-05-19}
- Bestehendes Buch ändern {cm:2025-07-05}
- Buch löschen   {cm:2025-05-20}

- Buchseiten Styling & Inhalt {cm:2025-07-16}
  - `book_overview.html` – Layout und Anzeige prüfen {cm:2025-07-16}
  - `book_add.html` – Alle Felder vorhanden? Buttons/Validierung prüfen {cm:2025-06-28}
    - bild vom rechner hochladen {cm:2025-06-28}
  - `book_details.html` – Alle Felder anzeigen, inkl. Bildanzeige Anzeige
    - funktionen {cm:2025-07-16}
      - Anpassung {cm:2025-07-16}
      - Löschung {cm:2025-07-16}
      - Fetch von ISBN Daten {cm:2025-07-16}

# 🎬 Filme-Funktionen
- Anzeige aller Filme {cm:2025-07-15}
- Anzeige nur der nicht versteckten Filme  {cm:2025-07-15}
- Anlegen eines neuen Films  {cm:2025-07-15}
- Bestehenden Film ändern {cm:2025-07-16}
- Film löschen {cm:2025-07-16}
- Filmseiten Styling & Inhalt
  - `movies_overview.html` – Übersicht prüfen {cm:2025-07-16}
  - `movies_add.html` – Formular prüfen {cm:2025-07-16}
  - `movies_details.html` – Detailanzeige und Bild Anzeige
- `movieForm.py` prüfen: Defaults & Validatoren {cm:2025-07-15}
- `routes.py` prüfen: Fehlerfälle abfangen
- `models.py` prüfen: Felder konsistent mit Formular? {cm:2025-07-15}

# 🔒 Benutzerrechte / Rollen
- "Anlegen"-Button für Nicht-Admins verstecken {cm:2025-05-19}
- Login-/Signup-Flow prüfen (Routing, Redirects)  {cm:2025-07-16}
- Benutzerrollen (Admin/Nutzer) zentral abfragen (Session, Decorator?)  {cm:2025-07-16}
- `login_site.html` – Style & Validierung {cm:2025-07-16}
- `signup_site.html` – Style & Validierung {cm:2025-07-16}
- `loginForm.py`, `signupForm.py` – Felder & Validatoren {cm:2025-07-16}


# 🧪 Book fetching
- ISBN per Scan aufnehmen {cm:2025-05-19}
- `isbn_scraping.py` testen & robust machen (Fehlermeldungen, Try/Except)
  Send a request to ISBN.de to validate my usage of theyr site {cm:2025-07-12}
- `isbn_scraping.py` umbau zu einem API Call
