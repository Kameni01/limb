from django.shortcuts import render, get_object_or_404
from home.models import News, Comments
from .forms import CommentForm

# Create your views hereself.
"""Вывод всех статей на главную страницу"""
def news_list(request):
    news = News.objects.all()
    return render(request, "home/news_list.html", {"news": news})

"""Функция выводящая статью подробно"""
def new_single(request, pk):
    new = get_object_or_404(News, id=pk)
    comment = Comments.objects.filter(new=pk)
    return render(request, "home/new_single.html", {"new": new, "Comments": comment})
