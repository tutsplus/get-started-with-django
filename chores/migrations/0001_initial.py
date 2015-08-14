# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('due_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ChoreList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('due_date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='chore',
            name='chore_list',
            field=models.ForeignKey(to='chores.ChoreList'),
        ),
    ]
