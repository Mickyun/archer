# -*- coding: UTF-8 -*- 

"""
Django settings for archer project.

Generated by 'django-admin startproject' using Django 1.8.17.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import pymysql
pymysql.install_as_MySQLdb()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hfusaf2m4ot#7)fkw#di2bu6(cv0@opwmafx5n#6=3d%x^hpl6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sql',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'sql.check_login_middleware.CheckLoginMiddleware',
)

ROOT_URLCONF = 'archer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'sql/static')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sql.processor.global_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'archer.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#扩展django admin里users字段用到，指定了sql/models.py里的class users
AUTH_USER_MODEL="sql.users"

###############以下部分需要用户根据自己环境自行修改###################

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

#该项目本身的mysql数据库地址
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'archer',
        'USER': 'archer_rw',
        'PASSWORD': 'archer_rw',
        'HOST': '172.21.139.1',
        'PORT': '5000'
    }
}

#inception组件所在的地址
INCEPTION_HOST = '172.16.5.7'
INCEPTION_PORT = '6100'

#查看回滚SQL时候会用到，这里要告诉archer去哪个mysql里读取inception备份的回滚信息和SQL.
#注意这里要和inception组件的inception.conf里的inception_remote_XX部分保持一致.
INCEPTION_REMOTE_BACKUP_HOST='172.16.5.10'
INCEPTION_REMOTE_BACKUP_PORT=5621
INCEPTION_REMOTE_BACKUP_USER='inception'
INCEPTION_REMOTE_BACKUP_PASSWORD='inception'

#是否开启邮件提醒功能：发起SQL上线后会发送邮件提醒审核人审核，执行完毕会发送给DBA. on是开，off是关，配置为其他值均会被archer认为不开启邮件功能
MAIL_ON_OFF='on'

MAIL_REVIEW_SMTP_SERVER='172.21.129.215'
MAIL_REVIEW_SMTP_PORT=25
MAIL_REVIEW_FROM_ADDR='archer@xxx.com'                                               #发件人，也是登录SMTP server需要提供的用户名
MAIL_REVIEW_FROM_PASSWORD=''                                                         #发件人邮箱密码，如果为空则不需要login SMTP server
MAIL_REVIEW_DBA_ADDR=['jialiyang@baijiahulian.com', 'zhangpeng@baijiahulian.com']        #DBA地址，执行完毕会发邮件给DBA，以list形式保存
