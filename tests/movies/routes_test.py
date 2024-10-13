import unittest

from booksite.app import create_app, db
from booksite.movies.models import Movies
from booksite.movies.routes import movies_delete
from booksite.user_handeling.models import User

from flask import session
from flask_login import login_user
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def movie_testdata():
    movie = Movies(autor="autor.data",
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
        bild="bild.data"
    )
    return movie

class MovieTestCase(unittest.TestCase):
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

    def test_delete_book(self):
        movie = movie_testdata()
        db.session.add(movie)
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

            response = movies_delete(movie.nummer)
            self.assertEqual(response[1], 200)
            deleted_movie = Movies.query.filter_by(nummer=movie.nummer).first()
            self.assertIsNone(deleted_movie)

if __name__ == '__main__':
    unittest.main()
