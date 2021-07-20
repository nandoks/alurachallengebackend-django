from rest_framework import viewsets
from video.serializer import VideoSerializer
from video.models import Video


class VideoViewSet(viewsets.ModelViewSet):
    """Listing all videos"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

