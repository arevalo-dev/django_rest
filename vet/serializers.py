from rest_framework import serializers
from .models import PetOwner, Pet, PetDate


class PetOwnersListModelSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = PetOwner
        fields = ('id', 'first_name', 'last_name')

class PetOwnerModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PetOwner
        fields = ('id', 'first_name', 'last_name', 'address', 'email', 'phone')

class PetListModelSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Pet
        fields = ('id', 'name', 'type')

class PetModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pet
        fields = ('id', 'name', 'type', 'owner')


class PetDatePetModelSerializer(serializers.ModelSerializer):
    
    pet = PetModelSerializer()

    class Meta:
        model = PetDate
        fields = ("id", "datetime", "type", "pet")


class PetDateModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = PetDate
        fields = ("id", "datetime", "type", "pet")

class PetDateUpdateModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PetDate
        fields = ("id", "datetime", "type")