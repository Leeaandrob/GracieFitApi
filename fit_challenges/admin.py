from django.contrib import admin

from .models import (Exercise, Workout, WorkoutRecipe, ImageExercise)


class ImageExerciseAdmin(admin.TabularInline):
    model = ImageExercise


class ExerciseAdmin(admin.ModelAdmin):
    inlines = [ImageExerciseAdmin]


class WorkoutRecipeAdmin(admin.ModelAdmin):
    list_filter = ['workout__name']


admin.site.register(Workout)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(WorkoutRecipe, WorkoutRecipeAdmin)
admin.site.register(ImageExercise)
