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

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm97glh*^-^(v$1urstuld512@i@ep=2vt4h_)ajo(ag%ytcxa!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
		'crispy_forms',
    'students',
]

MIDDLEWARE_CLASSES = [
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

ROOT_URLCONF = 'studentsdb.urls'

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
								'django.core.context_processors.request',
								'studentsdb.context_processors.students_proc',
								'students.context_processors.groups_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'studentsdb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

from .db import DATABASES


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


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

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


# email settings
# please, set here you smtp server details and your admin email

from .db import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

ADMIN_EMAIL = 'k6_alexstr@ukr.net'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

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





