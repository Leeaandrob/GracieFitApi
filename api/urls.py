# coding: utf-8
from django.conf.urls import include, url

from rest_framework import routers

from core import views


router = routers.DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', views.AuthView.as_view()),
    url(r'^register/', views.RegisterView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]
