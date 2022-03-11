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

    def delete(self, request, pk, format=None):
        song = get_object_or_404(Song, pk=pk)
        song.delete()
        # self-note: regarding the return, the user story stated to return a 200 status code; however, I typically had put a 204 NO CONTENT code
        return Response(status=status.HTTP_200_OK)


class SongLike(APIView):
    # A class-based view to add a "like" to a song

    # self-note: For the following function, the G4G reference https://www.geeksforgeeks.org/handling-ajax-request-in-django/ reflected a GET method request
    # However, it was advised by our instructor to use a PUT request which makes more sense
    def put(self, request, pk, format=None):
        song = get_object_or_404(Song, pk=pk)
        serializer = SongSerializer(song)
        song.likes += 1
        song.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
