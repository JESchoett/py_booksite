"""
dependencys im requirements.txt
"""

from flask import Flask, render_template, current_app, g
from flask_bootstrap import Bootstrap

import datetime

#Import Classes
from __init__ import create_app
from db import get_db, close_db
from LoginForm import LoginForm


@app.route('/')
def index():
    currentYear = datetime.datetime.now().year
    return render_template('index.html', currentYear=currentYear)

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)

@app.route('/book_overview', methods=["GET", "POST"])
def book_overview():
    try:
        db = get_db()
        book_list = db.execute('''Select * from buecher''')
        print(book_list)
        return render_template('book_overview.html', book_list=book_list)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


if __name__ == "__main__":
    app=create_app()
    Bootstrap(app)
    app.run(debug=True)