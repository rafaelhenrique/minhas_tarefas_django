# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('descricao', models.TextField(verbose_name='descrição')),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True, verbose_name='data de criação')),
                ('data_de_execucao', models.DateTimeField(verbose_name='data de execução')),
                ('finalizado', models.BooleanField(verbose_name='finalizado', default=False)),
            ],
            options={
                'ordering': ['-data_de_criacao'],
                'verbose_name': 'tarefa',
                'verbose_name_plural': 'tarefas',
            },
            bases=(models.Model,),
        ),
    ]
