from .models import Profile
# from rest_framework import status
# from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import AccountSerializer
from .serializers import RegisterSerializer
from rest_framework import generics

# Create your views here.
class AccountListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    
    def list(self, request):
        serializer = AccountSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        account = get_object_or_404(self.queryset, pk=pk)
        serializer = AccountSerializer(account)
        return Response(serializer.data)



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer