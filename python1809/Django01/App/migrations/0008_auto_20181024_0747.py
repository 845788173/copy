# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-24 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_auto_20181024_0647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_name', models.CharField(max_length=100)),
                ('g_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=100)),
                ('u_tel', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='g_user',
            field=models.ManyToManyField(to='App.User'),
        ),
    ]
