import json
from django.shortcuts import render,redirect
from .models import *
from .forms import BlogForm,NewsForm,CommentCreateForm
from django.db.models import Q,CharField
from django.db.models.functions import Lower
from django.contrib.auth.models import Group
from account.models import CustomUser
from django.http import HttpResponse
from django.views import View
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required


#Главная и статьи
def SearchResultsView(response):
    CharField.register_lookup(Lower, "lower")
    query =response.GET.get('q')
    if query !="":
        news_list = News.objects.filter(Q(title__iregex=query.lower()) | Q(full_text__iregex=query))
        blogs_list = Blog.objects.filter(Q(title__iregex=query.lower()) | Q(full_text__iregex=query))

        return render(response,'search_results.html',{"news_results":news_list,"blogs_results":blogs_list})
    return  render(response,'search_results.html',{"news_results":"Empty"})

def introduce(response):
    cats = Category.objects.all()
    blog1 = Blog.objects.get(pk=1)
    blog2 = Blog.objects.get(pk=2)
    blog3 = Blog.objects.get(pk=3)
    news = News.objects.all()
    context = {
        "blog1": blog1,
        "blog2": blog2,
        "blog3": blog3,
        "news": news,
        'cats': cats
    }
    return render(response,'forum/forum-main.html', context)


#Создание статьи


#Выбранная статья: отображение статьи, комментарии, повысить рейтинг
def news_detail_view(response,pk):
    error=''
    model = News.objects.get(id=pk)
    comments = CommentNews.objects.all()

    if response.method == "POST" and 'btn-create-comment' in response.POST:
        instance = CommentNews(comment_author=response.user,dog=model)
        form = CommentCreateForm(response.POST, instance=instance)
        if form.is_valid():
            form.save()

        else:
            error = "Ошибка в заполнении формы"

    comment_create_form = CommentCreateForm()

    data = {
        'news': model,
        'comments': comments,
        'comment_create_form': comment_create_form,
        'error':error,
        'User':CustomUser,
    }
    return render(response,'forum/news-page.html',data)

def blogs_detail_view(response,pk):
    error=''
    model = Blog.objects.get(id=pk)
    comments = CommentBlog.objects.all()

    if response.method == "POST" and 'btn-create-comment' in response.POST:
        instance = CommentBlog(comment_author=response.user,dog=model)
        form = CommentCreateForm(response.POST, instance=instance)
        if form.is_valid():
            form.save()

        else:
            error = "Ошибка в заполнении формы"

    comment_create_form = CommentCreateForm()

    data = {
        'blogs': model,
        'comments': comments,
        'comment_create_form': comment_create_form,
        'error':error,
        'User':CustomUser,
    }
    return render(response,'forum/blog-page.html',data)


def user_details(response,pk):
    data={
        'user':CustomUser.objects.get(id=pk)

    }
    return render(response, 'forum/show_user.html', context=data)

#Страница авторов
def authors(response):

    group = Group.objects.get(name='хуесосы')
    users = group.user_set.all()
    return render(response,'forum/authors.html',{"authors":users})

#Отображение категорий

def show_category(response,cat_id):
    cats = Category.objects.all()
    news = News.objects.all()
    blogs = Blog.objects.all()
    data = {
        'cat_id':0,
        'cats':cats,
        'cat_selected':cat_id,
        'news':news,
        'blogs':blogs,

    }
    return render(response, 'forum/show_category.html',context = data)

#Новости

#Список новостей
def news_list(response):
    return render(response,'news/news-main.html')

#Создание статьи
@login_required(login_url='../login')
def create_news(response):

    error = ""
    if response.method == "POST":
        instance = News(news_author=CustomUser.objects.get(username=response.user))
        form = NewsForm(response.POST, instance=instance)
        if form.is_valid():
            form.save()

            return redirect("../../")

        else:
            error = "Ошибка в заполнении формы"

    form = NewsForm()

    data = {

        'form': form,
        'error':error
    }
    return render(response,'news/news-create.html',data)

@login_required(login_url='../login')
def blog_create(response):
    error = ""
    if response.method == "POST":
        instance = Blog(blog_author=response.user)
        form = BlogForm(response.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("../../")

        else:
            error = "Ошибка в заполнении формы"

    form = BlogForm()

    data = {
        'user':response.user,
        'form': form,
        'error': error,
    }
    return render(response,'forum/create-discuss.html',data)