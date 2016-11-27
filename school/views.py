#!/usr/bin/python
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-11-26 13:48
# Last modified: 2016-11-27 18:09
# Filename: views.py
# Description:
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def question_table_view(request):
    return render(request, 'school/question_table.html')
