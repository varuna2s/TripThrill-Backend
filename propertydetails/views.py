from django.shortcuts import render
from rest_framework import generics
from .models import PropertyDetails
from .serializers import PropertyDeatilsSerializer

# Create your views here.
class PropertyDetailsfullList(generics.ListCreateAPIView):
    queryset=PropertyDetails.objects.all()
    serializer_class=PropertyDeatilsSerializer
    
class PropertyDetailsList(generics.RetrieveUpdateAPIView):
    queryset=PropertyDetails.objects.all()
    serializer_class=PropertyDeatilsSerializer

