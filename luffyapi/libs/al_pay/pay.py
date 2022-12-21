from alipay import AliPay
# from alipay.utils import AliPayConfig
from . import settings




alipay = AliPay(
    appid=settings.APPID,
    # app_notify_url='http://127.0.0.1:8000/home/',  # the default notify path
    app_notify_url=None,  # the default notify path
    app_private_key_string=settings.APP_PRIVATE_KEY_STRING,
    # alipay public key, do not use your own public key!
    alipay_public_key_string=settings.ALIPAY_PUBLIC_KEY_STRING,
    sign_type=settings.SIGN_TYPE,  # RSA or RSA2
    debug=settings.DEBUG,  # False by default
    # verbose=False,  # useful for debugging
    # config=AliPayConfig(timeout=15)  # optional, request timeout
)

gateway = settings.GATEWAY

