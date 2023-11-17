import datetime

from django.shortcuts import HttpResponse


def hello(request):
    if request.method == 'GET':
        return HttpResponse("Hello, this is my project")


def current_date(request):
    if request.method == 'GET':
        current_time = datetime.datetime.now()
        return HttpResponse(current_time)


def good_bye(request):
    if request.method == 'GET':
        return HttpResponse("Good bye user!")