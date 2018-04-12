# Import Flask
from flask import Flask
app = Flask(__name__)

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Config SQLAlchemy
import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_ECHO"] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create db
db = SQLAlchemy(app)

# Import content viewed to user
from application import views
from application.message import views
from application.auth import views

# Import database data models
from application.message import models
from application.auth import models
from application.reply import models

# Logging in
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.setup_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "This feature requires logging in"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Create database tables if required
try:
    db.create_all()
except:
    pass