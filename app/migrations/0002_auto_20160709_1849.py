# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-09 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_Completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='table_Paid',
            field=models.BooleanField(default=False),
        ),
    ]