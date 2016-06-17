# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 15:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacantes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacante',
            old_name='titulo',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='requisito',
            name='id',
        ),
        migrations.AddField(
            model_name='requisito',
            name='vacante_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='vacantes.Vacante'),
            preserve_default=False,
        ),
    ]