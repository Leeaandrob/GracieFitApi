# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-03 17:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homesite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homecontentapp',
            name='text',
        ),
    ]