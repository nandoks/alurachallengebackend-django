from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from video.views import VideoViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('videos', VideoViewSet, basename='Videos')
router.register('categories', CategoryViewSet, basename='Categories')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
