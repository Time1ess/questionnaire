#!/usr/bin/python
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-11-29 09:30
# Last modified: 2016-11-29 19:04
# Filename: views.py
# Description:
import os

from collections import defaultdict
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from const.models import Province, School
from const.models import QuestionSheet, AnswerSheet
from const.models import QuestionItem, AnswerItem

from const import PROVINCE_SHEET, SCHOOL_SHEET


@login_required
def question_table_view(request):
    """
    Desc:   Fetch related QuestionSheet(items) and AnswerSheet(items) to
            render manager question page.

    Author: David
    """
    context = {}
    user = request.user

    # We fetch the last sheet
    q_sheet = QuestionSheet.objects.filter(category=PROVINCE_SHEET).last()
    q_items = q_sheet.questionitem_set.all()
    a_sheet, _ = AnswerSheet.objects.get_or_create(user=user,
                                                   question_sheet=q_sheet)
    # Create all answer items if not exists.
    # it will be cached by django.
    for q_item in q_items:
        AnswerItem.objects.get_or_create(question_item=q_item,
                                         answer_sheet=a_sheet)
    a_items = a_sheet.answeritem_set.all().select_related('question_item')
    a_items = a_items.order_by('question_item__index')
    finished = a_sheet.finished
    for a_item in a_items:
        a_item.filename = os.path.basename(a_item.path)

    context['q_sheet'] = q_sheet
    context['a_sheet'] = a_sheet
    context['a_items'] = a_items
    context['finished'] = finished

    # Fetch schools in this province
    province = user.province
    schools = School.objects.filter(province=province)
    q_sheet_school = QuestionSheet.objects.filter(category=SCHOOL_SHEET).last()

    vals_sum = defaultdict(int)
    for school in schools:
        a_sheet_school = AnswerSheet.objects.get(user=school.user,
                                                 question_sheet=q_sheet_school)
        ans_items = a_sheet_school.answeritem_set.all()
        for item in ans_items:
            vals_sum[item.question_item] += int(item.value)
    school_data = sorted(vals_sum.items(), key=lambda x: x[0].index)

    context['school_data'] = school_data
    return render(request, 'manager/question_table.html', context)
