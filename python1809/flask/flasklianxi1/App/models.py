from App.ext import db



class User(db.Model):
    # primary_key 主键
    # autoincrement 自增长
    # default 默认值
    # nullable 是否能为空(默认是False不能为空)
    # unique 唯一
    # db.ForeignKey 外键
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    age = db.Column(db.Integer, default=18)
    tel = db.Column(db.String(20), nullable=True)
    score = db.Column(db.Integer)



class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    g_name = db.Column(db.String(20))
    g_students=db.relationship('Student',backref='grade',lazy=True)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(20))
    s_score = db.Column(db.Integer)
    s_age = db.Column(db.Integer)
    s_grade=db.Column(db.Integer,db.ForeignKey(Grade.id))