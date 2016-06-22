# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 17:39
from __future__ import unicode_literals

import contacto.modelsC
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactoInteresado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='contactoaplicante',
            name='mensaje',
        ),
        migrations.AddField(
            model_name='contactoaplicante',
            name='cv',
            field=models.FileField(blank=True, upload_to=contacto.modelsC.path_and_rename),
        ),
        migrations.AlterField(
            model_name='contactoingenia',
            name='correo',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='contactoingenia',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
    ]