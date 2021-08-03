from rest_framework import serializers
from .models import PetOwner, Pet

# class PetOwnersListSerializers(serializers.Serializer):
#     id = serializers.IntegerField()
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()

class PetOwnersListSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = PetOwner
        fields = ('id', 'first_name', 'last_name')



# class PetOwnerSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     first_name = serializers.CharField(max_length=255)
#     last_name = serializers.CharField(max_length=255)
#     address = serializers.CharField()
#     email = serializers.EmailField()
#     phone = serializers.CharField()

#     def create(self, validated_data):
#         return PetOwner.objects.create(**validated_data)
class PetOwnerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PetOwner
        fields = ('id', 'first_name', 'last_name', 'address', 'email', 'phone')




class PetOwnerUpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255, required=False)
    last_name = serializers.CharField(max_length=255, required=False)
    address = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance



# class PetsListSerializers(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     type = serializers.CharField()
class PetsListSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Pet
        fields = ('id', 'name', 'type')


# class PetSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     name = serializers.CharField()
#     type = serializers.ChoiceField(choices=Pet.PET_TYPES)
#     owner_id = serializers.IntegerField()

#     def create(self, validated_data):
#         return Pet.objects.create(**validated_data)

class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = ('id', 'name', 'type', 'owner_id')


class PetUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    type = serializers.CharField(required=False)
    owner_id = serializers.IntegerField(required=False)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.owner_id = validated_data.get('owner_id', instance.owner_id)
        instance.save()

        return instance