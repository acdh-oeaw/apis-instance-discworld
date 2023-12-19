"""
Django settings for discworld project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from apis_acdhch_default_settings.settings import *

from pathlib import Path

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2o=u-b51(vfs@0*o4!)blar1u9s7d+2ci&e3kwjabyrgwv=jxt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ROOT_URLCONF = 'discworld.urls'

WSGI_APPLICATION = 'discworld.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = "bootstrap4"
