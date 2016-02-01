"""
Local Settings
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dubilapdb',
        'USER': 'dbadmin',
        'PASSWORD': 'seniorjunior789',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


######## EMAIL CONF ########

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'enquiry.dubailap@gmail.com'
EMAIL_HOST_PASSWORD = 'sonyericssonw200i'
EMAIL_PORT = 587
EMAIL_USE_TLS = True