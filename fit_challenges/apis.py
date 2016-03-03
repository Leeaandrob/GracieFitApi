# coding: utf-8
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import WorkoutRecipe, Workout, Exercise
from .serializers import WorkoutDailySerializer, ExerciseSerializer


class WorkoutApiViewSet(APIView):
    def get(self, request):
        return Response([dict(
            id=w.id,
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

            return Response([dict(
                order=e.order,
                quantity_exercises=e.quantity,
                workout=e.workout.name,
                exercise_name=e.exercise.name,
                exercise_type=e.exercise.type,
                exercise_image=e.exercise.image.url,
                exercise_description=e.exercise.description,
                exercise_id=e.exercise.id,
            )
                for e in WorkoutRecipe.objects.filter(
                    workout__name=name)],
                status.HTTP_200_OK)
        return Response('fail', status.HTTP_400_BAD_REQUEST)


class ExerciseApiViewSet(APIView):
    serializer_class = ExerciseSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            id = serializer.data.get('id')
            exercise = Exercise.objects.get(id=id)
            return Response(dict(name=exercise.name), status.HTTP_200_OK)
        return Response('fail', status.HTTP_400_BAD_REQUEST)
