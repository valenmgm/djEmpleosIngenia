# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 22:08
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contactoApp', '0002_contactorecursoshumanos'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactorecursoshumanos',
            name='fecha',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime.now()),
            preserve_default=False,
        ),
    ]
