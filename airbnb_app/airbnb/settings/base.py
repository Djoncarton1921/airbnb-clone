import os
from pathlib import Path
from typing import List

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from django.contrib.messages import constants as messages_constants
from django.urls import reverse_lazy


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=g(33qw)hiwuk&$nrdwr#=xd2cblmh0&k^*he)-gq^4#a$b6*r'


ALLOWED_HOSTS: List[str] = []


# Application definition
INSTALLED_APPS = [
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
    'django.contrib.postgres',

    # django
    'rest_framework',
    'bootstrap4',
    'debug_toolbar',
    'django_extensions',
    'django_filters',
    'django_inlinecss',
    'django_celery_beat',
    'ckeditor',
    'ckeditor_uploader',
    'channels',
    'phonenumber_field',
    'sorl.thumbnail',

    # local
    'main.apps.MainConfig',
    'accounts.apps.AccountsConfig',
    'addresses.apps.AddressesConfig',
    'hosts.apps.HostsConfig',
    'realty.apps.RealtyConfig',
    'subscribers.apps.SubscribersConfig',
    'mailings.apps.MailingsConfig',
    'chat_bot.apps.ChatBotConfig',

    # cleanup
    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'main.middleware.MobileUserAgentMiddleware',
]

ROOT_URLCONF = 'airbnb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
            BASE_DIR / 'main/templates',
            BASE_DIR / 'accounts/templates',
            BASE_DIR / 'realty/templates',
            BASE_DIR / 'hosts/templates',
            BASE_DIR / 'subscribers/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'main.context_processors.absolute_url',
            ],
        },
    },
]

WSGI_APPLICATION = 'airbnb.wsgi.application'


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# AUTHENTICATION
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]
AUTH_USER_MODEL = 'accounts.CustomUser'
LOGIN_URL = reverse_lazy('accounts:login')
LOGIN_REDIRECT_URL = reverse_lazy('home_page')
LOGOUT_REDIRECT_URL = reverse_lazy('home_page')


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# SENTRY
SENTRY_CONF = sentry_sdk.init(
    dsn=os.environ.get("AIRBNB_SENTRY_DSN"),
    integrations=[DjangoIntegration()]
)


# SITES
SITE_ID = 1
DEFAULT_PROTOCOL = 'http'


# Static files (CSS, JavaScript, Images)
STATIC_URL = os.environ.get('STATIC_URL', '/static/')
STATIC_ROOT = BASE_DIR / 'airbnb/static/'


# MEDIA
MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')
MEDIA_ROOT = BASE_DIR / 'airbnb/media/'


# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER_ESL')
DEFAULT_FROM_EMAIL = 'support@airbnb.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD_ESL')


# CHARSET
DEFAULT_CHARSET = "utf-8"


# MESSAGES
MESSAGE_TAGS = {
    messages_constants.DEBUG: 'alert-secondary',
    messages_constants.INFO: 'alert-info',
    messages_constants.SUCCESS: 'alert-success',
    messages_constants.WARNING: 'alert-warning',
    messages_constants.ERROR: 'alert-danger',
}


# REST FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
}


# REDIS
REDIS_HOST = os.environ.get('AIRBNB_REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', '6379')
REDIS_DB = os.environ.get('REDIS_MAIN_DB', 1)
REDIS_DECODE_RESPONSES = os.environ.get('REDIS_DECODE_RESPONSES', True)


# CACHES
REDIS_CACHE_DB = os.environ.get('REDIS_CACHE_DB', 2)
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CACHE_DB}",
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    },
}


# SESSIONS
REDIS_SESSION_DB = os.environ.get('REDIS_SESSION_DB', 3)
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS = {
    'host': REDIS_HOST,
    'port': REDIS_PORT,
    'db': REDIS_SESSION_DB,
    'prefix': 'session',
    'socket_timeout': 1,
    'retry_on_timeout': False,
}


# CELERY
CELERY_TIMEZONE = 'Europe/Moscow'
CELERY_BROKER_TRANSPORT = os.environ.get('CELERY_BROKER_HOST', "redis")
CELERY_BROKER_HOST = os.environ.get('CELERY_BROKER_HOST', "redis")
CELERY_BROKER_PORT = os.environ.get('CELERY_BROKER_PORT', '6379')
CELERY_BROKER_VHOST = os.environ.get("CELERY_REDIS_DB", 4)
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", "redis")

CELERY_REDIS_HOST = REDIS_HOST
CELERY_REDIS_PORT = REDIS_PORT
CELERY_REDIS_DB = CELERY_BROKER_VHOST

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'


# CHANNELS
REDIS_CHANNELS_DB = os.environ.get("REDIS_CHANNELS_DB", 5)
REDIS_CHANNELS_URL = os.environ.get("REDIS_CHANNELS_URL", "redis://localhost:6379/2")
ASGI_APPLICATION = 'airbnb.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [REDIS_CHANNELS_URL],
        },
    },
}


# CKEDITOR
CKEDITOR_UPLOAD_PATH = 'upload/images_admin/'
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'width': 'auto',
        'height': '550px',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor', 'Youtube']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                'Preview',
                'Maximize']
             },
        ],
        'toolbar': '',  # selected toolbar config
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            # extra plugins
            'uploadimage',  # the upload image feature
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
        ]),
    },
}


# TWILIO
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')


# PHONENUMBER
PHONENUMBER_DB_FORMAT = 'NATIONAL'
PHONENUMBER_DEFAULT_REGION = 'RU'
