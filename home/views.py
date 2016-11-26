#!/usr/bin/python
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-11-26 09:42
# Last modified: 2016-11-26 10:30
# Filename: views.py
# Description:
from flask import Blueprint, render_template, request, redirect, url_for

home = Blueprint('home', 'home',
                 template_folder='templates')


@home.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('home/login.html')
    elif request.method == 'POST':
        if validate_user():
            return redirect(url_for('school.table'))
        else:
            context = {}
            error = u'请检查您的用户名和密码是否正确。'
            context['error'] = error
            return render_template('home/login.html', **context)


def validate_user():
    if request.form['username'] == 'david' and request.form['password'] == '1':
        return True
    else:
        return False
