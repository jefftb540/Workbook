# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-09-08 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0030_auto_20170823_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='orcamento',
            name='valor',
            field=models.IntegerField(default=0),
        ),
    ]