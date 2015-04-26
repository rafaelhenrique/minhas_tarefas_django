# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tarefas', '0002_auto_20150425_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='usuario',
            field=models.ForeignKey(related_name='tarefas', verbose_name='usuário', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
