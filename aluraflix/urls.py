from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from video.views import VideoViewSet, CategoryViewSet, ListVideosByCategory, ListVideosFree

router = routers.DefaultRouter()
router.register(r'videos', VideoViewSet, basename='Videos')
router.register(r'categories', CategoryViewSet, basename='Categories')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('category/<int:pk>/videos/', ListVideosByCategory.as_view()),
    path(r'videos/free/', ListVideosFree.as_view())
]
