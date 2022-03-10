from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongSerializer
from .models import Song


class SongsList(APIView):
    # A class-based view that lists all songs or creates a new song

    def get(self, request, format=None):
        songs = Song.objects.all()
        # the following serializer is going to take our songs table and convert to json
        serializers = SongSerializer(songs, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializers = SongSerializer(data=request.data)
        # the following validates that API user input is true or accurate to the database
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)


class SongDetail(APIView):
    # A class-based view that retrieves (by id), updates, or deletes a song

    def get(self, request, pk, format=None):
        song = get_object_or_404(Song, pk=pk)
        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        song = get_object_or_404(Song, pk=pk)
        serializer = SongSerializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
