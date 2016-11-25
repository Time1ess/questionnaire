#!/usr/bin/python
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-11-25 19:32
# Last modified: 2016-11-25 19:44
# Filename: views.py
# Description:
from flask import Blueprint, render_template

school = Blueprint('school', 'school',
                   template_folder='templates')


@school.route('/')
def index():
    return render_template('school/index.html')
