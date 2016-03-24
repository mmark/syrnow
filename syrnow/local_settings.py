"""
local development settings, not to be checked in
"""
from settings import *

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_URL = 'http://127.0.0.1:8000'
SITE_ID = 1
DEBUG = True
SQL_DEBUG = True
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1:8000']
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
