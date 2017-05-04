from django.contrib.auth.models import User, Group
from rest_framework import serializers, permissions
from .models import Profile

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def create(self, validated_data):
        u = User.objects.create_user(**validated_data)
        return u

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'