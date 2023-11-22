import datetime

from django.shortcuts import HttpResponse, render
from post.models import Equipment


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


def main(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def post_view(request):
    if request.method == 'GET':
        posts = Equipment.objects.all()

        context = {
            'post': posts
        }

        return render(request, 'posts/post.html', context=context)
