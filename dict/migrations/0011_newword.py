# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-09 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0010_auto_20161109_1858'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=75)),
                ('definition', models.CharField(max_length=512)),
                ('author', models.CharField(default='', max_length=128)),
                ('rating', models.SmallIntegerField(default=0)),
            ],
        ),
    ]