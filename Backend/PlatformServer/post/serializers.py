from rest_framework import serializers
from . import models
from .models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    def get_author_name(self, obj):
        return obj.author.username

    def get_comments(self, obj):
        queryset = Comment.objects.filter(post=obj)
        return CommentSerializer(queryset, many=True).data

    class Meta:
        fields = ('id', 'content', 'created_at', 'updated_at', 'comments', 'band_id', 'author', 'author_name')
        model = models.Post


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    def get_author_name(self, obj):
        return obj.author.username

    class Meta:
        fields = ('id', 'author', 'message', 'created_at', 'post', 'author_name')
        model = models.Comment

