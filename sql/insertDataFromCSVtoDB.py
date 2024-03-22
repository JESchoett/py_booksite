import csv
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('../../buchsammlung.db')
cursor = conn.cursor()

with open("C:/Zu_Sichern/Junk_Code/Python/py_website/buecher.csv", 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        print(row)  # Print out the row for debugging
        if row['Preis'].isspace() or row['Preis'] == "":
            row['Preis']="0"
        row['Preis'] = float(row['Preis'].replace(",", "."))

        if row['ISBN'].isspace() or row['ISBN'] == "":
            row['ISBN']="0"
        row['ISBN'] = row['ISBN'].strip()

        if row['Format'] != "DVD":
           cursor.execute('''INSERT INTO buecher (Autor, Titel, Genre, SubgenreRomane, Format, Verlag, Seiten, Laenge, ISBN, Jahr, Preis, Standort, Inhaltsangabe, Bemerkungen, Subtitel, SubgenreSachbuchRatgeber, SubgenreRatgeber, Auflage, Schlagw, Bild) VALUES (?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?,?)''',
                          (row['Autor'], row['Titel'], row['Genre'], row['SubgenreRomane'], row['Format'], row['Verlag'], row['Seiten'],row['Laenge'], row['ISBN'], row['Jahr'], row['Preis'], row['Standort'], row['Inhaltsangabe'], row['Bemerkungen'], row['Subtitel'], row['SubgenreSachbuchRatgeber'], row['SubgenreRatgeber'], row['Auflage'], row['Schlagw'], row['Bild']))
        else:
            cursor.execute('''INSERT INTO filme (Autor, Titel, Genre, SubgenreRomane, Format, Verlag, Laenge, ISBN, Jahr, Preis, Standort, Inhaltsangabe, Bemerkungen, Subtitel, SubgenreSachbuchRatgeber, SubgenreRatgeber, Auflage, Schlagw, Bild) VALUES (?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?)''',
                           (row['Autor'], row['Titel'], row['Genre'], row['SubgenreRomane'], row['Format'], row['Verlag'], row['Laenge'], row['ISBN'], row['Jahr'], row['Preis'], row['Standort'], row['Inhaltsangabe'], row['Bemerkungen'], row['Subtitel'], row['SubgenreSachbuchRatgeber'], row['SubgenreRatgeber'], row['Auflage'], row['Schlagw'], row['Bild']))

### Commit changes and close connection
conn.commit()
conn.close()
