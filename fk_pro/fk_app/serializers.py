from rest_framework import serializers
from .models import Singre,Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'singre', 'duration']

class SingreSerializer(serializers.ModelSerializer):
    song = serializers.StringRelatedField(many=True, read_only=True)
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # song_title ID is defined.
    # song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')
    # song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    # song = serializers.HyperlinkedIdentityField(view_name='song-detail')


    class Meta:
        model = Singre
        fields = ['id', 'name', 'song']
