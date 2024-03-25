from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import login_required

from booksite.app import db
from booksite.movies.models import Movies

movies = Blueprint('movies', __name__, template_folder='templates')


@movies.route('/movie_overview')
@login_required
def movie_overview():
    if request.method == 'GET':
        all_movies = Movies.query.all()
        return render_template("movies/movie_overview.html", all_movies=all_movies)