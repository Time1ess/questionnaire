# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 01:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schooladmin',
            name='user',
        ),
        migrations.DeleteModel(
            name='SchoolAdmin',
        ),
    ]