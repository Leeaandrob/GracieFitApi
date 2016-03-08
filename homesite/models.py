from __future__ import unicode_literals

from django.db import models


class HomeContentApp(models.Model):
    image = models.ImageField(upload_to="homesite")
    title = models.CharField(max_length=255, default="")
