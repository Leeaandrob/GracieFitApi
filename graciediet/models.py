from __future__ import unicode_literals

from django.db import models


class GroupFood(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class SubGroup(models.Model):
    name = models.CharField(max_length=255)
    group = models.ForeignKey('GroupFood')
    image = models.ImageField(upload_to='graciediet/')

    def __unicode__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=255)
    group_food = models.ForeignKey('GroupFood')
    sub_group = models.ForeignKey('SubGroup', null=True, blank=True)

    def __unicode__(self):
        return self.name
