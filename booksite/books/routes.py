from flask import render_template, request, redirect, url_for, Blueprint, flash, session
from flask_login import login_required

from sqlalchemy import text

from booksite.app import db

from booksite.books.models import Book
from booksite.books.bookForm import BookForm

books = Blueprint('books', __name__, template_folder='templates')


@books.route('/')
@login_required
def index():
    if request.method == 'GET':
        if session["userRoll"] == "admin":
            all_books = Book.query.all()
        else:
            #all_books = db.session.execute(text('SELECT * FROM buecher WHERE schlagw != "versteckt"'))
            all_books = Book.query.filter(Book.schlagw != "versteckt").all()
        return render_template("books/book_overview.html", all_books=all_books)

def addBookOverForm(book_form, db):
    # adding a new Book to the DB
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

def alterBookOverForm(book, book_form, db):
    # Update the book fields with the form
    book.autor = book_form.autor.data
    book.titel = book_form.titel.data
    book.genre = book_form.genre.data
    book.subgenreRomane = book_form.subgenreRomane.data
    book.format = book_form.format.data
    book.verlag = book_form.verlag.data
    book.laenge = book_form.laenge.data
    book.isbn = book_form.isbn.data
    book.jahr = book_form.jahr.data
    book.preis = book_form.preis.data
    book.standort = book_form.standort.data
    book.inhaltsangabe = book_form.inhaltsangabe.data
    book.bemerkungen = book_form.bemerkungen.data
    book.subtitel = book_form.subtitel.data
    book.subgenreSachbuchRatgeber = book_form.subgenreSachbuchRatgeber.data
    book.subgenreRatgeber = book_form.subgenreRatgeber.data
    book.auflage = book_form.auflage.data
    book.schlagw = book_form.schlagw.data
    book.bild = book_form.bild.data
    db.session.commit()


@books.route('/book_add', methods=['GET', 'POST'])
@login_required
def book_add():
    if session["userRoll"] != "admin":
        flash("insufficient rights")
        return redirect(url_for('core.index'))
    else:
        book_form = BookForm()
        if request.method == 'GET':
            return render_template("books/book_add.html", form=book_form)
        elif request.method == 'POST':
            addBookOverForm(book_form=book_form, db=db)
            return redirect(url_for('core.index'))

@books.route('/book_details/<nummer>', methods=['GET', 'POST'])
@login_required
def book_details(nummer):
    book = Book.query.filter(Book.nummer == nummer).first()
    book_form = BookForm(obj=book)
    if request.method == 'GET':
        return render_template('books/book_details.html', book=book, form=book_form)
    elif request.method == 'POST':
        alterBookOverForm(book=book, book_form=book_form, db=db)
        return redirect(url_for('core.index'))

@books.route('/book_delete/<nummer>', methods=['DELETE'])
@login_required
def book_delete(nummer):
    book = Book.query.filter(Book.nummer == nummer).first()
    if book:
        db.session.delete(book)
        db.session.commit()
        return {f"Book nr. {nummer} deleted."}, 200
    return {f"ERROR: Book nr. {nummer} waas not deleted."}, 404