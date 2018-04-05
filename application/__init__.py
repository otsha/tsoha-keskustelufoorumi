# Import Flask
from flask import Flask
app = Flask(__name__)

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_ECHO"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create db
db = SQLAlchemy(app)

# Import content viewed to user
from application import views
from application.database import views
from application.auth import views

# Import database data models
from application.database import models

# Import authentication models
from application.auth import models

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

# Create database tables
db.create_all()