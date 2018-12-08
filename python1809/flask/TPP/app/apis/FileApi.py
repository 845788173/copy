import os

from flask_restful import Resource, marshal_with, fields, reqparse
from werkzeug.datastructures import FileStorage

# 请求参数 定制
from werkzeug.utils import secure_filename

from app.ext import db
from app.models import User
from app.settings import BASE_DIR, UPLOAD_RID
from app.tools import format_response

parser = reqparse.RequestParser()
parser.add_argument('token', type=str, required=True, help='请填写token')
parser.add_argument('img', type=FileStorage, location='files', required=True, help='请选择头像img')

class IconForm(fields.Raw):
    def format(self, value):
        return '/static/img/' + value

user_fileds = {
    'icon': IconForm(attribute='icon'),
}

result_fields = {
    'msg': fields.String,
    'status': fields.Integer,
    'time': fields.String,
    'err': fields.String(default=''),
    'data': fields.Nested(user_fileds, default='')
}


class UploadHeadFile(Resource):
    @marshal_with(result_fields)
    def post(self):
        parse = parser.parse_args()
        token = parse.get('token')

        user = User.query.filter(User.token == token).first()

        # 图片数据
        img_file = parse.get('img')
        # 图片名称
        img_name = '%d-%s' % (user.id, secure_filename(img_file.filename))
        # 文件路径
        # upload_dir = os.path.join(BASE_DIR, 'static/img/')
        # print(upload_dir)
        img_file_path = os.path.join(UPLOAD_RID, img_name)
        print(img_file_path)
        # 保存文件
        img_file.save(img_file_path)

        # 更新用户信息
        user.icon = img_name
        db.session.add(user)
        db.session.commit()

        return format_response(msg='头像上传成功', status=200, data=user)