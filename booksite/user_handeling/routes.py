from flask import render_template, redirect, url_for, Blueprint, session, flash, make_response
from flask_login import current_user, login_user, logout_user, login_required
from booksite.app import db, bcrypt
from booksite.user_handeling.signupForm import SignupForm
from booksite.user_handeling.loginForm import LoginForm
from booksite.user_handeling.models import User

user_handeling = Blueprint('user_handeling', __name__, template_folder='templates')

@user_handeling.route("/signup", methods=['GET', 'POST'])
def signup_site():
    signup_form = SignupForm()
    if signup_form.validate_on_submit():
        user = User.query.filter(User.username == signup_form.username.data).first()
        if user:
            flash("Bitte anderen Nutzernamen auswählen")
            # user already exists (HTTP 409)
            return make_response(render_template("user_handeling/signup_site.html", form=signup_form), 409)

        # Create a new user
        hashed_password = bcrypt.generate_password_hash(signup_form.password.data).decode('utf-8')
        new_user = User(username=signup_form.username.data, password=hashed_password, role="user")

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('core.index'))
    return make_response(render_template("user_handeling/signup_site.html", form=signup_form), 200)

@user_handeling.route("/login_site", methods=['GET', 'POST'])
def login_site():
    login_form = LoginForm()
    if current_user.is_authenticated:
        flash("Es ist bereits ein Nutzer angemeldet")
        return redirect(url_for('core.index')), 302

    # If the form is valid, try to log the user in
    if login_form.validate_on_submit():
        user = User.query.filter(User.username == login_form.username.data).first()

        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            session["userRoll"] = user.role
            login_user(user)
            # Successful login (HTTP 302)
            return redirect(url_for('core.index')), 302

        # Invalid login credentials (HTTP 401)
        flash("Kein Nutzer mit diesen Login-Daten gefunden")
        return make_response(render_template("user_handeling/login_site.html", form=login_form), 401)

    return make_response(render_template("user_handeling/login_site.html", form=login_form), 200)

@user_handeling.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Erfolgreich abgemeldet.")
    # Redirect to the index page (HTTP 302)
    return redirect(url_for('core.index')), 302
