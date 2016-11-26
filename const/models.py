#!/usr/bin/env python
# coding=utf-8

from __future__ import unicode_literals
from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = u"省份"
        verbose_plure_name = u"省份"
    def __unicode__(self):
        return "%s" % self.name

class School(models.Model):
    province = models.ForeignField(Province)
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = u"院校"
        verbose_plure_name = u"院校"
    def __unicode__(self):
        return "%s" % self.name

class QuestionItem(models.Model):
    text = models.CharField(max_length=200)
    index = models.IntegerField(unique=True)

    class Meta:
        verbose_name = u"问题项"
        verbose_plure_name = u"问题项"
    def __unicode__(self):
        return "%s" % self.text

class AnswerSheet(models.Model):
    school = models.ForeignField(School)
    year = models.IntegerField()
    finished = models.BooleanField(default=False) #是否确认提交
    complete_cnt = models.IntegerField(default=0) #未完成的项数

    class Meta:
        verbose_name = u"问卷"
        verbose_plure_name = u"问卷"
    def __unicode__(self):
        return "%s %d" % (self.school.name, self.year)

class AnswerItem(models.Model):
    question_item = models.ForeignField(QuestionItem)
    answer_sheet = models.ForeignField(AnswerSheet)
    number = models.IntegerField(default=0)
    path = models.CharField(max_length=200, blank=True, null=True)
    complete = models.BooleanField(default=False) #是否完成过

    class Meta:
        verbose_name = u"回答项"
        verbose_plure_name = u"回答项"
    def __unicode__(self):
        return "%s:%s" % (self.question_item.text, self.number)
