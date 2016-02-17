from  base import *

INSTALLED_APPS += ('django_extensions', )

FAKER_LOCALE = None     # settings.LANGUAGE_CODE is loaded
FAKER_PROVIDERS = None  # faker.DEFAULT_PROVIDERS is loaded (all)

# import rest_framework

REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES']=[]



#EMAIL_CONFIGURACION
#import django.core.mail.backends.smtp.EmailBackend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'nestorgodoy2007@@gmail.com'
EMAIL_HOST_PASSWORD = 'Joseluis14*'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
'''
EMAIL_HOST = 'mx.000webhost.com'
EMAIL_HOST_USER = 'yendry5@test-mural.netai.net'
EMAIL_HOST_PASSWORD = 'yendry1'
EMAIL_PORT = 110
EMAIL_USE_TLS = True
'''

