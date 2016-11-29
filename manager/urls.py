#!/usr/bin/python
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-11-26 13:46
# Last modified: 2016-11-29 10:07
# Filename: urls.py
# Description:
from django.conf.urls import url

from manager import views

urlpatterns = [
    url(r'^$', views.question_table_view, name="manager.question_table"),
]
