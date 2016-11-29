#!/usr/bin/python
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-11-26 13:46
# Last modified: 2016-11-29 15:15
# Filename: urls.py
# Description:
from django.conf.urls import url

from manager import views
from manager import ajax

urlpatterns = [
    url(r'^$', views.question_table_view, name="manager.question_table"),
    url(r'^save_answer', ajax.save_answers, name="manager.save_answers"),
    url(r'^confirm_answer', ajax.confirm_answer, name="manager.confirm_answer"),
]
