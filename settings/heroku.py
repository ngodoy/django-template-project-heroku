from  base import *

INSTALLED_APPS += ('django_extensions', )

FAKER_LOCALE = None     # settings.LANGUAGE_CODE is loaded
FAKER_PROVIDERS = None  # faker.DEFAULT_PROVIDERS is loaded (all)

# import rest_framework

REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES']=[]
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

WSGI_APPLICATION = 'motelAdmin.wsgiheroku.application'

import dj_database_url
DATABASES['default'] =  dj_database_url.config()

STATIC_URL = '/staticfiles/'

#EMAIL_CONFIGURACION
##
EMAIL_BACKEND = 'postmark.django_backend.EmailBackend'
#EMAIL_HOST = '127.0.0.1'
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
#EMAIL_PORT = 1025
#EMAIL_USE_TLS = False


#Supply your own API KEY
POSTMARK_API_KEY =  os.environ.get('POSTMARK_API_TOKEN')
#assert len(POSTMARK_API_KEY) != 0

#Use the sender set up in your postmark account
#POSTMARK_SENDER = ''
#assert len(POSTMARK_SENDER) != 0
