# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-30 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0025_usuario_nome_fantasia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servico',
            old_name='valor',
            new_name='valor_maximo',
        ),
        migrations.RemoveField(
            model_name='servico',
            name='celular',
        ),
        migrations.RemoveField(
            model_name='servico',
            name='mediaAvaliacoes',
        ),
        migrations.RemoveField(
            model_name='servico',
            name='telefone',
        ),
        migrations.RemoveField(
            model_name='servico',
            name='totalAvaliacoes',
        ),
        migrations.AddField(
            model_name='servico',
            name='valor_minimo',
            field=models.IntegerField(null=True),
        ),
    ]
