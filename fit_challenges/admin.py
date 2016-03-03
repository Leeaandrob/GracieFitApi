from django.contrib import admin

from .models import Exercise, Workout, WorkoutRecipe


class WorkoutRecipeAdmin(admin.ModelAdmin):
    list_filter = ['workout__name']


admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(WorkoutRecipe, WorkoutRecipeAdmin)
