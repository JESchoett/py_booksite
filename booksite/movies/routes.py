from flask import render_template, request, redirect, url_for, Blueprint, flash, session
from flask_login import login_required

from sqlalchemy import text

from booksite.app import db

from booksite.movies.models import Movies
from booksite.movies.movieForm import MovieForm

movies = Blueprint('movies', __name__, template_folder='templates')


@movies.route('/')
@login_required
def index():
    print(session["userRoll"])
    if request.method == 'GET':
        if session["userRoll"] == "admin":
            all_movies = Movies.query.all()
        else:
            all_movies = Movies.query.filter(Movies.schlagw != "versteckt").all()
        return render_template("movies/movies_overview.html", all_movies=all_movies)

def addMovieOverForm(movie_form, db):
    # adding a new Movie to the DB
    movie = Movies(autor=movie_form.autor.data, titel=movie_form.titel.data, genre=movie_form.genre.data,
        subgenreRomane=movie_form.subgenreRomane.data, verlag=movie_form.verlag.data, laenge=movie_form.laenge.data,
        isbn=movie_form.isbn.data, jahr=movie_form.jahr.data, preis=movie_form.preis.data, standort=movie_form.standort.data,
        inhaltsangabe=movie_form.inhaltsangabe.data, bemerkungen=movie_form.bemerkungen.data,
        subtitel=movie_form.subtitel.data, subgenreSachbuchRatgeber=movie_form.subgenreSachbuchRatgeber.data,
        subgenreRatgeber=movie_form.subgenreRatgeber.data, auflage=movie_form.auflage.data,
        schlagw=movie_form.schlagw.data, bild=movie_form.bild.data)
    db.session.add(movie)
    db.session.commit()

def alterMovieOverForm(movie, movie_form, db):
    # Update the movie fields with the form
    movie.autor = movie_form.autor.data
    movie.titel = movie_form.titel.data
    movie.genre = movie_form.genre.data
    movie.subgenreRomane = movie_form.subgenreRomane.data
    movie.verlag = movie_form.verlag.data
    movie.laenge = movie_form.laenge.data
    movie.isbn = movie_form.isbn.data
    movie.jahr = movie_form.jahr.data
    movie.preis = movie_form.preis.data
    movie.standort = movie_form.standort.data
    movie.inhaltsangabe = movie_form.inhaltsangabe.data
    movie.bemerkungen = movie_form.bemerkungen.data
    movie.subtitel = movie_form.subtitel.data
    movie.subgenreSachbuchRatgeber = movie_form.subgenreSachbuchRatgeber.data
    movie.subgenreRatgeber = movie_form.subgenreRatgeber.data
    movie.auflage = movie_form.auflage.data
    movie.schlagw = movie_form.schlagw.data
    movie.bild = movie_form.bild.data
    db.session.commit()

@movies.route('/movies_add', methods=['GET', 'POST'])
@login_required
def movies_add():
    print(session["userRoll"])
    if session["userRoll"] != "admin":
        flash("insufficient rights")
        return redirect(url_for('core.index'))
    else:
        movie_form = MovieForm()
        if request.method == 'GET':
            return render_template("movies/movies_add.html", form=movie_form)
        elif request.method == 'POST':
            addMovieOverForm(movie_form=movie_form, db=db)
            return redirect(url_for('core.index'))

@movies.route('/movie_details/<nummer>', methods=['GET', 'POST'])
@login_required
def movie_details(nummer):
    movie = Movies.query.filter(Movies.nummer == nummer).first()
    movie_form = MovieForm(obj=movie)
    if request.method == 'GET':
        return render_template('movies/movies_details.html', movie=movie, form=movie_form)
    elif request.method == 'POST':
        alterMovieOverForm(movie=movie, movie_form=movie_form, db=db)
        return redirect(url_for('core.index'))

@movies.route('/movies_delete/<nummer>', methods=['DELETE'])
@login_required
def movies_delete(nummer):
    movie = Movies.query.filter(Movies.nummer == nummer).first()
    if movie:
        db.session.delete(movie)
        db.session.commit()
        return {f"Movie nr. {nummer} deleted."}, 200
    return {f"ERROR: Movie nr. {nummer} waas not deleted."}, 404
