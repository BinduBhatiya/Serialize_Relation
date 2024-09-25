from django.shortcuts import render
from .serializers import SongSerializer,SingreSerializer
from rest_framework import viewsets
from .models import Singre,Song
# Create your views here.

class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singre.objects.all()
    serializer_class = SingreSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

