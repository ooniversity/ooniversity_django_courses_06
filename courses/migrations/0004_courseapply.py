# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20170325_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('level', models.CharField(max_length=10)),
                ('comment', models.TextField()),
                ('is_active', models.BooleanField()),
                ('date_apply', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
