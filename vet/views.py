from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Models
from .models import PetOwner, Pet

# Serializers
from .serializers import (
    PetOwnersListSerializers, 
    PetsListSerializers, 
    PetOwnerSerializer, 
    PetSerializer, 
    PetOwnerUpdateSerializer, 
    PetUpdateSerializer
)


class PetOwnersListAPIView(generics.ListAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = PetOwnersListSerializers


# class PetOwnersListCreate(APIView):
#     """
#     View to list all pet owners in the system.
#     """

#     serializer_class = PetOwnersListSerializers

#     def get(self, request):
#         owners_queryset = PetOwner.objects.all()
#         serializer = self.serializer_class(owners_queryset, many=True)
#         return Response(serializer.data)

#     def post(self, request):

#         serializer = PetOwnerSerializer(data = request.data)
#         serializer.is_valid(raise_exception = True)
#         created_instance = serializer.save()
#         serialized_instance = PetOwnerSerializer(created_instance)

#         return Response(serialized_instance.data, status=status.HTTP_201_CREATED)

# class PetOwnerRetrieveUpdateDestroyAPIView(APIView):
    
#     serializer_class = PetOwnerSerializer

#     def get(self, request, pk):

#         owner = get_object_or_404(PetOwner, id=pk)
#         serializer = self.serializer_class(owner)

#         return Response(serializer.data)


#     def patch(self, request, pk):
#         owner = get_object_or_404(PetOwner, id=pk)
#         serializer = PetOwnerUpdateSerializer(instance=owner, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         update_instance = serializer.save()
#         serialized_instance = self.serializer_class(update_instance)
        
#         return Response(serialized_instance.data)
    
#     def delete(self, request, pk):
#         owner = get_object_or_404(PetOwner, id=pk)
#         owner.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)

class PetsListAPIView(generics.ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsListSerializers

# class PetsListCreate(APIView):
#     """
#     View to list all pets in the system.
#     """

#     serializer_class = PetsListSerializers

#     def get(self, request):
#         pets_queryset = Pet.objects.all()
#         serializer = self.serializer_class(pets_queryset, many=True)
#         return Response(serializer.data)

#     def post(self, request):
    
#         serializer = PetSerializer(data = request.data)
#         serializer.is_valid(raise_exception = True)
#         created_instance = serializer.save()
#         serialized_instance = PetSerializer(created_instance)

#         return Response(serialized_instance.data, status=status.HTTP_201_CREATED)


# class PetsRetrieveUpdateDestroyAPIView(APIView):
    
#     serializer_class = PetSerializer

#     def get(self, request, pk):

#         owner = get_object_or_404(Pet, id=pk)
#         serializer = self.serializer_class(owner)

#         return Response(serializer.data)

#     def patch(self, request, pk):
#         owner = get_object_or_404(Pet, id=pk)
#         serializer = PetUpdateSerializer(instance=owner, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         update_instance = serializer.save()
#         serialized_instance = self.serializer_class(update_instance)
        
#         return Response(serialized_instance.data)


#     def delete(self, request, pk):
#         owner = get_object_or_404(Pet, id=pk)
#         owner.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)