# coding: utf-8
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from homesite.views import HomesiteView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomesiteView.as_view()),
    url(r'^api/v1/', include('api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
