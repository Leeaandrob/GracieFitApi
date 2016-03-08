# coding: utf-8
from django.contrib import admin

from .models import GroupFood, TypeFood, Food


admin.site.register(GroupFood)
admin.site.register(TypeFood)
admin.site.register(Food)
