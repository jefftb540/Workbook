# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-04 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0017_auto_20170504_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orcamento',
            name='descricao',
            field=models.CharField(default='', max_length=1000, null=True),
        ),
    ]
