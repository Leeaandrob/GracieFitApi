# coding: utf-8
from __future__ import unicode_literals

from django.db import models


class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    is_premium = models.BooleanField()

    def __unicode__(self):
        return self.name


class Exercise(models.Model):
    CHOICES_TYPE = (
        ('Seconds', 'Seconds'),
        ('Repeats', 'Repeat')
    )

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=255, choices=CHOICES_TYPE)

    def __unicode__(self):
        return "{0}-{1}".format(self.name, self.type)


class WorkoutRecipe(models.Model):
    order = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    workout = models.ForeignKey('Workout')
    exercise = models.ForeignKey('Exercise')

    def __unicode__(self):
        return "{0}-{1}-{2}{3}".format(self.workout.name,
                                       self.exercise.name,
                                       self.quantity,
                                       self.exercise.type)


class ImageExercise(models.Model):
    image = models.ImageField(upload_to="fit_challenges/")
    exercise = models.ForeignKey('Exercise', related_name="imagexercise")

    def __unicode__(self):
        return self.exercise.name
