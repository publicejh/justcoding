from .models import ImageInfo, ChatImageInfo
from rest_framework import serializers


class ImageInfoSerializer(serializers.ModelSerializer):
    photo_thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        fields = ('user', 'band', 'photo', 'photo_thumbnail', )
        model = ImageInfo


class ChatImageInfoSerializer(serializers.ModelSerializer):
    photo_thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        fields = ('user', 'chat', 'photo', 'photo_thumbnail', )
        model = ChatImageInfo
