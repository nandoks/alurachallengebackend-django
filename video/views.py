from rest_framework import viewsets, status
from rest_framework.response import Response

from video.serializer import VideoSerializer, CategorySerializer
from video.models import Video, Category


class VideoViewSet(viewsets.ModelViewSet):
    """Listing all videos"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            return Video.objects.get(pk=self.kwargs['pk'])
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'detail': 'Video not found'})

    def destroy(self, request, *args, **kwargs):
        """Deleting a video"""
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "Vídeo not found"})
        return Response(status=status.HTTP_200_OK, data={"detail": "Vídeo successfuly deleted"})


class CategoryViewSet(viewsets.ModelViewSet):
    """Listing all categories"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            return Category.objects.get(pk=self.kwargs['pk'])
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'detail': 'Category not found'})

    def destroy(self, request, *args, **kwargs):
        """Deleting a video"""
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "Category not found"})
        return Response(status=status.HTTP_200_OK, data={"detail": "Category successfuly deleted"})
