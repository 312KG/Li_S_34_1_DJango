from django.contrib import admin
from django.urls import path
from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', views.post_view),
    path('hello/', views.hello),
    path('current_date/', views.current_date),
    path('goodbye/', views.good_bye)
]
