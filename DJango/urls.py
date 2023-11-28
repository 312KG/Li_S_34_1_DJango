from django.contrib import admin
from django.urls import path
from post import views
# from DJango import settings
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('post/', views.post_view),
    path('hashtags/', views.hashtags_view),
    path('categories/', views.categories_view),
    path('posts/<int:post_id>/', views.post_detail_view),
    # path('hello/', views.hello),
    # path('current_date/', views.current_date),
    # path('goodbye/', views.good_bye)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
