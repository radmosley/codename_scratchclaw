from rest_framework import serializers
from django.contrib.auth.models import User
from pets_api.models import Pet, Species

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ( 
            'species_name', 
            )
        
        model = Species

class NestedOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'username']
        model = User

class PetSerializer(serializers.ModelSerializer):
    pet_species = SpeciesSerializer()
    owner = NestedOwnerSerializer()
    class Meta:
        fields = ( 
            'owner',
            'pet_name', 
            'pet_species', 
            'level', 
            'strength', 
            'defense', 
            'hit_points', 
            'id'
            )
        
        model = Pet

