# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-26 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20170325_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='courses.Course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='student',
            name='surname',
            field=models.CharField(max_length=64),
        ),
    ]
