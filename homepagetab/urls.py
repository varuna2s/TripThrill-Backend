from rest_framework import views
from . import views
from django.urls import path

urlpatterns = [
    path('propertytype/',views.PropertyTypesList.as_view()),
]