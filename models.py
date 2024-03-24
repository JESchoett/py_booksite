from app import db


class Film(db.Model):
    __tablename__ = 'filme'

    Nummer = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Autor = db.Column(db.Text(100), nullable=False)
    Titel = db.Column(db.Text(100), nullable=False)
    Genre = db.Column(db.Text(100))
    SubgenreRomane = db.Column(db.Text(100))
    Format = db.Column(db.Text(100))
    Verlag = db.Column(db.Text(100))
    Laenge = db.Column(db.Text(10))
    ISBN = db.Column(db.Text(15))
    Jahr = db.Column(db.Integer)
    Preis = db.Column(db.Float)
    Standort = db.Column(db.Text(100))
    Inhaltsangabe = db.Column(db.Text(2500))
    Bemerkungen = db.Column(db.Text(2500))
    Subtitel = db.Column(db.Text(100))
    SubgenreSachbuchRatgeber = db.Column(db.Text(100))
    SubgenreRatgeber = db.Column(db.Text(100))
    Auflage = db.Column(db.Integer)
    Schlagw = db.Column(db.Text(100))
    Bild = db.Column(db.Text(250))

    def __repr__(self):
        return self

class Book(db.Model):
    __tablename__ = 'buecher'

    Nummer = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Autor = db.Column(db.Text(100), nullable=False)
    Titel = db.Column(db.Text(100), nullable=False)
    Genre = db.Column(db.Text(100))
    SubgenreRomane = db.Column(db.Text(100))
    Format = db.Column(db.Text(100))
    Verlag = db.Column(db.Text(100))
    Laenge = db.Column(db.Text(10))
    ISBN = db.Column(db.Text(15))
    Jahr = db.Column(db.Integer)
    Preis = db.Column(db.Float)
    Standort = db.Column(db.Text(100))
    Inhaltsangabe = db.Column(db.Text(2500))
    Bemerkungen = db.Column(db.Text(2500))
    Subtitel = db.Column(db.Text(100))
    SubgenreSachbuchRatgeber = db.Column(db.Text(100))
    SubgenreRatgeber = db.Column(db.Text(100))
    Auflage = db.Column(db.Integer)
    Schlagw = db.Column(db.Text(100))
    Bild = db.Column(db.Text(250))

    Seiten = db.Column(db.Integer)

    def __repr__(self):
        return self
