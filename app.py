"""
dependencys im requirements.txt
"""

from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap4
from flask_sqlalchemy import SQLAlchemy

import datetime
#zum Aufruf der .env Datei
import os
from dotenv import load_dotenv

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./buchsammlung.db'
    #get the Bot Token from a .env file
    load_dotenv()
    app.secret_key = os.getenv('APP_SECRET_KEY')

    bootstrap = Bootstrap4(app)
    db.init_app(app)

    from routes import register_routes
    register_routes(app=app, db=db)

    migrate = Migrate(app, db)

    return app



