# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-17 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0003_auto_20170103_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='argument',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='type',
            field=models.CharField(default=b'github', editable=False, max_length=20),
        ),
    ]
