#!/usr/bin/python
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-11-26 13:48
# Last modified: 2016-11-27 17:33
# Filename: views.py
# Description:
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index_view(request):
    return render(request, 'school/index.html')
