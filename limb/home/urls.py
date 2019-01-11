from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.news_list, name="list_news"),
    path('single/<int:pk>', views.new_single, name="new_single")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
