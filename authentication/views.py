#!/usr/bin/python
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-11-27 13:46
# Last modified: 2016-11-27 18:07
# Filename: views.py
# Description:
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from authentication.forms import LoginForm


def login_view(request):
    context = {}
    if request.method == 'GET':
        login_form = LoginForm()
        context['login_form'] = login_form
        return render(request, 'authentication/login.html', context)
    else:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(**cd)
            if user is not None:
                login(request, user)
                return redirect('school.question_table')
            context['errors'] = 'Invalid User'
        context['login_form'] = login_form
        return render(request, 'authentication/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('authentication.login')
