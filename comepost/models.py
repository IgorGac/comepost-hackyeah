from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(50))
    account_type = db.Column(db.Integer)

class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.Integer)
    item = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    desc = db.Column(db.String(200))
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    value = db.Column(db.Float)
    
