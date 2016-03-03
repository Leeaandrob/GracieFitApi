# coding: utf-8
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import HomeContentApp


class HomeAppContentApiViewSet(APIView):
    def get(self, request):
        return Response([dict(
            image=h.image.url,
        ) for h in HomeContentApp.objects.all()], status.HTTP_200_OK)
