from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        # these correspond to the table's columns
        fields = ['id', 'title', 'artist',
                  'album', 'release_date', 'genre']
