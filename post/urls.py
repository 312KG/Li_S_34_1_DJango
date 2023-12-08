from django.urls import path
from post import views

urlpatterns = [
    path('', views.main),
    path('post/', views.post_view),
    path('post/create/', views.post_create),
    path('hashtags/', views.hashtags_view),
    path('categories/', views.categories_view),
    path('categories/create/', views.category_create),
    path('posts/<int:post_id>/', views.post_detail_view),
    # path('hello/', views.hello),
    # path('current_date/', views.current_date),
    # path('goodbye/', views.good_bye)
]