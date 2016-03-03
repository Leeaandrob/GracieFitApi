# coding: utf-8
from django.conf.urls import include, url

from rest_framework import routers

from homesite.apis import HomeAppContentApiViewSet
from core import views
from fit_challenges.apis import (WorkoutApiViewSet, WorkoutRecipeApiViewSet,
                                 ExerciseApiViewSet)


router = routers.DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', views.AuthView.as_view()),
    url(r'^register/', views.RegisterView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^home/', HomeAppContentApiViewSet.as_view()),
    url(r'^workouts', WorkoutApiViewSet.as_view()),
    url(r'^workout_recipe/', WorkoutRecipeApiViewSet.as_view()),
    url(r'^exercise/', ExerciseApiViewSet.as_view()),
]
