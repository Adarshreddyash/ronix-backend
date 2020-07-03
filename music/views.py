from django.shortcuts import render

# Create your views here.
from rest_framework import generics ,filters
from .models import Songs
from .serializers import SongsSerializer
from rest_framework import permissions


class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    permission_classes = (permissions.IsAuthenticated,)