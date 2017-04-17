# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-25 22:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
        ('courses', '0002_auto_20170325_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assistant_courses', to='coaches.Coach'),
        ),
        migrations.AddField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coach_courses', to='coaches.Coach'),
        ),
    ]
