#!/usr/bin/python
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-11-26 13:48
# Last modified: 2016-11-27 18:09
# Filename: views.py
# Description:
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from const import SCHOOL_SHEET
from const.models import QuestionSheet,School,QuestionItem, AnswerSheet, AnswerItem

@login_required
def question_table_view(request):
    q_sheet = QuestionSheet.objects.filter(category=SCHOOL_SHEET).last()
    school = request.user.school
    q_items = QuestionItem.objects.filter(question_sheet=q_sheet).order_by('index')
    
    a_sheet = AnswerSheet.objects.filter(user=request.user).filter(question_sheet=q_sheet).last()
    print dir(a_sheet)
    

    context = {
        "q_items": q_items
    }
    return render(request, 'school/question_table.html', context)
