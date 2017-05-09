"""
maisie-info/db.py
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/maisie_info.db'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB = SQLAlchemy(APP)


class Content(DB.Model):
    index = DB.Column(DB.Integer, primary_key=True)
    subtitle = DB.Column(DB.String(140), unique=False)
    category = DB.Column(DB.String(140), unique=True)
    text = DB.Column(DB.String(500), unique=True)

    def __init__(self, subtitle, category, text):
        self.subtitle = subtitle
        self.category = category
        self.text = text

    def __repr__(self):
        return '<Content %r>' % self.subtitle


DB.create_all()
