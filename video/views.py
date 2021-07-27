from rest_framework import viewsets
from video.serializer import VideoSerializer, CategorySerializer
from video.models import Video, Category


class VideoViewSet(viewsets.ModelViewSet):
    """Listing all videos"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """Listing all categories"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

