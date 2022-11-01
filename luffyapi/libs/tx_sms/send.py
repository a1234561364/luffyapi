from qcloudsms_py import SmsSingleSender
from luffyapi.utils.logger import log
from qcloudsms_py.httpclient import HTTPError
from . import settings


# 生成一个四位随机验证码
def get_code():
    import random
    s_code = ''
    for i in range(4):
        s_code += str(random.randint(0, 9))
    return s_code


def send_messgage(phone, code):
    ssender = SmsSingleSender(settings.appid, settings.appkey)
    params = [code, settings.expiration_time]  # 当模板没有参数时，`params = []`
    try:
        result = ssender.send_with_param(86, phone, settings.template_id, params, sign=settings.sms_sign, extend="",
                                         ext="")  # 签名参数不允许为空串
        if result.get('result') == 0:
            return True
        else:
            return False
    except Exception as e:
        log.error('手机号：%s,的短信发送失败,错误为：%s' % (phone, str(e)))
