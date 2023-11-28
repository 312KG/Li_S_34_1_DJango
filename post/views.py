import datetime

from django.shortcuts import HttpResponse, render
from post.models import Equipment, HashTag, Review, Category


# def hello(request):
#     if request.method == 'GET':
#         return HttpResponse("Hello, this is my project")
#
#
# def current_date(request):
#     if request.method == 'GET':
#         current_time = datetime.datetime.now()
#         return HttpResponse(current_time)
#
#
# def good_bye(request):
#     if request.method == 'GET':
#         return HttpResponse("Good bye user!")


def main(request):
    # post = Equipment.objects.get(id=1)
    # hashtag = HashTag.objects.get(id=1)
    # hashtag.posts.all()
    # reviews = post.reviews.all()
    # hashtags = post.hashtags.all()
    # print(reviews)
    # for i in reviews:
    #     print(i.text)
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def post_view(request):
    if request.method == 'GET':
        posts = Equipment.objects.all()  # QuerySet

        context = {
            'post': posts
        }

        return render(request, 'posts/post.html', context=context)

def post_detail_view(request, post_id):
    if request.method == 'GET':
        try:
            post = Equipment.objects.get(id=post_id)
        except Equipment.DoesNotExist:
            return render(request, 'errors/404.html')

        context = {
            "post": post
        }
        return render(request, 'posts/post_detail.html', context)

def hashtags_view(request):
    if request.method == 'GET':
        hashtags = HashTag.objects.all()

        context = {
            "hashtags": hashtags
        }

        return render(
            request,
            'posts/hashtags.html',
            context=context
        )

def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        context = {
            "categories": categories
        }

        return render(
            request,
            'posts/categories.html',
            context=context
        )

