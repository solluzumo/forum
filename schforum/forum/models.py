from django.db import models
from django.utils import timezone
from account.models import CustomUser
from django.contrib.contenttypes.fields import GenericRelation
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



# Статьи
class Blog(models.Model):
    title = models.CharField("Название",max_length=50)
    anons = models.TextField("Анонсмент",max_length=150)
    full_text = models.TextField("Текст")
    blog_image = models.ImageField("Картинка",blank=True,null=True)
    blog_date = models.DateTimeField("Дата",blank=True,null=True,default=timezone.now)
    blog_author = models.ForeignKey('account.CustomUser', on_delete=models.PROTECT, null=True,
                                            related_name='blog_author',blank=True,default="")
    cat1 = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, related_name='blogcat1', blank=True)
    cat2 = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, related_name='blogcat2', blank=True)
    cat3 = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, related_name='blogcat3', blank=True)
    cat4 = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, related_name='blogcat4', blank=True)
    cat5 = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, related_name='blogcat5', blank=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"

        verbose_name_plural = "Статьи"


class News(models.Model):
    title = models.CharField("Название",max_length=50)

    anons = models.TextField("Анонсмент",max_length=150)

    full_text = models.TextField("Текст")

    news_image = models.ImageField("Картинка",blank=True)

    news_date = models.DateTimeField("Дата",blank=True,null=True,default=timezone.now)

    news_author = models.ForeignKey('account.CustomUser', on_delete=models.PROTECT, null=True,
                                            related_name='news_author',blank=True,default="")


    cat1 = models.ForeignKey('Category', on_delete=models.PROTECT,null=True,
                                            related_name='newscat1',blank=True,default="")

    cat2 = models.ForeignKey('Category', on_delete=models.PROTECT, null=True,
                                            related_name='newscat2',blank=True,default="")

    cat3 = models.ForeignKey('Category', on_delete=models.PROTECT, null=True,
                                             related_name='newscat3',blank=True,default="")

    cat4 = models.ForeignKey('Category', on_delete=models.PROTECT, null=True,
                                            related_name='newscat4',blank=True,default="")

    cat5 = models.ForeignKey('Category', on_delete=models.PROTECT, null=True,
                                            related_name='newscat5',blank=True,default="")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"

        verbose_name_plural = "Новости"

class Category(models.Model):

    name = models.CharField(max_length=100,db_index=True,default="")

    class Meta:
        verbose_name = "Категория"

        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class CommentNews(models.Model):
    comment_author = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE, null=True,
                                            related_name='comment_news_author',blank=True,default="")

    text = models.TextField("Комментарий",max_length=500)


    comment_date = models.DateTimeField("Дата",blank=True,null=True,default=timezone.now)

    dog = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Комментарий к новости"

        verbose_name_plural = "Коментарии к новостям"

class CommentBlog(models.Model):
    comment_author =models.ForeignKey('account.CustomUser', on_delete=models.CASCADE, null=True,
                                            related_name='comment_blog_author',blank=True,default="")

    text = models.TextField("Комментарий",max_length=500)

    comment_date = models.DateTimeField("Дата",blank=True,null=True,default=timezone.now)

    dog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Комментарий к статье"

        verbose_name_plural = "Коментарии к статьям"



