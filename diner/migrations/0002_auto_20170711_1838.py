# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mbbpm',
            name='value',
            field=models.CharField(blank=True, max_length=62, null=True),
        ),
    ]
