# core/serializers.py, this file was created manually
from rest_framework import serializers
from .models import User, Song, Playlist, Detailpl
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
 
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'
 
class DetailplSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detailpl
        fields = '__all__'