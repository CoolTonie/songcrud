from rest_framework import serializers
from .models import artiste, song, lyric

class ArtisteSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=artiste
        fields= '__all__'


class SongSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=song
        fields= '__all__'


class LyricSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=lyric
        fields= '__all__'

