# Generated by Django 4.0.1 on 2022-02-23 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='like',
        ),
        migrations.RemoveField(
            model_name='commentblog',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='commentblog',
            name='like',
        ),
        migrations.RemoveField(
            model_name='commentnews',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='commentnews',
            name='like',
        ),
        migrations.RemoveField(
            model_name='news',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='news',
            name='like',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]