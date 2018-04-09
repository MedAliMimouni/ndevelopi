# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-26 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_auto_20180326_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapiter',
            name='chpiterSlug',
            field=models.SlugField(blank=True, help_text='enter a slug for the course (a slug is the name in the url exemple you enter html the link will be ndevelopi/html/ ...', null=True),
        ),
    ]
