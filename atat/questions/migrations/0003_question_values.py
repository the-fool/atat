# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-21 02:36
from __future__ import unicode_literals

import django.contrib.postgres.fields.hstore
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20160921_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='values',
            field=django.contrib.postgres.fields.hstore.HStoreField(default={}),
        ),
    ]
