from flask import render_template, redirect, url_for, Blueprint, session, flash
from flask_login import current_user, login_user, logout_user, login_required

from booksite.app import db, bcrypt
from booksite.user_handeling.signupForm import SignupForm
from booksite.user_handeling.loginForm import LoginForm
from booksite.user_handeling.models import User

user_handeling = Blueprint('user_handeling', __name__, template_folder='templates')

#login needs to be implemented
@user_handeling.route("/signup", methods=['GET', 'POST'])
def signup_site():
    signup_form = SignupForm()#test crsf
    if signup_form.validate_on_submit():
        #check if there is a user in the database with the picked name
        user = User.query.filter(User.username == signup_form.username.data).first()
        if user:
            flash("Bitte anderen Nutzernamen auswählen")
            return render_template("user_handeling/signup_site.html", form=signup_form)
        hashed_password = bcrypt.generate_password_hash(signup_form.password.data)
        user = User(username=signup_form.username.data, password=hashed_password)
        user.role="user"
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('core.index'))
    return render_template("user_handeling/signup_site.html", form=signup_form)

@user_handeling.route("/login_site", methods=['GET', 'POST'])
def login_site():
    login_form = LoginForm()
    if current_user.is_authenticated:
        flash("Es ist bereits ein Nutzer angemeldet")
        return redirect(url_for('core.index'))

    if login_form.validate_on_submit():
        user = User.query.filter(User.username == login_form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, login_form.password.data):
                session["userRoll"] = user.role
                print(session["userRoll"])

                login_user(user)
                return redirect(url_for('core.index'))
        flash("Kein Nutzer mit diesen Login Daten gefunden")
    return render_template("user_handeling/login_site.html", form=login_form)


@user_handeling.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.index'))