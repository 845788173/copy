from App.ext import db


class Lunbo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image=db.Column(db.String(256))
    def model_to_dict(self):
        return {'id': self.id, 'image': self.image}


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username=db.Column(db.String(40))
    password=db.Column(db.String(60))
    email=db.Column(db.String(150))
    token=db.Column(db.String(256))

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    postid=db.Column(db.String(100))
    title=db.Column(db.String(100))
    image=db.Column(db.String(256))
    duration=db.Column(db.String(100))
    app_fu_title=db.Column(db.String(200))