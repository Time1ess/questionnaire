#!/usr/bin/python
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-11-26 13:48
# Last modified: 2016-11-26 13:48
# Filename: views.py
# Description:
from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'school/index.html')
