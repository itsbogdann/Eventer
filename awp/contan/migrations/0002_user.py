# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('parola', models.CharField(max_length=50)),
                ('scoala', models.CharField(max_length=50)),
            ],
        ),
    ]