# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-13 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0012_auto_20170404_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitacao',
            name='servico',
        ),
        migrations.AddField(
            model_name='solicitacao',
            name='servico',
            field=models.ManyToManyField(to='servico.Servico'),
        ),
    ]