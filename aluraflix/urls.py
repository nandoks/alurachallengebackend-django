from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from video.views import VideoViewSet

router = routers.DefaultRouter()
router.register('videos', VideoViewSet, basename='Videos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
