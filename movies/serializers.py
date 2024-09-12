from rest_framework import serializers

from .models import Movie, Comment

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'poster', 'release_date']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'movie', 'text', 'created_at']
