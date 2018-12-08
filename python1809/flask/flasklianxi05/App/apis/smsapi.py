import random

from flask_restful import reqparse, fields, Resource

from App.ext import cache
from tools import format_response

parser=reqparse.RequestParser()
parser.add_argument('phone',type=str,required=True)


result_fields = {
    'msg': fields.String,
    'status': fields.Integer,
    'time': fields.String,
    'err': fields.String(default='')
}
from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
class SMSResource(Resource):
    def get(self):
        parse=parser.add_argument()
        phone=parse.get('phone')
        appid=''
        appkey=''
        template_id=''
        sms_sign=''
        num=1
        ssender = SmsSingleSender(appid, appkey)
        random_str = random.randrange(1000, 10000)

        params = [random_str, num]
        cache.set(phone,random_str,60*1)

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


