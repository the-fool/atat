# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-13 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_question_short'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='notes',
            field=models.CharField(default='', max_length=512),
        ),
    ]
