# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-22 20:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('overview', models.TextField(help_text='write a brief overview', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Chapiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='your chpiter title', max_length=256)),
                ('completed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text="your cource's title", max_length=50)),
                ('summary', models.TextField(help_text='Enter a brief description of the cource', max_length=1000)),
                ('pic', models.URLField(help_text='image link', max_length=256)),
                ('github_url', models.URLField(help_text='Enter the github url page that includes all commits', max_length=256)),
                ('slug', models.SlugField(help_text='enter a slug for the course (a slug is the name in the url exemple you enter html the link will be ndevelopi/html/ ...')),
                ('authors', models.ManyToManyField(help_text='Who are the authors of this cource ', to='course.Authors')),
                ('enrolled', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Requirments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='requirment subject (like html)', max_length=50)),
                ('info', models.TextField(help_text='basic info of what should the student learn for this subject ', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Youtube_links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(help_text='url video', max_length=256)),
                ('name', models.CharField(max_length=256, null=True)),
                ('chapiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Chapiter')),
                ('seen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='requirments',
            field=models.ManyToManyField(help_text='Select the requirments for this book', to='course.Requirments'),
        ),
        migrations.AddField(
            model_name='chapiter',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course'),
        ),
    ]
