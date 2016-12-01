#!/usr/bin/python
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-11-26 13:46
# Last modified: 2016-11-27 18:09
# Filename: urls.py
# Description:
from django.conf.urls import url

from school import views
from school import ajax

urlpatterns = [
    url(r'^$', views.question_table_view, name="school.question_table"),
    url(r'answer_save$', ajax.answer_save, name="school.answer_save"),
    url(r'answer_confirm$', ajax.answer_confirm, name="school.answer_confirm")
]
