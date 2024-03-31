from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import login_required

from sqlalchemy import text

from booksite.app import db, userRoll

from booksite.books.models import Book
from booksite.books.bookForm import BookForm

books = Blueprint('books', __name__, template_folder='templates')


@books.route('/')
@login_required
def index():
    print(userRoll)
    if request.method == 'GET':
        if userRoll == "admin":
            all_books = Book.query.all()
        else:
            all_books = db.session.execute(text('SELECT * FROM buecher WHERE schlagw != "versteckt"'))
        return render_template("books/book_overview.html", all_books=all_books)

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

@books.route('/book_add', methods=['GET', 'POST'])
@login_required
def book_add():
    book_form = BookForm()
    if request.method == 'GET':
        return render_template("books/book_add.html", form=book_form)
    elif request.method == 'POST':
        changeBookDataOverForm(book_form=book_form, db=db)
        return redirect(url_for('core.index'))

@books.route('/book_details/<nummer>')
@login_required
def book_details(nummer):
    book = Book.query.filter(Book.nummer == nummer).first()
    book_form = BookForm(obj=book)
    if request.method == 'GET':
        return render_template('books/book_details.html', book=book, form=book_form)
    elif request.method == 'POST':
        changeBookDataOverForm(book_form=book_form, db=db)
        return redirect(url_for('core.index'))

@books.route('/book_delete/<nummer>', methods=['DELETE'])
@login_required
def book_delete(nummer):
    Book.query.filter(Book.nummer == nummer).delete()
    db.session.commit()
    return redirect(url_for('core.index'))
