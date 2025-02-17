from rest_framework import serializers
from .models import Movie, Director, Review

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = "id name movies_count".split()

    def get_movies_count(self, obj):
        return obj.movies.count()

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Name must be at least 3 characters long")
        return value


class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "id title description duration director average_rating".split()

    def get_average_rating(self, obj):
        return obj.average_rating
    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Title must be at least 2 characters long")
        return value

    def validate_duration(self, value):
        if len(value) <= 0:
            raise serializers.ValidationError("Duration must be a positive integer.")


class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())

    class Meta:
        model = Review
        fields = "id text stars movie ".split()
