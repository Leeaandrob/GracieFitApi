from rest_framework import serializers
from .models import UserBase


class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserBase
        fields = ("email", "first_name", "last_name")


class RegisterSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()


class AuthSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
