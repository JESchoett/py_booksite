from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

from sqlalchemy import text

import datetime

#classes
from models import Book, User
from loginForm import LoginForm
from bookForm import BookForm
from signupForm import SignupForm

def register_routes(app, db, bcrypt):

    @app.route('/')
    def index():
        currentYear = datetime.datetime.now().year

        if current_user.is_authenticated:
            user=str(current_user.username)
        else:
            user="no user is loged in"

        return render_template('index.html', currentYear=currentYear, user=user)

    #login needs to be implemented
    @app.route("/signup", methods=['GET', 'POST'])
    def signup_site():
        signup_form = SignupForm()
        if signup_form.validate_on_submit():
            #check if there is a user in the database with the picked name
            user = User.query.filter(User.username == signup_form.username.data).first()
            if user:
                error = "Username allready taken"
                return render_template("signup_site.html", form=signup_form, error=error)

            hashed_password = bcrypt.generate_password_hash(signup_form.password.data)

            user = User(username=signup_form.username.data, password=hashed_password)

            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))

        return render_template("signup_site.html", form=signup_form)

    #login needs to be implemented
    @app.route("/login_site", methods=['GET', 'POST'])
    def login_site():
        login_form = LoginForm()
        if login_form.validate_on_submit():

            user = User.query.filter(User.username == login_form.username.data).first()

            if bcrypt.check_password_hash(user.password, login_form.password.data):
                login_user(user)
                return redirect(url_for('index'))

        return render_template("login_site.html", form=login_form)

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))



    @app.route('/book_overview')
    @login_required
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
    @login_required
    def book_add():
        book_form = BookForm()
        if request.method == 'GET':
            all_books = Book.query.all()
            return render_template("book_add.html", all_books=all_books, form=book_form)
        elif request.method == 'POST':
            changeBookDataOverForm(book_form=book_form, db=db)
            return redirect(url_for('index'))

    @app.route('/book_details/<nummer>')
    @login_required
    def book_details(nummer):
        book = Book.query.filter(Book.nummer == nummer).first()
        book_form = BookForm(obj=book)
        if request.method == 'GET':
            return render_template('book_details.html', book=book, form=book_form)
        elif request.method == 'POST':
            changeBookDataOverForm(book_form=book_form, db=db)
            return redirect(url_for('index'))

    @app.route('/book_delete/<nummer>', methods=['DELETE'])
    @login_required
    def book_delete(nummer):
        Book.query.filter(Book.nummer == nummer).delete()
        db.session.commit()
        return redirect(url_for('index'))
