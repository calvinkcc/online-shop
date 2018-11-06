"""repairstore URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from oscar.app import application
from paypal.payflow.dashboard.app import application as payflow
from paypal.express.dashboard.app import application as express_dashboard
from yourappsfolder.checkout.views import save_contact_form
from yourappsfolder.dashboard.views import ContactListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', application.urls),
    re_path(r'^contact/add/$',save_contact_form,name='create_contact'),
    re_path(r'^dashboard/contacts-list/$',ContactListView.as_view(),name='contact_list'),
    re_path(r'^checkout/paypal/', include('paypal.express.urls')),
    # Dashboard views for Payflow Pro
    re_path(r'^dashboard/paypal/payflow/', payflow.urls),
    # Dashboard views for Express
    re_path(r'^dashboard/paypal/express/', express_dashboard.urls),
]