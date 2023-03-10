# 上线阶段的配置文件
# 开发阶段的配置文件

from .const import *

import os
import sys

# 现在BASE_DIR内部小luffyapi
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 把这个路径加入到环境变量
sys.path.insert(0, BASE_DIR)
# 把apps路径加入到环境变量
sys.path.insert(1, os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = 'x-tv!gu(v241g20jmm38guh2hi#-a0y5n*-#mdb*m&ou!155&4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# 运行的host，服务端的地址,买的服务器的公网ip
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',
    'django_filters',
    # xadmin主体模块
    'xadmin',
    # 渲染表格模块
    'crispy_forms',
    # 为模型通过版本控制，可以回滚数据
    'reversion',

    'user',  # 因为apps目录已经被加到环境变量了,所有直接能找到
    'home',
    'course',
    'order',
]

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 处理跨域
    'corsheaders.middleware.CorsMiddleware',
    # 'luffyapi.utils.middle.MyMiddle',
]

ROOT_URLCONF = 'luffyapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'luffyapi.wsgi.application'

# password = sys.path.get('mysql_pass','123456')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'luffyapi',
        'USER': 'luffyapi',
        'PASSWORD': 'Luffy123?',
        'PORT': 3306,
        'HOST': '127.0.0.1',

    }
}
import pymysql

pymysql.install_as_MySQLdb()

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 现在的BASE_DIR是luffyapi下的luffyapi

AUTH_USER_MODEL = 'user.user'

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'luffyapi.utils.exceptions.common_exception_handler',
}

# 日志的配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            # 实际开发建议使用WARNING
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            # 实际开发建议使用ERROR
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            # 日志位置,日志文件名,日志保存目录必须手动创建，注：这里的文件路径要注意BASE_DIR代表的是小luffyapi
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs", "luffy.log"),
            # 日志文件的最大值,这里我们设置300M
            'maxBytes': 300 * 1024 * 1024,
            # 日志文件的数量,设置最大日志数量为10
            'backupCount': 100,
            # 日志格式:详细格式
            'formatter': 'verbose',
            # 文件内容编码
            'encoding': 'utf-8'
        },
    },
    # 日志对象
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True,  # 是否让日志信息继续冒泡给其他的日志处理系统
        },
    }
}

# 封装一个logger对象


# django 使用django-cors-headers 解决跨域问题
# CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = (
#     '*'
# )
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    # 'XMLHttpRequest',
    # 'X_FILENAME',
    # 'accept-encoding',
    'authorization',
    'content-type',
    # 'dnt',
    # 'origin',
    # 'user-agent',
    # 'x-csrftoken',
    # 'x-requested-with',
    # 'Pragma',
)

import datetime
JWT_AUTH = {
    # 过期时间1天
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),

}

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES':{
        'sms':'1/m'  # key要跟类中的scop对应
    }
}


# django默认不支持redis做缓存
# 缓存
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
            # "PASSWORD": "123",
        }
    }
}

# 上线后必须换成公网地址
# 后台基URL
BASE_URL = 'http://123.57.64.206:8000'
# 前台基URL
LUFFY_URL = 'http://123.57.64.206'
# 支付宝同步异步回调接口配置
# 后台异步回调接口
NOTIFY_URL = BASE_URL + "/order/success/"
# 前台同步回调接口，没有 / 结尾
RETURN_URL = LUFFY_URL + "/pay/success"



