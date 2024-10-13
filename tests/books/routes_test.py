import unittest

from booksite.app import create_app, db
from booksite.books.models import Book
from booksite.books.routes import addBookOverForm, book_delete
from booksite.books.bookForm import BookForm
from booksite.user_handeling.models import User

from flask import session
from flask_login import login_user
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def book_testdata():
    book = Book(autor="autor.data",
        titel="titel.data",
        genre="genre.data",
        subgenreRomane="subgenreRomane.data",
        format="format.data",
        verlag="verlag.data",
        laenge="",
        isbn=9783861087212,
        jahr=2000,
        preis=0.0,
        standort="1_1_1",
        inhaltsangabe="inhaltsangabe.data",
        bemerkungen="bemerkungen.data",
        subtitel="subtitel.data",
        subgenreSachbuchRatgeber="subgenreSachbuchRatgeber.data",
        subgenreRatgeber="subgenreRatgeber.data",
        auflage="auflage.data",
        schlagw="schlagw.data",
        bild="bild.data",
        seiten=123
    )
    return book

class BookRoutesTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app(config_name='testing')
        cls.client = cls.app.test_client()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        cls.app_context.pop()

    def test_add_book(self):
        # Simulate user login
        with self.client:
            response = self.client.post('/login', data=dict(
                username="admin_test",
                password="admin123",
                role = "admin"
            ))
            session["userRoll"] = "admin"
            login_user(User.query.filter_by(username="admin").first())
            book_form = BookForm()
            book = book_testdata()
            book_form.autor.data = book.autor
            book_form.titel.data = book.titel
            book_form.genre.data = book.genre
            book_form.subgenreRomane.data = book.subgenreRomane
            book_form.format.data = book.format
            book_form.verlag.data = book.verlag
            book_form.laenge.data = book.laenge
            book_form.isbn.data = book.isbn
            book_form.jahr.data = book.jahr
            book_form.preis.data = book.preis
            book_form.standort.data = book.standort
            book_form.inhaltsangabe.data = book.inhaltsangabe
            book_form.bemerkungen.data = book.bemerkungen
            book_form.subtitel.data = book.subtitel
            book_form.subgenreSachbuchRatgeber.data = book.subgenreSachbuchRatgeber
            book_form.subgenreRatgeber.data = book.subgenreRatgeber
            book_form.auflage.data = book.auflage
            book_form.schlagw.data = book.schlagw
            book_form.bild.dat = book.bild

            addBookOverForm(book_form=book_form, db=db)
            added_book = Book.query.filter_by(nummer=book.nummer).first()
            self.assertEqual(added_book.nummer, book.nummer)

            db.session.delete(book)

    def test_delete_book(self):
        book = book_testdata()
        db.session.add(book)
        db.session.commit()

        # Simulate user login
        with self.client:
            response = self.client.post('/login', data=dict(
                username="admin_test",
                password="admin123",
                role = "admin"
            ))
            session["userRoll"] = "admin"
            login_user(User.query.filter_by(username="admin").first())

            response = book_delete(book.nummer)
            self.assertEqual(response[1], 200)
            deleted_book = Book.query.filter_by(nummer=book.nummer).first()
            self.assertIsNone(deleted_book)

if __name__ == '__main__':
    unittest.main()