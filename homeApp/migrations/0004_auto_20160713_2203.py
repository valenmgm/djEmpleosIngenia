# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0003_auto_20160713_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageneshome',
            name='seccion',
            field=models.CharField(choices=[('imagen_intro', 'Imagen Intro'), ('imagen_1', 'Imagen 1'), ('imagen_2', 'Imagen 2'), ('imagen_3', 'Imagen 3')], max_length=50),
        ),
        migrations.AlterField(
            model_name='infoingenia',
            name='seccion',
            field=models.CharField(choices=[('info_intro', 'Intro'), ('info_1', 'Info 1'), ('info_2', 'Info 2'), ('info_3', 'Info 3')], max_length=40),
        ),
    ]
