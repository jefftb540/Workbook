# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-04 00:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0009_auto_20170304_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
