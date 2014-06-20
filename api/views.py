from django.shortcuts import render
from django.contrib.auth.models import User, Group
from misc.models import Migrant, Abuse, CheckPoint

from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, AbuseSerializer, CheckPointSerializer, MigrantSerializer
from api.permissions import IsSuperUserOrReadOnly
from rest_framework import permissions
from rest_framework import generics

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MigrantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = (permissions.AllowAny,)
    allowed_methods = ('POST',)                
    queryset = Migrant.objects.all()
    serializer_class = MigrantSerializer

class AbuseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = (permissions.AllowAny,)
    allowed_methods = ('POST',)            
    queryset = Abuse.objects.all()
    serializer_class = AbuseSerializer

class CheckPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = (permissions.AllowAny,)
    allowed_methods = ('POST',)            
    queryset = CheckPoint.objects.all()
    serializer_class = CheckPointSerializer
   
