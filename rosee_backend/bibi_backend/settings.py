import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'change-this-in-production-use-a-long-random-string'
DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.admin','django.contrib.auth','django.contrib.contenttypes',
    'django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',
    'bookings',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'bibi_backend.urls'
TEMPLATES = [{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[],'APP_DIRS':True,
    'OPTIONS':{'context_processors':['django.template.context_processors.debug',
    'django.template.context_processors.request','django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION = 'bibi_backend.wsgi.application'
DATABASES = {'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
# Dev: prints emails to the terminal
# Production SMTP — uncomment and fill in:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'adekunleadepoju916@gmail.com'
EMAIL_HOST_PASSWORD = 'kmnmoarpjefztlby'
EMAIL_TIMEOUT = 5
STUDIO_EMAIL = 'adekunleadepoju916@gmail.com'
DEFAULT_FROM_EMAIL = 'Bibi Lash Studio <adekunleadepoju916@gmail.com>'
STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Lagos'
USE_I18N = True
USE_TZ = True



CSRF_TRUSTED_ORIGINS = ['https://bibi-lash-studio-production.up.railway.app']