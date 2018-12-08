import hashlib
import time
import uuid


def get_token():
    hash=hashlib.sha512()
    hash_str=str(uuid.uuid4())+str(int(time.time()))
    hash.update(hash_str.encode())
    return hash.hexdigest()


def format_response(status=400,msg='',err='',data=None):
    responseData={}
    responseData['msg']=msg
    responseData['status']=status
    responseData['err']=err
    responseData['data']=data
    return responseData
