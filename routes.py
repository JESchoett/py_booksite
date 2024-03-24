from flask import render_template, request
from sqlalchemy import text

import datetime

#classes
from models import Book, Film
from loginForm import LoginForm
from bookForm import BookForm

def register_routes(app, db):

    @app.route('/')
    def index():
        currentYear = datetime.datetime.now().year
        return render_template('index.html', currentYear=currentYear)

    #login needs to be implemented
    @app.route("/login", methods=['GET', 'POST'])
    def login():
        login_form = LoginForm()
        if login_form.validate_on_submit():
            if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
                return render_template("success.html")
            else:
                return render_template("denied.html")
        return render_template("login.html", form=login_form)

    @app.route('/book_overview')
    def book_overview():
        if request.method == 'GET':
            all_books = Book.query.all()
            return render_template("book_overview.html", all_books=all_books)

    @app.route('/book_add', methods=['GET', 'POST'])
    def book_add():
        book_form = BookForm()
        if request.method == 'GET':
            all_books = Book.query.all()
            return render_template("book_add.html", all_books=all_books, form=book_form)
        elif request.method == 'POST':
            book = Book(Autor = book_form.autor.data, Titel = book_form.titel.data, Genre = book_form.genre.data, SubgenreRomane = book_form.subgenre_romane.data,
                        Format = book_form.format.data, Verlag = book_form.verlag.data, Laenge = book_form.laenge.data,
                        Seiten = book_form.seiten.data, ISBN = book_form.isbn.data, Jahr = book_form.jahr.data,
                        Preis = book_form.preis.data, Standort = book_form.standort.data, Inhaltsangabe = book_form.inhaltsangabe.data,
                        Bemerkungen = book_form.bemerkungen.data, Subtitel = book_form.subtitel.data,
                        SubgenreSachbuchRatgeber = book_form.subgenre_sachbuch_ratgeber.data, SubgenreRatgeber = book_form.subgenre_ratgeber.data,
                        Auflage = book_form.auflage.data, Schlagw = book_form.schlagw.data, Bild = book_form.bild.data)

            db.session.add(book)
            db.session.commit()
            return render_template('index.html')
