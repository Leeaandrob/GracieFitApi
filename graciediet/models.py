from __future__ import unicode_literals

from django.db import models


class GroupFood(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class TypeFood(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=255)
    group_food = models.ForeignKey('GroupFood')
    type_food = models.ForeignKey('TypeFood', null=True, blank=True)

    def __unicode__(self):
        return self.name
