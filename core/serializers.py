# core/serializers.py, this file was created manually
from rest_framework import serializers
from .models import User, Song
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
 
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'