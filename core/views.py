# coding: utf-8
from django.contrib.auth import login, logout, authenticate

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import UserBase
from .serializers import (UserSerializers, RegisterSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserBase.objects.all()
    serializer_class = UserSerializers


class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def get_user(self, email):
        try:
            return UserBase.objects.get(email=email)
        except UserBase.DoesNotExist:
            return None

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            pswd = serializer.data.get('password')

            user = self.get_user(serializer.data.get('email'))
            if user:
                return Response(
                    {"message": "Email already exists"},
                    status=status.HTTP_406_NOT_ACCEPTABLE
                )
            else:
                new_user = UserBase.objects.create(
                    email=email, password=pswd)
                new_user.set_password(pswd)
                new_user.save()
                return Response(
                    {"message": "User Created"}, status=status.HTTP_201_CREATED
                )


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
