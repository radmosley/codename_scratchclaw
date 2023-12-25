from .models import Pet, Species
from rest_framework import status
# from django.http import Http404

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import PetSerializer, SpeciesSerializer

# Pokemon end points
class PetListViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def list(self, request):
        serializer = PetSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        pet = get_object_or_404(self.queryset, pk=pk)
        serializer = PetSerializer(pet)
        return Response(serializer.data)
    
    
class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

    def list(self, request):
        serializer = SpeciesSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        species = get_object_or_404(self.queryset, pk=pk)
        serializer = SpeciesSerializer(species)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SpeciesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)