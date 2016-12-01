#!/usr/bin/env python
# coding=utf-8
import os

from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from const.models import AnswerItem, AnswerSheet

@csrf_exempt
@login_required
def answer_save(request):
    username = request.user.username
    if request.method == "POST":
        data = list(request.POST.dict().iteritems())
        answers = filter(lambda (k,v):(k.startswith('answer_'), v), data)
        file_data = list(request.FILES.dict().iteritems())
        files = filter(lambda (k,v):(k.startswith('file_'), v), file_data)
        media_dir = settings.MEDIA_DIR
        response = []
        print answers
        for item, value in answers:
            item_id = item.replace('answer_', '')
            try:
                answer_item = AnswerItem.objects.get(id=item_id)
            except AnswerItem.DoesNotExist:
                answer_item = None

            if answer_item:
                answer_item.value = value
                answer_item.save()
                response.append(item_id)

        for item, value in files:
            print item
            item_id = item.replace('file_', '')
            try:
                answer_item = AnswerItem.objects.get(id=item_id)
            except AnswerItem.DoesNotExist:
                answer_item = None

            if answer_item:
                file_ext = value.name[value.name.rfind('.')+1:]
                file_path = os.path.join(media_dir, username)
                try:
                    os.makedirs(file_path)
                except OSError:
                    pass
                file_path = os.path.join(file_path, item_id+file_ext)

                try:
                    with open(file_path, 'wb') as f:
                        f.write(value.read())
                    answer_item.path = file_path
                    answer_item.save()
                    response.append(item_id)
                except IOError,e:
                    print e
                    pass
            
        if response:
            return HttpResponse(','.join(response))
        else:
            return HttpResponse('保存失败')
    else:
        return HttpResponse('非法操作')

@csrf_exempt
@login_required
def answer_confirm(request):
    if request.method == "POST":
        print request.POST
        answer_sheet_id = request.POST["sheet_id"]
        try:
            a_sheet = AnswerSheet.objects.get(id=answer_sheet_id)
        except AnswerSheet.DoesNotExist:
            a_sheet = None
        if a_sheet:
            a_sheet.finished = True
            a_sheet.save()
            return HttpResponse("SUCCESS")

    return HttpResponse("ERROR")
