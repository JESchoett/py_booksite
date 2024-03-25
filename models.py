from flask_login import UserMixin

from app import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String)

    def __repr__(self):
        return f'<User: {self.username}, Role: {self.role}>'

    def get_id(self):
        return self.uid

class Movies(db.Model):
    __tablename__ = 'movies'

    nummer = db.Column(db.Integer, primary_key=True, autoincrement=True)
    autor = db.Column(db.Text(100), nullable=False)
    titel = db.Column(db.Text(100), nullable=False)
    genre = db.Column(db.Text(100))
    subgenreRomane = db.Column(db.Text(100))
    format = db.Column(db.Text(100))
    verlag = db.Column(db.Text(100))
    laenge = db.Column(db.Text(10))
    isbn = db.Column(db.Text(15))
    jahr = db.Column(db.Integer)
    preis = db.Column(db.Float)
    standort = db.Column(db.Text(100))
    inhaltsangabe = db.Column(db.Text(2500))
    bemerkungen = db.Column(db.Text(2500))
    subtitel = db.Column(db.Text(100))
    subgenreSachbuchRatgeber = db.Column(db.Text(100))
    subgenreRatgeber = db.Column(db.Text(100))
    auflage = db.Column(db.Integer)
    schlagw = db.Column(db.Text(100))
    bild = db.Column(db.Text(250))

    def __repr__(self):
        return self

class Book(db.Model):
    __tablename__ = 'buecher'

    nummer = db.Column(db.Integer, primary_key=True, autoincrement=True)
    autor = db.Column(db.Text(100), nullable=False)
    titel = db.Column(db.Text(100), nullable=False)
    genre = db.Column(db.Text(100))
    subgenreRomane = db.Column(db.Text(100))
    format = db.Column(db.Text(100))
    verlag = db.Column(db.Text(100))
    laenge = db.Column(db.Text(10))
    isbn = db.Column(db.Text(15))
    jahr = db.Column(db.Integer)
    preis = db.Column(db.Float)
    standort = db.Column(db.Text(100))
    inhaltsangabe = db.Column(db.Text(2500))
    bemerkungen = db.Column(db.Text(2500))
    subtitel = db.Column(db.Text(100))
    subgenreSachbuchRatgeber = db.Column(db.Text(100))
    subgenreRatgeber = db.Column(db.Text(100))
    auflage = db.Column(db.Integer)
    schlagw = db.Column(db.Text(100))
    bild = db.Column(db.Text(250))

    seiten = db.Column(db.Integer)

    def __repr__(self):
        return self
