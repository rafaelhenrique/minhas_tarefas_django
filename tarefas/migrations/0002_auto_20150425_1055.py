# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='data_de_execucao',
            field=models.DateTimeField(blank=True, verbose_name='data de execução', null=True),
            preserve_default=True,
        ),
    ]
