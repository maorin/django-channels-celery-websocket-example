# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 01:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0009_auto_20170105_0042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='confirmed_company_details',
        ),
        migrations.AddField(
            model_name='customer',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.Company'),
        ),
    ]