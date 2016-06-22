# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacantes', '0003_auto_20160617_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacante',
            name='abierta',
            field=models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=True),
        ),
        migrations.AlterField(
            model_name='requisito',
            name='requisito_de',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vacantes.Vacante'),
        ),
    ]
