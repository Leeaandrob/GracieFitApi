# coding: utf-8
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from homesite.views import HomesiteView
from core import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', views.AuthView.as_view()),
    url(r'^register/', views.RegisterView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomesiteView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]
