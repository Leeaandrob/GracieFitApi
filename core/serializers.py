from rest_framework import serializers
from .models import UserBase



class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserBase
        fields = ("email", "first_name", "last_name")
