# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='广告标题', max_length=50)),
                ('description', models.CharField(verbose_name='广告描述', max_length=200)),
                ('image_url', models.ImageField(verbose_name='图片路径', upload_to='ad/%Y/%m')),
                ('callback_url', models.URLField(verbose_name='回调url', blank=True, null=True)),
                ('date_publish', models.DateTimeField(verbose_name='发布时间', auto_now_add=True)),
                ('index', models.IntegerField(verbose_name='排列顺序(从小到大)', default=999)),
            ],
            options={
                'verbose_name': '广告',
                'ordering': ['index', 'id'],
                'verbose_name_plural': '广告',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='文章标题', max_length=50)),
                ('desc', models.CharField(verbose_name='文章描述', max_length=50)),
                ('content', models.TextField(verbose_name='文章内容')),
                ('click_count', models.IntegerField(verbose_name='点击次数', default=0)),
                ('is_recommend', models.BooleanField(verbose_name='是否推荐', default=False)),
                ('date_publish', models.DateTimeField(verbose_name='发布时间', auto_now_add=True)),
            ],
            options={
                'verbose_name': '文章',
                'ordering': ['-date_publish'],
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='分类名称', max_length=30)),
                ('index', models.IntegerField(verbose_name='显示顺序(从小到大)', default=999)),
            ],
            options={
                'verbose_name': '分类',
                'ordering': ['index', 'id'],
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('content', models.TextField(verbose_name='评论内容')),
                ('date_publish', models.DateTimeField(verbose_name='发布时间', auto_now_add=True)),
                ('article', models.ForeignKey(null=True, to='blog.Article', verbose_name='文章', blank=True)),
                ('pid', models.ForeignKey(null=True, to='blog.Comment', verbose_name='父级评论', blank=True)),
            ],
            options={
                'verbose_name': '评论',
                'ordering': ['-date_publish'],
                'verbose_name_plural': '评论',
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='标题', max_length=50)),
                ('description', models.CharField(verbose_name='友情链接描述', max_length=200)),
                ('callback_url', models.URLField(verbose_name='url地址')),
                ('date_publish', models.DateTimeField(verbose_name='发布时间', auto_now_add=True)),
                ('index', models.IntegerField(verbose_name='排列顺序(从小到大)', default=999)),
            ],
            options={
                'verbose_name': '友情链接',
                'ordering': ['index', 'id'],
                'verbose_name_plural': '友情链接',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='标签名称', max_length=30)),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('avatar', models.ImageField(verbose_name='头像', default='avatar/default.png', max_length=200, upload_to='avatar/%Y/%m')),
                ('qq', models.CharField(verbose_name='qq号码', blank=True, max_length=20, null=True)),
                ('mobile', models.CharField(verbose_name='手机号码', blank=True, unique=True, null=True, max_length=11)),
            ],
            options={
                'verbose_name': '用户',
                'ordering': ['-id'],
                'verbose_name_plural': '用户',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, to='blog.User', verbose_name='用户', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, to='blog.Category', verbose_name='分类', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(verbose_name='标签', to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(verbose_name='用户', to='blog.User'),
        ),
    ]
