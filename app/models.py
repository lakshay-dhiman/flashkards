from os import name
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model
from requests import models
from .database import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), unique=True, nullable = False)
    password = db.Column(db.String(300), nullable=False)
    udeck = db.relationship('Decks', cascade='all, delete-orphan', backref='deck')

class Decks(db.Model):
    __tablename__ = 'decks'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), unique=True, nullable = False)
    user_id = db.Column(db.Integer,  db.ForeignKey('users.id'))
    last_rev = db.Column(db.DateTime(timezone=True), default=func.now())
    count = db.Column(db.Integer, default = 0)
    score = db.Column(db.Integer, default= 0)
    dcard = db.relationship('Cards', cascade='all, delete-orphan', backref='card')

class Cards(db.Model):
    __tablename__ = 'cards'
    front = db.Column(db.String(30))
    back = db.Column(db.String(30))
    id = db.Column(db.Integer, primary_key = True)
    deck_id = db.Column(db.Integer,  db.ForeignKey('decks.id'))

# class Score(db.Model):
#     __tablename__ = 'score'
#     score = db.Column(db.Integer, default= 0)
#     deck_id = db.Column(db.Integer,  db.ForeignKey('decks.id'), primary_key = True)
#     count = db.Column(db.Integer, default = 0)