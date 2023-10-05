from .models import Video
from rest_framework import serializers


class ValidateDataMixin:
    serializer_class_out = None
    serializer_class_in = None

    def get_serializer_class(self):
        if not self.serializer_class_out:
            raise NotImplementedError("You must define 'serializer_class_out' in your viewset.")
        return self.serializer_class_out

    def get_validate_data(self):
        if not self.serializer_class_in:
            raise NotImplementedError("You must define 'serializer_class_in' in your viewset.")
        serializer = self.serializer_class_in(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data


class VideoInputSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    disabled = serializers.BooleanField(required=False)


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ['name', 'disabled', 'focus']
