from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

from config import DB_CONNECTION_URI
from routes.routes import routes
from routes.users import users

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize db
SQLAlchemy(app)

# Get routes
app.register_blueprint(routes)
app.register_blueprint(users)
