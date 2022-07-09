"""
Creating endpoints 
"""
from django.shortcuts import render
from rest_framework import generics
from . import serializers
from . import models


class RoomView(generics.CreateAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializers
