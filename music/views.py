from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics ,filters
from .models import Songs
from rest_framework import status
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

class PostSongsView(APIView):
    def post(self,request ,*args,**kwargs):
        serializer = SongsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
