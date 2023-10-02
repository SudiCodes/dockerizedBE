"""
Django settings for mt_backend project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from mt_backend.be_secrets import smtp, database, google_auth
from datetime import timedelta

# Pluggin the djnago backward incompartibility
import django
from django.utils.encoding import force_str
django.utils.encoding.force_text = force_str


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c987-fp(o%^xbvn4ti*6amq+28%de+m*(69xni*sl82)1=k)x3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# Application definition
SHARED_APPS = (
    'tenant_schemas',  # mandatory, should always be before any django app
    'multitenancy',  # you must list the app where your tenant model resides in

    'django.contrib.contenttypes',

    # everything below here is optional
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
)

TENANT_APPS = (
    'django.contrib.contenttypes',

    # your tenant-specific apps
    'authentication',

)


INSTALLED_APPS = [
    'tenant_schemas',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.sites', # Enabled for all auth
    'rest_framework',
    'corsheaders',
    'djoser',

    'authentication'

]

MIDDLEWARE = [
    'tenant_schemas.middleware.TenantMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mt_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # for django-allauth
                # 'django.template.context_processors.request'
                # for drf-social-oauth2
                # 'social_django.context_processors.backends',
                # for drf-social-oauth2
                # 'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'mt_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': database
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = 'static/'
STATICFILES_DIRS = [
    "/var/www/static/",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Email settings
EMAIL_BACKEND = smtp["EMAIL_BACKEND"]
EMAIL_HOST = smtp["EMAIL_HOST"]
EMAIL_PORT = smtp["EMAIL_PORT"]
EMAIL_HOST_USER = smtp["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = smtp["EMAIL_HOST_PASSWORD"]
EMAIL_USE_TLS = smtp["EMAIL_USE_TLS"]
EMAIL_USE_SSL = smtp["EMAIL_USE_SSL"]
DEFAULT_FROM_EMAIL = smtp["DEFAULT_FROM_EMAIL"]


AUTH_USER_MODEL = "authentication.Customer"


# ACCOUNT_FORMS = {'signup': 'authentication.forms.CustomSignupForm'}


# CORS settings
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = ["https://example.com",
                        "https://sub.example.com", "http://localhost:3000", "http://127.0.1.1:3000"]


CSRF_TRUSTED_ORIGINS = ['http://localhost:3000', 'http://127.0.0.1:3000']

CORS_ALLOW_HEADERS = (
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
)
SESSION_COOKIE_SECURE = False
# CSRF_COOKIE_HTTPONLY = False
# CSRF_COOKIE_SECURE = False


# REST FRAMEWORK configuration
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


AUTHENTICATION_BACKENDS = (
    # 'drf_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    # Google OAuth2
    # 'social_core.backends.google.GoogleOAuth2',
)


SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=180),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    # "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
}


# Djoser configurations
DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "ACTIVATION_URL": "/activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_RESET_CONFIRM_URL": "/password-reset/{uid}/{token}",
    "TOKEN_MODEL": None,
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND": True,
    "SERIALIZERS": {
        'user': 'authentication.serializers.CustomerSerializer',
        'user_create': 'authentication.serializers.CustomerSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    }
}


# multi tenancy configuration
DATABASE_ROUTERS = (
    'tenant_schemas.routers.TenantSyncRouter',
)

TENANT_MODEL = "multitenancy.Client"
