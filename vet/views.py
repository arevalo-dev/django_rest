from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

# Models
from .models import PetOwner, Pet

# Serializers
from .serializers import PetOwnersListSerializers, PetsListSerializers


class PetOwnersList(APIView):
    """
    View to list all pet owners in the system.
    """

    serializer_class = PetOwnersListSerializers

    def get(self, request):
        # owners = [ 
        #     {
        #         "id": owner.id, 
        #         "first_name": owner.first_name
        #     } 
        #         for owner in PetOwner.objects.all()
        #     ]

        owners_queryset = PetOwner.objects.all()
        serializer = self.serializer_class(owners_queryset, many=True)

        return Response(serializer.data)






class PetsList(APIView):
    """
    View to list all pets in the system.
    """

    serializer_class = PetsListSerializers

    def get(self, request):
        # pets = [ 
        #     {
        #         "id": pet.id, 
        #         "name": pet.name, 
        #         "type": pet.type, 
        #         "owner": f"{pet.owner.first_name} {pet.owner.last_name}",
        #     }
        #     for pet in Pet.objects.all()
        #     ]

        pets_queryset = Pet.objects.all()
        serializer = self.serializer_class(pets_queryset, many=True)

        return Response(serializer.data)