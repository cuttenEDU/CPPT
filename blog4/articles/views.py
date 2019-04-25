# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import Http404
from models import Article

# Create your views here.
def archive(request):
    return render(request,'archive.html', {"posts":
                                               Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    if not request.user.is_anonymous():
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"],
                'title': request.POST["title"]
            }

            article = None;
            try:
                article = Article.objects.get(title=form["title"])
            except Article.DoesNotExist:
                pass
            # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"] and article is None:
                # если поля заполнены без ошибок
                article = Article.objects.create(text=form["text"],
                                                 title=form["title"],
                                                 author=request.user)
                return redirect('get_article', article_id=article.id)
            # перейти на страницу поста
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})

    else:
        raise Http404
