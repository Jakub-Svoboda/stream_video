from .models import Video
from rest_framework import serializers


class VideoInputSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    disabled = serializers.BooleanField(required=False)


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ['name', 'disabled', 'focus']
