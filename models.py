#!/usr/bin/env python
# coding=utf-8

from peewee import *;

from mysql import questionDB

class User(Model):
    name = CharField()
    password = CharField()
    role = IntegerField()
    class Meta:
        db_table = "user"
        database = questionDB

class Province(Model):
    name = CharField()
    class Meta:
        db_table = "province"
        database = questionDB

class School(Model):
    name = CharField()
    province_id = ForeinKeyField(Province)
    class Meta:
        db_table = "school"
        database = questionDB

class Question(Model):
    school_id = ForeinKeyField(School)
    class Meta:
        db_table = "question"
        database = questionDB

class QuestionItem(Model):
    question_id = ForeinKeyField(Question)
    item_name = CharField()
    number = IntegerField()
    path = CharField()
    index = IntegerField()
    class Meta:
        db_table = "question_item"
        database = questionDB
