# 📚 Bücher-Funktionen
- Anzeige aller Bücher  {cm:2025-05-19}
- Anzeige nur der nicht versteckten Bücher  {cm:2025-05-19}
- Anlegen eines neuen Buchs  {cm:2025-05-19}
- Bestehendes Buch ändern 
  - Kann ich evtl. die Komplett löschen und nur `book_add.html` verwenden? 
  - Aufnahme aller felder 
  - Bild bei Anpassung aus der Datenbank löschen 
  - ISBN Fetch einbauen 
- Buch löschen   {cm:2025-05-20}
- Buchseiten Styling & Inhalt 
  - `book_overview.html` – Layout und Anzeige prüfen
  - `book_add.html` – Alle Felder vorhanden? Buttons/Validierung prüfen {cm:2025-06-28}
    - bild vom rechner hochladen {cm:2025-06-28}
  - `book_details.html` – Alle Felder anzeigen, inkl. Bildanzeige
    - alle felder
    - styling, wie beim book `book_add.html`
    - funktionen (Anpassung und Löschung)
  - `book_breadcrumb.html` – Pfadnavigation prüfen
- `bookForm.py` prüfen: Validierungen & Defaults   {cm:2025-06-29}
- `routes.py` prüfen: Fehlerbehandlung, Redirects 
  - bei book_add daten einer Bookform behalten, sollte ich auf einen Fehler laufen //TODO
  - sollten die `addBookOverForm` oder `alterBookOverForm` auf fehler laufen, sollte das Bild der Speicherung gelöscht werden {cm:2025-06-29}
- `models.py` prüfen: Felder konsistent mit Formularen?  

# 🎬 Filme-Funktionen
- Anzeige aller Filme #movies 
- Anzeige nur der nicht versteckten Filme #movies 
- Anlegen eines neuen Films #movies 
- Bestehenden Film ändern #movies 
- Film löschen #movies 
- Filmseiten Styling & Inhalt #movies
  - `movies_overview.html` – Übersicht prüfen
  - `movies_add.html` – Formular prüfen
  - `movies_details.html` – Detailanzeige und Bild
- `movieForm.py` prüfen: Defaults & Validatoren #movies 
- `routes.py` prüfen: Fehlerfälle abfangen #movies
- `models.py` prüfen: Felder konsistent mit Formular? #movies 
- `routes_test.py` erstellen/prüfen #movies #tests

# 🖼️ Bilder / Cover
- Bilder hochladen #images
- Bilder speichern (Storage) #images
- Bilder anzeigen in Details-Seite (Bücher & Filme) #images
- Ansicht nur mit Bildern/Cover #images
- `move_file.py` prüfen #images #scripts
- `remove_file.py` prüfen #images #scripts
- Speicherpfad-Struktur (Ordner z. B. `/static/images`) #images #infra

# 🧭 Navigation / Breadcrumbs
- Breadcrumbs implementieren #navigation
  - Zurück zur Buchübersicht #navigation
  - Zurück zur Buchanlage #navigation
  - Zurück zur Buchdetails #navigation
  - Zurück zur Filmübersicht #navigation
  - Zurück zur Filmanlage #navigation
  - Zurück zur Filmdetails #navigation
- `book_breadcrumb.html` korrekt eingebunden? #navigation

# 🔒 Benutzerrechte / Rollen
- "Anlegen"-Button für Nicht-Admins verstecken #auth {cm:2025-05-19}
- Login-/Signup-Flow prüfen (Routing, Redirects) #auth
- Benutzerrollen (Admin/Nutzer) zentral abfragen (Session, Decorator?) #auth
- `login_site.html` – Style & Validierung #auth
- `signup_site.html` – Style & Validierung #auth
- `loginForm.py`, `signupForm.py` – Felder & Validatoren #auth 

# ⚙️ Technische Funktionen
- Erstellung einer Test-Datenbank (`test.db`) #tech {cm:2025-05-19}
- Testabdeckung für alle Routen (Books, Movies, Login) #tech #tests
- `run.py` und `app.py` auf sauberen Einstieg prüfen #tech
- Backup der Datenbank bei Docker-Einsatz #docker
- Check: Bild-Storage funktioniert korrekt? #images 

# 🧪 Extras
- ISBN per Scan aufnehmen #isbn {cm:2025-05-19}
- `isbn_scraping.py` testen & robust machen (Fehlermeldungen, Try/Except) #isbn #scripts {cm:2025-06-28}
- `isbn_scraping.py` umbau zu einem API Call

---

# 📂 Projektstruktur verstehen & nutzen
- Ausgabe der Projektstruktur regelmäßig zur Notizpflege nutzen (`find . -type f \( -name "*.py" -o -name "*.html" \) | grep -v .venv | grep -v migrations > structure.txt`) #overview  {cm:2025-05-19}
- Struktur-Übersicht als Markdown exportieren #doc
