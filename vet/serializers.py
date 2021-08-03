from rest_framework import serializers
from .models import PetOwner

class PetOwnersListSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    

class PetOwnerSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    address = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()

    def create(self, validated_data):
        return PetOwner.objects.create(**validated_data)

class PetsListSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    type = serializers.CharField()