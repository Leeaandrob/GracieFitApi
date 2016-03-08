# coding: utf-8
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Food


class FoodApiViewSet(APIView):
    def _get_foods(self):
        return Food.objets.all().order_by('name')

    def get(self, request):
        foods = self._get_foods()
        if foods:
            return Response([dict(
                name=f.name,
                type=f.type_food.name,
                group=f.group_food.name,
            ) for f in foods], status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)
