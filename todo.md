# 📚 Bücher-Funktionen
- Anzeige aller Bücher {cm:2025-05-19}
- Anzeige nur der nicht versteckten Bücher  {cm:2025-05-19}
- Anlegen eines neuen Buchs {cm:2025-05-19}
- Bestehendes Buch ändern {cm:2025-07-05}
- Buch löschen   {cm:2025-05-20}

- Buchseiten Styling & Inhalt
  - `book_overview.html` – Layout und Anzeige prüfen
  - `book_add.html` – Alle Felder vorhanden? Buttons/Validierung prüfen {cm:2025-06-28}
    - bild vom rechner hochladen {cm:2025-06-28}
  - `book_details.html` – Alle Felder anzeigen, inkl. Bildanzeige
    - funktionen
      - Anpassung 
      - Löschung 
      - Fetch von ISBN Daten

# 🎬 Filme-Funktionen
- Anzeige aller Filme #movies {cm:2025-07-15}
- Anzeige nur der nicht versteckten Filme #movies  {cm:2025-07-15}
- Anlegen eines neuen Films #movies  {cm:2025-07-15}
- Bestehenden Film ändern #movies 
- Film löschen #movies
- Filmseiten Styling & Inhalt #movies
  - `movies_overview.html` – Übersicht prüfen
  - `movies_add.html` – Formular prüfen
  - `movies_details.html` – Detailanzeige und Bild
- `movieForm.py` prüfen: Defaults & Validatoren #movies {cm:2025-07-15}
- `routes.py` prüfen: Fehlerfälle abfangen #movies
- `models.py` prüfen: Felder konsistent mit Formular? #movies {cm:2025-07-15}

# 🔒 Benutzerrechte / Rollen
- "Anlegen"-Button für Nicht-Admins verstecken #auth {cm:2025-05-19}
- Login-/Signup-Flow prüfen (Routing, Redirects) #auth
- Benutzerrollen (Admin/Nutzer) zentral abfragen (Session, Decorator?) #auth
- `login_site.html` – Style & Validierung #auth
- `signup_site.html` – Style & Validierung #auth
- `loginForm.py`, `signupForm.py` – Felder & Validatoren #auth


# 🧪 Book fetching
- ISBN per Scan aufnehmen #isbn {cm:2025-05-19}
- `isbn_scraping.py` testen & robust machen (Fehlermeldungen, Try/Except) #isbn #scripts
  Send a request to ISBN.de to validate my usage of theyr site {cm:2025-07-12}
- `isbn_scraping.py` umbau zu einem API Call
