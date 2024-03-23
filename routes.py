from flask import render_template
from sqlalchemy import text

import datetime

#classes
from LoginForm import LoginForm
from models import Book, Film

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


    #db conncetion nis not tested
    @app.route('/book_overview')
    def book_overview():
        result = db.session.execute(text('select * from buecher'))
        all_books = result.scalars()
        return render_template("book_overview.html", all_books=all_books)