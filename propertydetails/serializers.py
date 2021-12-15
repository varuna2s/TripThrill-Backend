from django.db.models import fields
from rest_framework import serializers
from .models import PropertyDetails

class PropertyDeatilsSerializer(serializers.ModelSerializer):
    class Meta:
        model=PropertyDetails
        fields='__all__'