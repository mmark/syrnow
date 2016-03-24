"""
@copyright Michelle Mark 2016

Project wide settings
"""
from __future__ import unicode_literals
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.environ.get('ORGHUB_SECRET_KEY')

################################################################################
# Production mode / secure settings over ride for dev in a local_settings.py
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
SITE_ID = 2
DEBUG = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
ALLOWED_HOSTS = ['.organizershub.com', '.organizers-hub.com']
SITE_URL = 'https://syracuseforsanders.organizershub.com'
DEFAULT_FROM_EMAIL = 'michellemark@organizershub.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Make sure the user is not logged in forever, time out after 8 hours
SESSION_COOKIE_AGE = 28800

# Save session on each request, so an active user will not be timed out
SESSION_SAVE_EVERY_REQUEST = True

# Expire session when the user closes the browser
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
ADMINS = (
    ('Michelle Mark', 'topaz1968@gmail.com'),
)
MANAGERS = ADMINS
GOOGLE_API_KEY = os.environ.get('ORGHUB_GOOGLE_API')
################################################################################

# Application definition
INSTALLED_APPS = [
    'django_admin_bootstrapped',
    'storages',
    'ckeditor',
    'ckeditor_uploader',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'snowpenguin.django.recaptcha2',

    'syracuse_for_sanders',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'syrnow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'syrnow.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('ORGHUB_DB_ENGINE'),
        'NAME': os.environ.get('ORGHUB_DB'),
        'USER': os.environ.get('ORGHUB_DB_USER'),
        'PASSWORD': os.environ.get('ORGHUB_DB_PW'),
        'HOST': os.environ.get('ORGHUB_DB_HOST'),
        'PORT': os.environ.get('ORGHUB_DB_PORT'),
    }
}
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        #'toolbar': 'Full',
        'skin': 'moono',
        'toolbar': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'youcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        ],
        'extraPlugins': ','.join(
            [
                'a11yhelp', 'about', 'adobeair', 'ajax', 'autoembed', 'autogrow', 'autolink', 'bbcode',
                'clipboard', 'codesnippet', 'codesnippetgeshi', 'colordialog', 'devtools', 'dialog', 'div',
                'divarea', 'docprops', 'embed', 'embedbase', 'embedsemantic', 'filetools', 'find', 'flash',
                'forms', 'iframe', 'iframedialog', 'image', 'image2', 'language', 'lineutils', 'link',
                'liststyle', 'magicline', 'mathjax', 'menubutton', 'notification', 'notificationaggregator',
                'pagebreak', 'pastefromword', 'placeholder', 'preview', 'scayt', 'sharedspace',
                'showblocks', 'smiley', 'sourcedialog', 'specialchar', 'stylesheetparser', 'table',
                'tableresize', 'tabletools', 'templates', 'uicolor', 'uploadimage', 'uploadwidget',
                'widget', 'wsc', 'xml'
            ]
        )
    },
}
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
RECAPTCHA_PUBLIC_KEY = '6LdcbxsTAAAAAJVVEIW7ljeXXJ6BwTlpvubsylix'
RECAPTCHA_PRIVATE_KEY = '6LdcbxsTAAAAAFgGowBRuMAiwgFqBGRolHzf_qgM'

