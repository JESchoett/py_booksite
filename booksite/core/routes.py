from flask import render_template, redirect, url_for, Blueprint, flash, session
from flask_login import current_user

core = Blueprint('core', __name__, template_folder='templates')

@core.route('/')
def index():
    if current_user.is_authenticated:
        user=str(current_user.username)
    else:
        return redirect(url_for('user_handeling.login_site'))

    if session["userRoll"] == "admin":
        return render_template('core/index_admin.html', user=user)
    else:
        return render_template('core/index.html', user=user)