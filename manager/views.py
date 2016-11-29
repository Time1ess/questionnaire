#!/usr/bin/python
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-11-29 09:30
# Last modified: 2016-11-29 11:32
# Filename: views.py
# Description:
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from const.models import Province, School
from const.models import QuestionSheet, AnswerSheet
from const.models import QuestionItem, AnswerItem

from const import PROVINCE_SHEET


@login_required
def question_table_view(request):
    """
    Desc:   Fetch related QuestionSheet(items) and AnswerSheet(items) to 
            render manager question page.

    Author: David
    """
    user = request.user
    # For now, we fetch the last sheet
    q_sheet = QuestionSheet.objects.filter(category=PROVINCE_SHEET).last()
    q_items = q_sheet.questionitem_set.all()
    a_sheet, _ = AnswerSheet.objects.get_or_create(user=user,
                                                question_sheet=q_sheet)
    # create all answer items if not exits.
    # it will be cached by django.
    for q_item in q_items:
        AnswerItem.objects.get_or_create(question_item=q_item, answer_sheet=a_sheet)
    a_items = a_sheet.answeritem_set.all().select_related('question_item')
    a_items = a_items.order_by('question_item__index')
    context = {}
    context['q_sheet'] = q_sheet
    context['a_sheet'] = a_sheet
    context['a_items'] = a_items
    return render(request, 'manager/question_table.html', context)
