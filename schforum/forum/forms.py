from .models import Blog, News,CommentNews,CommentBlog
from django.forms import ModelForm,TextInput,Textarea,DateTimeInput,NumberInput
import datetime
class BlogForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'anons', 'full_text', 'cat1', 'cat2', 'cat3', 'cat4', 'cat5']

        widgets = {
            "title": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Название статьи",
                'max_length': 50,
            }),
            "anons": Textarea(attrs={
                'class': "form-control",
                'placeholder': "Анонс статьи",
                'max_length': 150,
                'style': 'height:200px'
            }),
            "full_text": Textarea(attrs={
                'class': "form-control",
                'placeholder': "Текст статьи",

            }),

        }
class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title','anons','full_text','cat1','cat2','cat3','cat4','cat5']

        widgets ={
            "title": TextInput(attrs={
                'class':"form-control",
                'placeholder': "Название новости",
                'max_length': 50 ,
            }),
            "anons": Textarea(attrs={
                'class': "form-control",
                'placeholder': "Анонс новости",
                'max_length': 150,
                'style':'height:200px'
            }),
            "full_text": Textarea(attrs={
                'class': "form-control",
                'placeholder': "Текст новости",


            }),




        }
class CommentCreateForm(ModelForm):
    class Meta:
        model = CommentNews
        fields = ['text']
        widgets = {
            "text": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Оставить комментарий",
                'max_length': 500,
            })
        }

