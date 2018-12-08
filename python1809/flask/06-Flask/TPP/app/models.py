from app.ext import db

# 字母模型类
class Letter(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(4))
    # 城市列表
    l_cities = db.relationship('City', backref='letter', lazy=True)

# 城市模型类
class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parentId = db.Column(db.Integer, default=0)
    regionName = db.Column(db.String(100))
    cityCode = db.Column(db.Integer)
    pinYin = db.Column(db.String(40))
    # 关系 【属于哪个字母下】
    c_letter = db.Column(db.Integer, db.ForeignKey(Letter.id))



