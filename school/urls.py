#!/usr/bin/python
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-11-26 13:46
# Last modified: 2016-11-27 16:52
# Filename: urls.py
# Description:
from django.conf.urls import url

from school import views

urlpatterns = [
    url(r'^$', views.index_view, name="school.question_table"),
]
