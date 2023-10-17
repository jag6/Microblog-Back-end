from .models import *
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer


class CommentSerializer(FlexFieldsModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    created_on = serializers.DateTimeField(format="%m/%d/%Y")

    class Meta:
        model = Comment
        fields = ('pk', 'body', 'author', 'created_on', 'post')

class TagSerializer(FlexFieldsModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ('pk', 'name', 'author', 'posts')

class LikeSerializer(FlexFieldsModelSerializer):
    liker = serializers.ReadOnlyField(source='liker.username')
    created_on = serializers.DateTimeField(format="%m/%d/%Y")

    class Meta:
        model = Like
        fields = ('pk', 'liker', 'created_on', 'post')

class PostSerializer(FlexFieldsModelSerializer):
    author = serializers.ReadOnlyField(source='author.username', read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    created_on = serializers.DateTimeField(format="%m/%d/%Y")
    
    class Meta:
        model = Post
        fields = ('pk', 'author', 'title', 'body', 'created_on', 'comments', 'tags', 'likes')
        expandable_fields = {
          'comments': (CommentSerializer, {'many': True}),
          'tags': (TagSerializer, {'many': True}),
          'likes': (LikeSerializer, {'many': True}),
        }