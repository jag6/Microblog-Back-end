from .models import *
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username', read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    created_on = serializers.DateTimeField(format="%m/%d/%Y")
    
    class Meta:
        model = Post
        fields = ('pk', 'author', 'title', 'body', 'created_on', 'comments')

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    created_on = serializers.DateTimeField(format="%m/%d/%Y")

    class Meta:
        model = Comment
        fields = ('pk', 'body', 'author', 'created_on', 'post')