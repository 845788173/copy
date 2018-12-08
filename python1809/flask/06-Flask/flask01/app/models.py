from app.ext import db

# 建模
class Wheel(db.Model):
    __tablename__ = 'axf_wheel'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    img = db.Column(db.String(100))
    name = db.Column(db.String(100))
    trackid = db.Column(db.String(20))
