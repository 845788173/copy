import random

from flask_restful import Resource, marshal_with, fields, reqparse

# 请求参数 定制

from app.tools import format_response

parser = reqparse.RequestParser()
parser.add_argument('phone', type=str, required=True, help='请带入手机号')

# 响应参数定制
result_fields = {
    'msg': fields.String,
    'status': fields.Integer,
    'time': fields.String,
    'err': fields.String(default='')
}


'''
AppID: 1400112809
AppKey: 8d8b808cb9073023631d241951f49fb4
# 短信正文id
template_id: 166915
# 签名 名字
sms_sign: 钟远智工作经验分享


# 正文模板
短信验证码: {1}，请于{2}分钟内填写。如非本人操作，请忽略本短信。
'''

from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
class SMSResource(Resource):
    def get(self):
        parse = parser.parse_args()
        phone = parse.get('phone')

        appid = 1400112809
        appkey = '8d8b808cb9073023631d241951f49fb4'
        template_id = 166915
        sms_sign = '钟远智工作经验分享'
        num = 1     # 超时时间 【单位是分钟】

        ssender = SmsSingleSender(appid, appkey)
        # 参数一: 验证码
        # 参数二: 超时时间
        random_str = random.randrange(1000,10000)
        params = [random_str, num]

        # 超时处理
        # phone:ramdom_str  [key:value]
        # cache.set(str(phone), random_str, 60*num)

        try:
            result = ssender.send_with_param(86, phone,
                                             template_id, params, sign=sms_sign, extend="",
                                             ext="")  # 签名参数未提供或者为空时，会使用默认签名发送短信
            return format_response(msg='短信发送成功', status=200)
        except HTTPError as e:
            print(e)
            return format_response(msg='短信发送失败', status=400, err=e)
        except Exception as e:
            print(e)
            return format_response(msg='短信发送失败', status=400, err=e)
