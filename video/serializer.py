from rest_framework import serializers

from video.models import Video, Category
from video.validators.video import validate_title, validate_description
from video.validators.category import validate_hexadecimal


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

    def validate(self, data):
        if not validate_title(data['title']):
            raise serializers.ValidationError({"title": "Title must have at least 5 characters"})
        if not validate_description(data['description']):
            raise serializers.ValidationError({"description": "Description must have at least 10 characters"})
        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate(self, data):
        if not validate_hexadecimal(data['color']):
            raise serializers.ValidationError({"color": "Color must be a hexadecimal value e.g. #959595 "})
        return data
