"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import cloudinary

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$ok6*buoc-06t2^p&3aff(ki84i-9(gji!73pwsf7!%44sjrfs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mfmadmin-izldar4i.b4a.run', '*', '.mfmadmin-izldar4i.b4a.run']

# Setup support for proxy headers
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
FORCE_SCRIPT_NAME = 'https://mfmadmin-izldar4i.b4a.run'
# SECURE_SSL_REDIRECT = True

CSRF_TRUSTED_ORIGINS = ['https://mfmadmin-izldar4i.b4a.run',]
CSRF_COOKIE_DOMAIN = 'mfmadmin-izldar4i.b4a.run'


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'taggit',
    'drf_yasg',
    'ckeditor',
    'ckeditor_uploader',
    'embed_video',
    'main',
    'program',
    'sermon',
    'rest_framework',
    'cloudinary',
    'corsheaders',
    'djangoql',
    'import_export'
]
# pip install -U django-jazzmin drf-yasg
# django-taggit django-ckeditor-5 django-ckeditor django-embed-video djangorestframework cloudinary django-cors-headers djangoql django-import-export

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'core.middleware.AdminCORSMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ]
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# SECURE_SSL_REDIRECT = True
# # Configure the SECURE_HSTS_INCLUDE_SUBDOMAINS setting if needed.
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# # Include the SECURE_HSTS_PRELOAD setting if you want to submit your site to the HSTS preload list.
# SECURE_HSTS_PRELOAD = True


STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'main/static')]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_uploads')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CORS_ALLOWED_ORIGINS = (
#     'https://camfront.vercel.app',
#     'https://mfmadmin-izldar4i.b4a.run',
#     'http://localhost:3000',
#     'http://localhost:8000',
# )

CORS_ALLOW_METHODS = (
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
    "DELETE",
)

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True

####################################
    ##  CKEDITOR CONFIGURATION ##
####################################
# for uploading images and the rest using ckeditor
# https://django-ckeditor.readthedocs.io/en/latest/

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'my_uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 550,
    },
}


###################################
    ##  TAG CASE SENSITIVE ##
#################################### 
TAGGIT_CASE_INSENSITIVE = True


###################################
    ##  CLOUDINARY IMAGE AND VIDEO UPLOAD SETTINGS ##
#################################### 
cloudinary.config( 
  cloud_name = "ddqibt7em", 
  api_key = "185718447627493", 
  api_secret = "QIYTfSXOefCl72rixkvBgEzJiDs",
  secure = True
)

###############   JAZZMIN SETTINGS ###################
JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "MFM Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "MFMCAM",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "MFMCAM",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "img/logo.png",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": "img/logo.png",

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": "img/logo.png",

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": "img/logo.png",

    # Welcome text on the login screen
    "welcome_sign": "Welcome to MFMCAM WEBSITE",

    # Copyright on the footer
    "copyright": "Acme MooglesMe",

    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth.User",

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": 'img/logo.png',
}


