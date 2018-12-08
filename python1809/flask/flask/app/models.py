from app.ext import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(256))
    token = db.Column(db.String(256))
    isdelte = db.Column(db.Boolean,default=False)


class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40))
    color = db.Column(db.String(20))
    age = db.Column(db.Integer)