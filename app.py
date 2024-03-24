"""
dependencys im requirements.txt
"""

from flask import Flask, redirect, url_for
from flask_bootstrap import Bootstrap4

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager
from flask_bcrypt import Bcrypt

import datetime
#zum Aufruf der .env Datei
import os
from dotenv import load_dotenv

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./buchsammlung.db'

    #get the Sekret key from a .env file
    load_dotenv()
    app.secret_key = os.getenv('APP_SECRET_KEY')

    #init the Database to use it in the app
    db.init_app(app)
    #add Bootstrap
    bootstrap = Bootstrap4(app)

    #logic to setup login
    login_manager = LoginManager()
    login_manager.init_app(app)

    from models import User
    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(uid)

    @login_manager.unauthorized_handler
    def unauthorize_callback():
        return redirect(url_for('index'))

    bcrypt = Bcrypt(app)

    #register the routes
    from routes import register_routes
    register_routes(app=app, db=db, bcrypt= bcrypt)

    migrate = Migrate(app, db)

    return app



