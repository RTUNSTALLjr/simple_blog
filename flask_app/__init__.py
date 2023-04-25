# __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.secret_key = "youreawizardharry"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flask_app.controllers import blogs_control

