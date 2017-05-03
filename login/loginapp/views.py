# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.models import User, Group
from .models import Profile
from rest_framework import viewsets
from loginapp.serializers import UserSerializer, GroupSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated)    
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer