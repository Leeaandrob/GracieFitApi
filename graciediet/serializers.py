from rest_framework import serializers


class FoodSerializer(serializers.Serializer):
    name = serializers.CharField()
