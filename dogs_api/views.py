from django.shortcuts import render

# from django.db.models.query import QuerySet

from django.shortcuts import render

# The views i created
from rest_framework import generics
from .serializers import DogSerializer
from .models import Dog


# generics.ListCreateAPIView will be inherited by DogList

# will either display all Contacts in the DB or create a new one
class DogList(generics.ListCreateAPIView):
    # tell django how to retrieve all objects from the DB, order by id ascending
    queryset = Dog.objects.all().order_by('id')
    # tell django what serializer to use
    serializer_class = DogSerializer

# generics.RetrieveUpdateDestroyAPIView will be inherited by ContactDetail

# will either update or delete a contact in the DB
class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    querySet = Dog.objects.all().order_by('id')
    serializer_class = DogSerializer

