from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import PropertyTypes
from .serializers import PropertyTypesSerializer

class PropertyTypesList(generics.ListAPIView):
    queryset = PropertyTypes.objects.all()
    serializer_class = PropertyTypesSerializer