# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-03 18:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fit_challenges', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='workout',
        ),
        migrations.AddField(
            model_name='workoutrecipe',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fit_challenges.Exercise'),
        ),
        migrations.AddField(
            model_name='workoutrecipe',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fit_challenges.Workout'),
        ),
    ]