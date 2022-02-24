from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('',views.introduce),
    path('create-blog', views.blog_create),
    path('authors', views.authors),
    path('news',views.news_list),
    path('news/create-news',views.create_news),
    path('news/<int:pk>',views.news_detail_view, name="news-details"),
    path('blog/<int:pk>',views.blogs_detail_view, name="blog-details"),
    path('category/<int:cat_id>',views.show_category, name="category"),
    path('search', views.SearchResultsView,name="search"),
    path('user/<int:pk>',views.user_details,name="user-details")
]
