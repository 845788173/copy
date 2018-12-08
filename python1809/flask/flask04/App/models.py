from App.ext import db


# class Person(db.Model):
#     id=db.Column(db.Integer,primary_key=True,autoincrement=True)
#     p_name=db.Column(db.String(30))
#     p_age=db.Column(db.Integer,default=18)
#
#
# class Grade(db.Model):
#     id=db.Column(db.Integer,primary_key=True,autoincrement=True)
#     g_name=db.Column(db.String(20),unique=True)
#     g_students=db.relationship('Student',backref='grade',lazy=True)
#
# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     s_name=db.Column(db.String(20))
#     s_age=db.Column(db.Integer,default=16)
#     s_grade_id=db.Column(db.Integer,db.ForeignKey('grade.id'),nullable=False)

class Animal(db.Model):
    __abstract__=True
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    a_name=db.Column(db.String(16))

class Cat(Animal):
    c_hobby=db.Column(db.String(16))

class Dog(Animal):
    __tablename__='BIGdog'
    d_leg=db.Column(db.Integer,default=4)

class Student(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    s_name=db.Column(db.String(20))
    s_age=db.Column(db.Integer,default=16)
    def model_to_dict(self):
        return {'id':self.id,'name':self.s_name,'age':self.s_age}