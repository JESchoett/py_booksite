from flask import render_template, request, Blueprint
from flask_login import current_user

import datetime


core = Blueprint('core', __name__, template_folder='templates')


@core.route('/')
def index():
    currentYear = datetime.datetime.now().year

    if current_user.is_authenticated:
        user=str(current_user.username)
    else:
        user="no user is loged in"

    return render_template('core/index.html', currentYear=currentYear, user=user)