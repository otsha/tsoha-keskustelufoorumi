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

# Create database tables
db.create_all()