# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-23 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0028_auto_20170821_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacao',
            name='respondida',
            field=models.BooleanField(default=False),
        ),
    ]