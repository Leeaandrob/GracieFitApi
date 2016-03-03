# coding: utf-8
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import WorkoutRecipe, Workout
from .serializers import WorkoutDailySerializer


class WorkoutApiViewSet(APIView):
    def get(self, request):
        return Response([dict(
            name=w.name,
            description=w.description,
            is_premium=w.is_premium,
        ) for w in Workout.objects.all()])


class WorkoutRecipeApiViewSet(APIView):
    serializer_class = WorkoutDailySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            name = serializer.data.get('name')
            id = serializer.data.get('id')

            return Response([dict(
                order=e.order,
                quantity_exercises=e.quantity,
                workout=e.workout.name,
                exercise_name=e.exercise.name,
                exercise_type=e.exercise.type,
                exercise_image=e.exercise.image,
                exercise_description=e.exercise.description)
                for e in WorkoutRecipe.objects.filter(
                    name=name, id=id)],
                status.HTTP_200_OK)
        return Response('fail', status.HTTP_400_BAD_REQUEST)
