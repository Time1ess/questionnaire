#!/usr/bin/python
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-11-29 09:23
# Last modified: 2016-11-29 09:24
# Filename: admin.py
# Description:
from django.contrib import admin

from const.models import *

# Register your models here.

RegisterClass = (
    Province,
    School,
    QuestionSheet,
    QuestionItem,
    AnswerSheet,
    AnswerItem,
)

for item in RegisterClass:
    admin.site.register(item)
