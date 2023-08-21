from mysite.settings import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--c7h!nqh))%mjt9*d57=jzs9q@14+!=ddib4uddnc_00vy2645'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# INSTALLED_APPS = []

# Robots 
ROBOTS_USE_HOST = False
ROBOTS_USE_SITEMAP = False

# Site framework
SITE_ID = 3

MAINTENANCE_MODE = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]


# CSRF_COOKIE_SECURE = True