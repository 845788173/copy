# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-04 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_goods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='g_price',
            field=models.CharField(max_length=60),
        ),
    ]
