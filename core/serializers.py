from rest_framework import serializers
from .models import Movie,Person,Genre


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields=['movie_id','title','sipnosis','release_year','lenguage','top']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields= '__all__'

class GenerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields='__all__'
