# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-30 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0004_auto_20161030_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='nota',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
    ]
