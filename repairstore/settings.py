from oscar.defaults import *
"""
Django settings for repairstore project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR,'static')
MEDIA_DIR = os.path.join(BASE_DIR,'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z*au_xq4^xu^1iy$j2-s80j(*7^&fh47p*pq&dgex@11^ca2kl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['USOscarStoreUS.pythonanywhere.com','store.kccstech.com']


# Application definition
from oscar import get_core_apps

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'widget_tweaks',
    'paypal',
    'stripe',
] + get_core_apps(['yourappsfolder.partner','yourappsfolder.checkout','yourappsfolder.shipping','yourappsfolder.dashboard',
    'yourappsfolder.order',])

PAYPAL_API_USERNAME = 'calvinkcc0-facilitator_api1.gmail.com'
PAYPAL_API_PASSWORD = 'JWKASC5LH3K3RB29'
PAYPAL_API_SIGNATURE = 'A.Uc-kraUyFHKmQHgO7fZfqdXhGkAMvrwwi4MLl-1DzlyI6n-emeelB5'
PAYPAL_CURRENCY = 'USD'
SITE_ID = 1

STRIPE_SECRET_KEY = "sk_test_D6hDVP3hjjwFy4hp8puvyiOv"
STRIPE_PUBLISHABLE_KEY = "pk_test_mJFPanxRUx55cVZ1Zb2IiAQh"
STRIPE_CURRENCY = "USD"

OSCAR_SHOP_TAGLINE = 'Wholesale Cell Phone Repair Parts And Accessories'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.locale.LocaleMiddleware'
]

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)


ROOT_URLCONF = 'repairstore.urls'

from oscar import OSCAR_MAIN_TEMPLATE_DIR

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            OSCAR_MAIN_TEMPLATE_DIR
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',

                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]

WSGI_APPLICATION = 'repairstore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGES = [
    ('en', 'English'),
    ('zh-hant','Traditional Chinese'),
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

OSCAR_DEFAULT_CURRENCY = '$'
OSCAR_CURRENCY_LOCALE = 'US'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = STATIC_DIR

MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
OSCAR_FROM_EMAIL = 'support@kccstech.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.office365.com'
EMAIL_HOST_USER = 'support@kccstech.com'
EMAIL_HOST_PASSWORD = 'Calvinkcc123!'
EMAIL_PORT = 587

OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Processed', 'Cancelled',),
    'Cancelled': (),
}
from django.utils.translation import ugettext_lazy as _
OSCAR_DASHBOARD_NAVIGATION.append(
    {
        'label': _('PayPal'),
        'icon': 'icon-globe',
        'children': [
            {
                'label': _('PayFlow transactions'),
                'url_name': 'paypal-payflow-list',
            },
            {
                'label': _('Express transactions'),
                'url_name': 'paypal-express-list',
            },
        ]
    })
OSCAR_DASHBOARD_NAVIGATION += [
    {
        'label': 'Shipping',
        'children': [
            {
                'label': 'Shipping',
                'url_name': 'dashboard:shipping-method-list',
            },
         ]
    },
]