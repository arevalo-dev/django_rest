from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Models
from .models import PetOwner, Pet

# Serializers
from .serializers import (
    PetOwnersListModelSerializers,
    PetOwnerModelSerializer,
    PetListModelSerializers,
    PetModelSerializer
)


class PetOwnersListCreateAPIView(generics.ListCreateAPIView):
    
    queryset = PetOwner.objects.all()
    serializer_class = PetOwnersListModelSerializers

    def get_queryset(self):

        first_name_filter = self.request.GET.get("first_name")
        filters = {}
        if first_name_filter:
            filters["first_name__icontains"] = first_name_filter
        return self.queryset.filter(**filters)
    
    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = PetOwnerModelSerializer
        
        return serializer_class

class PetOwnersRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = PetOwnerModelSerializer



class PetListCreateAPIView(generics.ListCreateAPIView):
    
    queryset = Pet.objects.all()
    serializer_class = PetListModelSerializers

    def get_queryset(self):

        name_filter = self.request.GET.get("name")
        filters = {}
        if name_filter:
            filters["name__icontains"] = name_filter
        return self.queryset.filter(**filters)
    
    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = PetModelSerializer
        
        return serializer_class

class PetRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetModelSerializer
