from pathlib import Path
import os
import socket
socket.getaddrinfo('127.0.0.1', 8000)

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-3d1^+j5@*y**2!dyv53h!t@tplo!mc3wyt1eorjl8&36uc-ar9'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'accounts.apps.AccountsConfig',
    'posts.apps.PostsConfig',
    'chat.apps.ChatConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'widget_tweaks',
    'social_django',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'crispy_forms',
    'django_private_chat',
    'django_messages',
    
]
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                os.path.join(BASE_DIR, 'templates', 'allauth', 'static'),
                os.path.join(BASE_DIR, 'accounts', 'templates', 'accounts'),
                os.path.join(BASE_DIR, 'posts', 'templates', 'posts'),
                os.path.join(BASE_DIR, 'chat', 'templates', 'chat'),

],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

TEMPLATE_CONTEXT_PROCESSORS = (
    'django_messages.context_processors.inbox',
)
FORM_RENDERER = 'django.forms.renderers.DjangoTemplates'

WSGI_APPLICATION = 'server.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'valentina98',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',

]

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v10.0',
    },
    'google': {
        'SCOPE': [
            'profile',
            'email',
            
        ],
     
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/images/'


STATIC_ROOT = os.path.join(BASE_DIR,'/static/')
LOGIN_REDIRECT_URL = 'about'
LOGOUT_REDIRECT_URL = 'index' 

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 2

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '176538770623-bph9ltepol7l5t5m1vpvm03qfukgpgid.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'rTJV5c-9ulfFBDfwKGxOcgJF'

SOCIAL_AUTH_FACEBOOK_KEY = '313689557037437'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET ='15e4a8992f8403d7f61758fd540e0ef2' #app key


EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = str(BASE_DIR.joinpath('sent_emails'))

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.User'

CHAT_WS_SERVER_HOST = 'localhost'
CHAT_WS_SERVER_PORT = 5002
CHAT_WS_SERVER_PROTOCOL = 'ws'