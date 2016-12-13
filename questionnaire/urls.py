#!/usr/bin/python
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-11-26 13:44
# Last modified: 2016-11-29 10:19
# Filename: urls.py
# Description:
"""questionnaire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from authentication import views as auth_views

urlpatterns = [
    url(r'^$', auth_views.login_view, name='authentication.login'),
    url(r'^admin/', admin.site.urls),
    url(r'^school/', include('school.urls')),
    url(r'^auth/', include('authentication.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^manager/', include('manager.urls')),
]


