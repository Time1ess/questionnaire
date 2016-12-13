#!/usr/bin/python
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-11-26 13:48
# Last modified: 2016-11-27 18:09
# Filename: views.py
# Description:
import os
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from const import SCHOOL_SHEET
from const.models import QuestionSheet, AnswerSheet, AnswerItem

@login_required
def question_table_view(request):
    q_sheet = QuestionSheet.objects.filter(category=SCHOOL_SHEET).last()
    a_sheet, _ = AnswerSheet.objects.get_or_create(user=request.user,
                                                question_sheet=q_sheet)

    finished = a_sheet.finished

    q_items = q_sheet.questionitem_set.all()
    for q_item in q_items:
        AnswerItem.objects.get_or_create(question_item=q_item,
                                        answer_sheet=a_sheet)

    a_items = a_sheet.answeritem_set.all().select_related('question_item').order_by('question_item__index')
    for a_item in a_items:
        a_item.filename = os.path.basename(a_item.path)

    context = {
        "a_items": a_items,
        "a_sheet": a_sheet,
        "finished": finished
    }
    return render(request, 'school/question_table.html', context)
