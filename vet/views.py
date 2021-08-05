from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Models
from .models import PetOwner, Pet, PetDate

# Serializers
from .serializers import (
    PetOwnersListModelSerializers,
    PetOwnerModelSerializer,
    PetListModelSerializers,
    PetModelSerializer,
    PetDateModelSerializer,
    PetDateUpdateModelSerializer,
    PetDatePetModelSerializer
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



################################################################################
class PetDateListAPIView(generics.ListAPIView):
    queryset = PetDate.objects.all()
    serializer_class = PetDateModelSerializer

class PetDateCreateAPIView(generics.CreateAPIView):
    queryset = PetDate.objects.all()
    serializer_class = PetDateModelSerializer

class PetDateRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PetDate.objects.all()
    serializer_class = PetDateUpdateModelSerializer

class PetDateRetrievePet(generics.ListAPIView):
    queryset = PetDate.objects.all()
    serializer_class = PetDatePetModelSerializer

    def get_queryset(self):
        pet_id = self.request.GET.get("pet")
        owner_id = self.request.GET.get("owner")
        filters = {}
        if pet_id:
            filters["pet_id"] = pet_id

        if owner_id:
            filters["pet__owner_id"] = owner_id

        return self.queryset.filter(**filters)