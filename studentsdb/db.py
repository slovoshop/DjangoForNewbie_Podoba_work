import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
			'ENGINE': 'django.db.backends.mysql',
			'HOST': 'localhost',
			'USER': 'students_db_user',
			'PASSWORD': 'k7k7k7k7',
			'NAME': 'students_db',
    }
}


# Security login to SMTP 
EMAIL_HOST_USER = 'kominterna62@gmail.com'
EMAIL_HOST_PASSWORD = 'baburka10'
