from rest_framework import views
from . import views
from django.urls import path

urlpatterns = [
    path('propertydetails/',views.PropertyDetailsfullList.as_view()),
    path('propertydetails/<pk>',views.PropertyDetailsList.as_view()),
]