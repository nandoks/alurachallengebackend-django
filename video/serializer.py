from rest_framework import serializers

from video.models import Video
from video.validators import validate_titulo

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

    def validate(self, data):
        if not validate_titulo(data['title']):
            raise serializers.ValidationError({"title": "Title must have at least characters"})
        return data