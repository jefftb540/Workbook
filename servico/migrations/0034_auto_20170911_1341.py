# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-09-11 13:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0033_auto_20170909_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orcamento',
            name='data_atendimento',
        ),
        migrations.RemoveField(
            model_name='orcamento',
            name='hora_atendimento',
        ),
        migrations.RemoveField(
            model_name='orcamento',
            name='minutos_atendimento',
        ),
    ]
