from App.ext import db


class Letter(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(20))
    l_cities=db.relationship('City',backref='letter',lazy=True)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parentId = db.Column(db.Integer, default=0)
    regionName = db.Column(db.String(100))
    cityCode = db.Column(db.Integer)
    pinYin = db.Column(db.String(40))
    c_letter=db.Column(db.Integer,db.ForeignKey(Letter.id))
class Wheel(db.Model):
    __tablename__ = 'axf_wheel'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    img = db.Column(db.String(100))
    name = db.Column(db.String(100))
    trackid = db.Column(db.String(20))
# 用户模型类
class User(db.Model):
    # 主键
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 用户名
    name = db.Column(db.String(40))
    # 密码
    password = db.Column(db.String(256))
    # 邮箱
    email = db.Column(db.String(20), unique=True)
    # 手机
    phone = db.Column(db.String(20))
    # 令牌
    token = db.Column(db.String(256))
    # 是否删除
    isdelete = db.Column(db.Boolean, default=False)
    # 是否激活
    isactive = db.Column(db.Boolean, default=False)
    # 头像
    icon = db.Column(db.String(40), default='head.png')
    # 等级
    permissions = db.Column(db.Integer, default=1)
