import unittest
from booksite.app import create_app, db
from booksite.movies.models import Movies

class MovieTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_movie_deletion(self):
        # Add a test movie
        movie = Movies(autor="Author", titel="Test Movie", nummer=123)
        db.session.add(movie)
        db.session.commit()

        # Now delete the movie via the API
        response = self.client.delete(f'/movies_delete/{movie.nummer}')
        self.assertEqual(response.status_code, 200)

        # Check that the movie is no longer in the database
        deleted_movie = Movies.query.filter_by(nummer=123).first()
        self.assertIsNone(deleted_movie)

if __name__ == '__main__':
    unittest.main()
