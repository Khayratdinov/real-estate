from .base import *

# ============================================================================ #


# ============================================================================ #
#                                     EMAIL                                    #
# ============================================================================ #

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_USE_TLS = True
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = "info@real-estate.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Real Estate"


# ============================================================================ #
#                                   DATABASE                                   #
# ============================================================================ #


DATABASES = {
    "default": {
        "ENGINE": env("POSTGRES_ENGINE"),
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': "django.db.backends.postgresql",
#         'NAME': "real-estate",
#         'USER': "postgres",
#         'PASSWORD': "admin12345",
#         'HOST': "postgres-db",
#         'PORT': "5432",
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'estate',
#         'USER': 'postgres',
#         'PASSWORD': 'admin12345',
#         'HOST': '',
#         'PORT': '5432',
#     }
# }


CELERY_BROKER_URL = env("CELERY_BROKER")
CELERY_RESULT_BACKEND = env("CELERY_BACKEND")
CELERY_TIMEZONE = "Asia/Tashkent"