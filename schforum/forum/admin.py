from django.contrib import admin
from .models import Blog,News,CommentNews,CommentBlog,Category
# Register your models here.

admin.site.register(Blog)
admin.site.register(News)
admin.site.register(CommentNews)
admin.site.register(CommentBlog)
admin.site.register(Category)
