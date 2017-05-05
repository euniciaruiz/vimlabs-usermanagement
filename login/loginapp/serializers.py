from django.contrib.auth.models import User, Group
from rest_framework import serializers, permissions
from .models import Profile

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def create(self, validated_data):
        u = User.objects.create_user(**validated_data)
        return u
    def update(self, instance, validated_data):
        # u = User.objects.get(id=instance.id)
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance
        
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'