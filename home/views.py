#!/usr/bin/python
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-11-26 09:42
# Last modified: 2016-11-26 10:11
# Filename: views.py
# Description:
from flask import Blueprint, render_template

home = Blueprint('home', 'home',
                 template_folder='templates')


@home.route('/login')
def login():
    return render_template('home/login.html')
