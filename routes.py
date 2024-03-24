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

    def changeBookDataOverForm(book_form, db):
        book = Book(autor=book_form.autor.data, titel=book_form.titel.data, genre=book_form.genre.data,
            subgenreRomane=book_form.subgenreRomane.data, format=book_form.format.data,
            verlag=book_form.verlag.data, laenge=book_form.laenge.data, isbn=book_form.isbn.data,
            jahr=book_form.jahr.data, preis=book_form.preis.data, standort=book_form.standort.data,
            inhaltsangabe=book_form.inhaltsangabe.data, bemerkungen=book_form.bemerkungen.data,
            subtitel=book_form.subtitel.data, subgenreSachbuchRatgeber=book_form.subgenreSachbuchRatgeber.data,
            subgenreRatgeber=book_form.subgenreRatgeber.data, auflage=book_form.auflage.data,
            schlagw=book_form.schlagw.data, bild=book_form.bild.data)

        db.session.add(book)
        db.session.commit()


    @app.route('/book_add', methods=['GET', 'POST'])
    def book_add():
        book_form = BookForm()
        if request.method == 'GET':
            all_books = Book.query.all()
            return render_template("book_add.html", all_books=all_books, form=book_form)
        elif request.method == 'POST':
            changeBookDataOverForm(book_form=book_form, db=db)
            return render_template('index.html')

    @app.route('/book_details/<nummer>')
    def book_details(nummer):
        book = Book.query.filter(Book.nummer == nummer).first()
        book_form = BookForm(obj=book)
        if request.method == 'GET':
            return render_template('book_details.html', book=book, form=book_form)
        elif request.method == 'POST':
            changeBookDataOverForm(book_form=book_form, db=db)
            return render_template('index.html')

    @app.route('/book_delete/<nummer>', methods=['DELETE'])
    def book_delete(nummer):
        Book.query.filter(Book.nummer == nummer).delete()
        db.session.commit()
        return render_template('index.html')
