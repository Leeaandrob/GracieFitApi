# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-03 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeContentApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='homesite')),
                ('text', models.TextField()),
            ],
        ),
    ]
