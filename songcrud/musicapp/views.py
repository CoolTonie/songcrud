from rest_framework import viewsets
from .models import artiste, song, lyric
from .serializers import ArtisteSerializers, SongSerializers, LyricSerializers

class ArtisteView(viewsets.ModelViewSet):
    queryset=artiste.objects.all()
    serializer_class=ArtisteSerializers


class SongView(viewsets.ModelViewSet):
    queryset=song.objects.all()
    serializer_class=SongSerializers


class LyricView(viewsets.ModelViewSet):
    queryset=artiste.objects.all()
    serializer_class=LyricSerializers


