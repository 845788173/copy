# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-04 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lunbo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('img', models.CharField(max_length=255)),
            ],
        ),
    ]
