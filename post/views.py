import datetime

from django.shortcuts import HttpResponse, render, redirect
from post.models import Equipment, HashTag, Review, Category, Feedback
from post.forms import PostCreateForm, PostCreateForm2, CategoryCreateForm, FeedbackCreateForm


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

        post = Equipment.objects.get(id=post_id)
        feedbacks = Feedback.objects.filter(equipment=post)

        context = {
            "post": post,
            'feedback': feedbacks,
            'form': FeedbackCreateForm
        }
        return render(request, 'posts/post_detail.html', context=context)
    if request.method == 'POST':
        post = Equipment.objects.get(id=post_id)
        feedbacks = Feedback.objects.filter(post=post)
        form = FeedbackCreateForm(data=request.POST)
        if form.is_valid():
            Feedback.objects.create(
                title=form.cleaned_data.get('title'),
                post=post
            )
            return redirect(f'/post/{post.id}/')
        return render(request, 'posts/post_detail.html', context={
            "post": post,
            'feedback': feedbacks,
            'form': FeedbackCreateForm
        })

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

def post_create(request):
    if request.method == 'GET':
        context = {
            'form': PostCreateForm
        }
        return render(request, 'posts/create.html', context)
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Equipment.objects.create(**form.cleaned_data)
            return redirect("/post/")
            # Equipment.objects.create(
            #     title=form.cleaned_data['title'],
            #     description=form.cleaned_data['description'],
            #     image=form.cleaned_data['image'],
            #     price=form.cleaned_data['price'],
            #     rate=form.cleaned_data['rate']
            # )
            # return redirect('/post/')

        context = {
            'form': form
        }

        # Equipment.objects.create(
        #     title=title, description=description, image=image, price=price, rate=rate
        # )
        return redirect('/posts/create.html', context)
        # return render(request, 'posts/create.html', context)


def category_create(request):
    if request.method == 'GET':
        context = {
            'form': CategoryCreateForm
        }
        return render(request, 'posts/create_category.html', context)
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Equipment.objects.create(**form.cleaned_data)
            return redirect("/categories/")

        context = {
            'form': form
        }

        return redirect('/posts/create_category.html', context)


