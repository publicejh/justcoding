#serializer는 데이터를 json 형식으로 변환하는데 사용된다.

from rest_framework import serializers
from . import models
from .models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(use_url=True)
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        queryset = Comment.objects.filter(post=obj)
        return CommentSerializer(queryset, many=True).data

    class Meta:
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'image', 'file', 'comments', 'band_id', 'author')
        model = models.Post


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'message', 'created_at', 'post')
        model = models.Comment

