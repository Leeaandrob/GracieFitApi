
from django.contrib.auth import login, logout, authenticate
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserBase
from .serializers import UserSerializers



class UserViewSet(viewsets.ModelViewSet):
    queryset = UserBase.objects.all()
    serializer_class = UserSerializers



class AuthView(APIView):

    def post(self, request):
        email = request.POST.get("email")
        pswd = request.POST.get("password")
        user = authenticate(email=email, password=pswd)
        if user:
            if user.is_active:
                login(request, user)
                return Response(
                    {"message": "Loggin successful"}, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"message": "User is not activated"},
                    status=status.HTTP_401_UNAUTHORIZED
                )
        else:
            return Response(
                {"message": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request):
        logout(request)
        return Response({"message": "Goodbye"}, status=status.HTTP_200_OK)
