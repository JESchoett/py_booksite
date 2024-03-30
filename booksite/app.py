"""
dependencys im requirements.txt
"""

from flask import Flask, redirect, url_for
from flask_bootstrap import Bootstrap4

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager
from flask_bcrypt import Bcrypt

from flask_wtf.csrf import CSRFProtect

#zum Aufruf der .env Datei
import os
from dotenv import load_dotenv

db = SQLAlchemy()
bcrypt = Bcrypt()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__, template_folder='templates')

    current_dir = os.path.dirname(os.path.abspath('buchsammlung.db'))
    database_file = os.path.join(current_dir, 'instance', 'buchsammlung.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_file

    #get the Sekret key from a .env file
    load_dotenv()
    app.secret_key = os.getenv('APP_SECRET_KEY')

    #test for csrf
    app.config['CSRF_SECRET_KEY'] = 'test for csrf'
    app.config['WTF_CSRF_SECRET_KEY'] = 'test for csrf'

    #init the Database to use it in the app
    db.init_app(app)
    #add Bootstrap
    bootstrap = Bootstrap4(app)

    #logic to setup login
    login_manager = LoginManager()
    login_manager.init_app(app)

    from booksite.user_handeling.models import User
    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(uid)

    @login_manager.unauthorized_handler
    def unauthorize_callback():
        return redirect(url_for('core.index'))

    bcrypt.init_app(app)
    csrf.init_app(app)

    # import and register blueprints
    from booksite.core.routes import core
    from booksite.books.routes import books
    from booksite.movies.routes import movies
    from booksite.user_handeling.routes import user_handeling

    app.register_blueprint(core, url_prefix='/')
    app.register_blueprint(books, url_prefix='/books')
    app.register_blueprint(movies, url_prefix='/movies')
    app.register_blueprint(user_handeling, url_prefix='/user_handeling', bcrypt=bcrypt)

    csrf.exempt(core)
    csrf.exempt(books)
    csrf.exempt(movies)
    csrf.exempt(user_handeling)

    migrate = Migrate(app, db)
    return app



