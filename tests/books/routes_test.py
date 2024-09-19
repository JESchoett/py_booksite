import unittest

from booksite.app import create_app, db
from booksite.books.models import Book
from booksite.books.routes import book_delete
from booksite.user_handeling.models import User

from flask import session
from flask_login import login_user
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# Helper function to create book data
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
        # Create the app in testing mode, initialize the database
        cls.app = create_app(config_name='testing')
        cls.client = cls.app.test_client()  # Create a test client
        cls.app_context = cls.app.app_context()  # Create an application context
        cls.app_context.push()  # Push the context to activate the app

        # Initialize the database and create tables
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        # Clean up the app context and database at the end of the test suite
        db.session.remove()
        cls.app_context.pop()

    def test_delete_book(self):
        # First, add a book to the database
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