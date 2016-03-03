# coding: utf-8
from rest_framework import serializers


class WorkoutDailySerializer(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.CharField()
