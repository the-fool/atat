# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-22 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('responses', '0005_auto_20160921_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='demography',
            name='nice',
            field=models.CharField(default='', max_length=128),
        ),
    ]