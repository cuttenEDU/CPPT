# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import Http404
from models import Article
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def archive(request):
    return render(request,'archiveNew.html', {"posts":
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

def create_user(request):
    if request.method == "POST":
        data = {
            'username': request.POST["username"],
            'mail': request.POST["mail"],
            'password': request.POST["password"]
        }
        user = None
        try:
            user = User.objects.get(username=data["username"])
            user = User.objects.get(email=data["mail"])
            print (u"This username already exists")
        except User.DoesNotExist:
            pass
        if data["username"] and data["mail"] and data["password"] and user is None:
            user = User.objects.create(username=data["username"], email=data["mail"],
                                       password=make_password(data["password"]))
            return redirect(archive)
        else:
            if user is not None:
                data["errors"] = u"Login or/and email is already taken"
            else:
                data["errors"] = u"Not all fields are filled in"
            return render(request, 'registration.html', {'data': data})
    else:
        return render(request, 'registration.html', {})


def input_user(request):
    if request.method == "POST":
        data = {
            'username': request.POST["username"],
            'password': request.POST["password"]
        }
        if data["username"] and data["password"]:
            user = authenticate(username=data["username"], password=data["password"])
            if user is None:
                data['errors'] = u"Такой пользователь не зарегестрирован!"
                return render(request, 'login.html', {'form': data})
            else:
                login(request, user)
                return redirect('home')
        else:
            data['errors'] = u"Не все поля заполнены"
            return render(request, 'login.html', {'form': data})
    else:
        return render(request, 'login.html', {})
