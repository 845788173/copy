from flask import Blueprint, request, jsonify

from App.models import *

api=Blueprint('api_blue',__name__,url_prefix='/api/')
@api.route('/students/',methods=['GET','POST'])
@api.route('/students/<int:id>/',methods=['GET','POST','DELETE','PUT'])
def students(id=None):
    if request.method=='GET':
        if id:
            student=Student.query.get(id)
            return jsonify(student.model_to_dict())
        else:

            students=Student.query.all()
            data=[]
            for student in students:
                data.append(student.model_to_dict())
            return jsonify(data=data)
    elif request.method=='POST':
        username=request.form.get('username')
        age=request.form.get('age')
        student=Student()
        student.s_name=username
        student.s_age=age
        db.session.add(student)
        db.session.commit()
        return jsonify(student.model_to_dict())
    elif request.method=='DELETE':
        student=Student.query.get(id)
        db.session.delete(student)
        db.session.commit()
        data={
            'msg':'deletesuccess'
        }
        return jsonify(data)
    elif request.method=='PUT':
        username = request.form.get('username')
        age = request.form.get('age')
        student=Student.query.get(id)
        student.s_age=age
        student.s_name=username
        db.session.add(student)
        db.session.commit
        return jsonify(student.model_to_dict())
