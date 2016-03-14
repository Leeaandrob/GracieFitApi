# coding: utf-8
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (Food, SubGroup)
from .serializers import FoodSerializer


class SubGroupApiviewSet(APIView):
    def _get_sub_groups(self):
        return SubGroup.objects.all().order_by('name')

    def get(self, request):
        subs = self._get_sub_groups()
        if subs:
            return Response([dict(
                name=g.name,
                image=g.image.url,
            ) for g in subs], status.HTTP_200_OK)
        return Response('fail', status.HTTP_400_BAD_REQUEST)


class FoodApiViewSet(APIView):
    serializer_class = FoodSerializer

    def _get_foods(self, name):
        return Food.objects.filter(sub_group__name=name).order_by('name')

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            name = serializer.data.get('name')
            foods = self._get_foods(name)

            if foods:
                return Response([dict(
                    name=f.name,
                    type=f.sub_group.name,
                    group=f.group_food.name,
                    image=f.sub_group.image.url,
                ) for f in foods], status.HTTP_200_OK)
        return Response('fail', status.HTTP_400_BAD_REQUEST)
