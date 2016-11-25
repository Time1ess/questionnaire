#!/usr/bin/python
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-11-25 19:38
# Last modified: 2016-11-25 19:43
# Filename: views.py
# Description:
from flask import Blueprint, render_template

admin = Blueprint('admin', 'admin',
                  template_folder='templates')

@admin.route('/')
def index():
    return render_template('admin/index.html')
