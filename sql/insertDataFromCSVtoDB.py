import csv
import sqlite3

# Connect to SQLite database
connections = ['../instance/testing.db', '../instance/buchsammlung.db']

for c in connections:
    conn = sqlite3.connect(c)
    cursor = conn.cursor()

    with open('buecher.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            if row['Preis'].isspace() or row['Preis'] == "":
                row['Preis']="0"
            row['Preis'] = float(row['Preis'].replace(",", "."))

            if row['ISBN'].isspace() or row['ISBN'] == "":
                row['ISBN']="0"
            row['ISBN'] = row['ISBN'].strip()

            if row['Format'] != "DVD":
               cursor.execute('''INSERT INTO buecher (Autor, Titel, Genre, SubgenreRomane, Format, Verlag, Seiten, Laenge, ISBN, Jahr, Preis, Standort, Inhaltsangabe, Bemerkungen, Subtitel, SubgenreSachbuchRatgeber, SubgenreRatgeber, Auflage, Schlagw, Bild) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                              (row['Autor'], row['Titel'], row['Genre'], row['SubgenreRomane'], row['Format'], row['Verlag'], row['Seiten'],row['Laenge'], row['ISBN'], row['Jahr'], row['Preis'], row['Standort'], row['Inhaltsangabe'], row['Bemerkungen'], row['Subtitel'], row['SubgenreSachbuchRatgeber'], row['SubgenreRatgeber'], row['Auflage'], row['Schlagw'], row['Bild']))
            elif row['Format'] == "DVD":
                cursor.execute('''INSERT INTO movies (Autor, Titel, Genre, SubgenreRomane, Format, Verlag, Laenge, ISBN, Jahr, Preis, Standort, Inhaltsangabe, Bemerkungen, Subtitel, SubgenreSachbuchRatgeber, SubgenreRatgeber, Auflage, Schlagw, Bild) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                               (row['Autor'], row['Titel'], row['Genre'], row['SubgenreRomane'], row['Format'], row['Verlag'], row['Laenge'], row['ISBN'], row['Jahr'], row['Preis'], row['Standort'], row['Inhaltsangabe'], row['Bemerkungen'], row['Subtitel'], row['SubgenreSachbuchRatgeber'], row['SubgenreRatgeber'], row['Auflage'], row['Schlagw'], row['Bild']))

            cursor.execute('''INSERT INTO users (username, password, role) VALUES (?,?,?)''',
                           ('admin','$2b$12$5gfS/2UDZVhsmggWX1aalefToHv6UOqLj/57cCQofMiw0qpIJfeg2','admin'))
            cursor.execute('''INSERT INTO users (username, password, role) VALUES (?,?,?)''',
                           ('test','$2b$12$IZLS7uZe02L.6zNsB/d7ZevpOlKvZ.8gVRPeIqJMuR.Ga34wkbqzu','user'))

### Commit changes and close connection
conn.commit()
conn.close()
