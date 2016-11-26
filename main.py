#!/usr/bin/python
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-11-25 19:09
# Last modified: 2016-11-26 10:11
# Filename: main.py
# Description:
from flask import Flask, render_template

from school.views import school
from admin.views import admin
from home.views import home

app = Flask(__name__)
app.register_blueprint(school, url_prefix='/school')
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(home)

if __name__ == '__main__':
    app.run()
