from django.shortcuts import render, get_object_or_404, redirect
from home.models import News, Comments
from django.views.generic.edit import CreateView, UpdateView


from .forms import CommentForm, PostForm
from .models import User, News

# Create your views hereself.
"""Вывод всех статей на главную страницу"""
def news_list(request):
    news = News.objects.all()
    return render(request, "home/news_list.html", {"news": news})

"""Функция выводящая статью подробно"""
def new_single(request, pk):
    new = get_object_or_404(News, id=pk)
    comment = Comments.objects.filter(new=pk, moderation=True)
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = new
            form.save()
            return redirect(new_single, pk)
    else:
        form = CommentForm()
    return render(request, "home/new_single.html", {"new": new,
                "сommentaries": comment,
                'form': form})

"""Класс для создания постов в блоге"""
class create_post(CreateView):
    model = News
    form_class = PostForm
    template_name = 'home/create_post.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('/create_post/')

    def success_url(self):
        return redirect('')
