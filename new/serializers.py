from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    like_count = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'published_date', 'like_count']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'post', 'author', 'created_date']