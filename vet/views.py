from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Models
from .models import PetOwner, Pet

# Serializers
from .serializers import PetOwnersListSerializers, PetsListSerializers, PetOwnerSerializer


class PetOwnersListCreate(APIView):
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

    def post(self, request):
        serializer = PetOwnerSerializer(data = request.data)
        serializer.is_valid(raise_exceptions = True)
        created_instance = serializer.save()

        print(created_instance.__dict__)

        return Response({})


class PetOwnerDetailAPIView(APIView):
    
    serializer_class = PetOwnerSerializer

    def get(self, request, pk):

        owner = get_object_or_404(PetOwner, id=pk)
        serializer = self.serializer_class(owner)
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

