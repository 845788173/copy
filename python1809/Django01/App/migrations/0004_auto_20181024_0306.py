# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-24 03:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20181024_0240'),
    ]

    operations = [
        migrations.CreateModel(
            name='IDCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_num', models.CharField(max_length=40)),
                ('i_addr', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=80)),
                ('p_age', models.IntegerField()),
            ],
        ),
        migrations.AlterModelManagers(
            name='dog',
            managers=[
                ('myobjects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='idcard',
            name='i_person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='App.Person'),
        ),
    ]
