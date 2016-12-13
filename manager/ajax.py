#!/usr/bin/python
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-11-29 12:40
# Last modified: 2016-11-29 19:04
# Filename: ajax.py
# Description:
import os
import logging

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required

from const.models import AnswerItem, AnswerSheet


@csrf_exempt
@login_required
def save_answers(request):
    username = request.user.username
    if request.method == 'POST':
        data = list(request.POST.dict().iteritems())
        answers = filter(lambda (key, val): key.startswith('answer_'), data)
        answers = map(lambda (key, val): (key.replace('answer_', ''), val), answers)
        files = list(request.FILES.dict().iteritems())
        files = map(lambda (key, val): (key.replace('file_', ''), val), files)
        media_dir = settings.MEDIA_DIR
        response = ''
        for ans_id, val in files:
            try:
                item = AnswerItem.objects.get(id=ans_id)
            except AnswerItem.DoesNotExist, e:
                logging.warning(str(e)+':'+ans_id)
                item = None
            if item:
                ext = val.name[val.name.rfind('.')+1:]
                path = os.path.join(media_dir, username)
                try:
                    os.makedirs(path)
                except OSError:
                    pass
                #path = os.path.join(path, ans_id+ext)
                path = os.path.join(path, val.name)
                try:
                    with open(path, 'wb') as f:
                        f.write(val.read())
                    item.path = path
                    item.save()
                    response += ans_id +':'
                except IOError, e:
                    logging.error(e)
        for ans_id, val in answers:
            try:
                item = AnswerItem.objects.get(id=ans_id)
            except AnswerItem.DoesNotExist:
                logging.warning(e)
                item = None
            if item:
                item.value = val
                item.save()
            else:
                return HttpResponse(u'编号不存在')
        if response:
            return HttpResponse(response)
        return HttpResponse(u'保存成功')
    else:
        return HttpResponse(u'非法操作')


@csrf_exempt
@login_required
def confirm_answer(request):
    if request.method == 'POST':
        sheet_id = request.POST['sheet_id']
        try:
            a_sheet = AnswerSheet.objects.get(id=sheet_id)
        except AnswerSheet.DoesNotExist:
            a_sheet = None
        if a_sheet:
            a_sheet.finished = True
            a_sheet.save()
            return HttpResponse('SUCCESS')
    return HttpResponse('ERROR')
