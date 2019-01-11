from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.MyView.as_view()),
    path('add-ticket/', views.MyTemplateView.as_view())
]
