from rest_framework import viewsets, status, generics, filters
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from video.serializer import VideoSerializer, CategorySerializer, ListVideosByCategorySerializer, \
    ListVideoFreeSerializer
from video.models import Video, Category


class VideoViewSet(viewsets.ModelViewSet):
    """Listing all videos"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

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
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        """Deleting a category"""

        try:
            instance = self.get_object()
            # if instance.id == 1:
            #     return Response(status=status.HTTP_403_FORBIDDEN, data={"detail": "Category with id 1 cannot be deleted"})
            self.perform_destroy(instance)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "Category not found"})
        return Response(status=status.HTTP_200_OK, data={"detail": "Category successfuly deleted"})


class ListVideosByCategory(generics.ListAPIView):
    """Listing videos from a category"""

    def get_queryset(self):
        queryset = Video.objects.filter(category_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListVideosByCategorySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListVideosFree(generics.ListAPIView):
    """Listing a free version of the API returns only 5 videos"""
    queryset = Video.objects.all().order_by('-id')[:5]
    serializer_class = ListVideoFreeSerializer
    search_fields = ['title', 'description']