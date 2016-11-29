#!/usr/bin/python
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-11-29 09:30
# Last modified: 2016-11-29 09:58
# Filename: views.py
# Description:
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from const.models import Province, School
from const.models import QuestionSheet, AnswerSheet


@login_required
def question_table_view(request):
    return render(request, 'manager/question_table.html')
