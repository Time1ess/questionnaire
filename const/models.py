#!/usr/bin/env python
# coding=utf-8

from __future__ import unicode_literals
from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=50)


class School(models.Model):
    province = models.ForeignField(Province)
    name = models.CharField(max_length=100)


class QuestionReport(models.Model):
    school = models.ForeignField(School)
    year = models.IntegerField()
    finished = models.BooleanField(default=False) #是否确认提交
    complete_cnt = models.IntegerField(default=0) #未完成的项数

class QuestionItem(models.Model):
    report = models.ForeignField(QuestionReport)
    text = models.CharField(max_length=200)
    number = models.IntegerField(default=0)
    path = models.CharField(max_length=200, blank=True, null=True)
    complete = models.BooleanField(default=False) #是否完成过
