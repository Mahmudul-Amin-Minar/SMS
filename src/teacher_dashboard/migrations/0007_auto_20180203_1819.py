# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-03 12:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_dashboard', '0006_auto_20180203_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Student'),
        ),
    ]
