"""Production settings."""

import os
from .base import *  # noqa: F403


SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
PRODUCTION_HOSTNAMES = [
    'genome.edu.au',
    'apollo-portal.genome.edu.au',
    'django-sandpit.genome.edu.au',
    'ubuntu22-test.genome.edu.au',
]
ALLOWED_HOSTS += PRODUCTION_HOSTNAMES  # noqa
CSRF_TRUSTED_ORIGINS = [
    f"https://{hostname}"
    for hostname in PRODUCTION_HOSTNAMES
]

# Use manifest to manage static file versions for cache busting:
STATICFILES_STORAGE = ('django.contrib.staticfiles.storage'
                       '.ManifestStaticFilesStorage')

DATABASES['default'] = {  # noqa: F405
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.environ['DB_NAME'],
    'USER': os.environ['DB_USER'],
    'PASSWORD': os.environ['DB_PASSWORD'],
    'HOST': '127.0.0.1',
    'PORT': '5432',
}
