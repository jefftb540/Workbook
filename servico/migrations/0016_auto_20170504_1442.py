# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-04 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0015_auto_20170503_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='orcamento',
            name='servicos_atendidos',
            field=models.ManyToManyField(to='servico.Servico'),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='descricao',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
