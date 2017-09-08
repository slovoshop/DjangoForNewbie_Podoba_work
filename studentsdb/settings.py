# -*- coding: utf-8 -*-

"""
Django settings for studentsdb project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""



import os
from django.conf import global_settings

from .evn_settings import SECRET_KEY, DEBUG, TEMPLATE_DEBUG, ALLOWED_HOSTS
from .env_settings import SOCIAL_AUTH_FACEBOOK_SECRET, SOCIAL_AUTH_FACEBOOK_KEY
from .env_settings import DATABASES, STATIC_URL, MEDIA_URL, MEDIA_ROOT
from .env_settings import ADMIN_EMAIL, EMAIL_HOST, EMAIL_PORT, EMAIL_USE_SSL
from .env_settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_USE_TLS
from .env_settings import PORTAL_URL

# in dev envrironment we may not have STATIC_ROOT defined
try:
    from .env_settings import STATIC_ROOT
except ImportError:
    pass

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
		'crispy_forms',
		'registration',
		'social.apps.django_app.default',
		'django_coverage',
		'students',
		'studentsdb',
		'dbbackup',
]

MIDDLEWARE_CLASSES = [
		'studentsdb.middleware.RequestTimeMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
		'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DBBACKUP_STORAGE = 'dbbackup.storage.filesystem_storage'
DBBACKUP_STORAGE_OPTIONS = {'location': os.path.join(BASE_DIR, 'backups')}

ROOT_URLCONF = 'studentsdb.urls'

LOGIN_URL 						= 'users:auth_login'
LOGOUT_URL 						= 'users:auth_logout'
TEMPLATE_REGISTRATION = os.path.join(BASE_DIR, 'templates') # location of login/registry templates 

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_REGISTRATION],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
								'social.apps.django_app.context_processors.backends',
								'social.apps.django_app.context_processors.login_redirect',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
								'django.core.context_processors.request',
								'studentsdb.context_processors.students_proc',
								'students.context_processors.groups_processor',
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = (
	'social.backends.facebook.FacebookOAuth2',
	'django.contrib.auth.backends.ModelBackend',
)


WSGI_APPLICATION = 'studentsdb.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

REGISTRATION_OPEN = True

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

#DEFAULT_CHARSET='utf-8' 

LANGUAGE_CODE = 'uk'
LANGUAGES = (
	('uk', 'Ukrainian'),
	('en', 'English'),
)
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
PORTAL_URL = ''
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')


CRISPY_TEMPLATE_PACK = 'bootstrap3'

LOG_FILE = os.path.join(BASE_DIR, 'studentsdb.log')

LOGGING = {
	'version': 1,
	'disable_existing_loggers': True,
	'formatters': {
		'verbose': {
			'format': '%(levelname)s %(asctime)s %(module)s: %(message)s'
			},
		'simple': {
			'format': '%(levelname)s: %(message)s'
			},
		},
	'handlers': {
		'null': {
			'level': 'DEBUG',
			'class': 'logging.NullHandler',
		},
		'console': {
			'level': 'INFO',
			'class': 'logging.StreamHandler',
			'formatter': 'verbose'
		},
		'file': {
			'level': 'INFO',
			'class': 'logging.FileHandler',
			'filename': LOG_FILE,
			'formatter': 'verbose'
		},
	},
	'loggers': {
		'django': {
			'handlers': ['null'],
			'propagate': True,
			'level': 'INFO',
		},
		'students.signals': {
			'handlers': ['console', 'file'],
			'level': 'INFO',
		},
		'students.views.contact_admin': {
			'handlers': ['console', 'file'],
			'level': 'INFO',
		}
	}
}

COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(BASE_DIR, '..', 'coverage')



