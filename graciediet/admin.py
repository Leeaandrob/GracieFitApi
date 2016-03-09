# coding: utf-8
from django.contrib import admin

from .models import (GroupFood, Food, SubGroup)


admin.site.register(GroupFood)
admin.site.register(Food)
admin.site.register(SubGroup)
