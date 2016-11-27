#!/usr/bin/python
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-11-27 14:07
# Last modified: 2016-11-27 16:37
# Filename: forms.py
# Description:
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=20, label=u'用户名',
        widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(
        max_length=20, label=u'密码',
        widget=forms.PasswordInput(attrs={'class':'form-control'}))
    captcha = CaptchaField(label=u'验证码')
