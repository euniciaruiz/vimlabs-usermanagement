from django.contrib.auth.models import User, Group
from rest_framework import serializers, permissions
from .models import Profile
import datetime
import hashlib
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def create(self, validated_data):
        profile_data = self.to_internal_value(validated_data)

        password = validated_data.pop('password', None)
        role = validated_data.pop('role')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        self.create_profile(profile_data)
        return instance
    
    def create_profile(self, role):
        data = {
            'first_name': role.get('first_name'),
            'last_name': role.get('last_name'),
            'username': role.get('username'),
            'password': role.get('password'),
            'email': role.get('email'),
            'role': role.get('role')
        }
        print(role.get('role'))
        new_profile = Profile.objects.create(**data)
        new_profile.save()       

    def to_internal_value(self, data):
        internal_value = super(UserSerializer, self).to_internal_value(data)
        role_raw_value = data.get("role")
        internal_value.update({
            "role": role_raw_value
        })
        return internal_value

    # def update(self, instance, validated_data):
    #     # password = validated_data.pop('password', None)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.email = "updated@gmail.com"
    #     instance.set_password(validated_data.get('password'))
    #     instance.save()
    #     print('hellooooo')
    #     return instance

    

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('uid', 'first_name', 'last_name', 'username', 'email', 'password', 'role')
    
    def update(self, instance, validated_data):
        curr_email = instance.email
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.password = validated_data.get('password')
        instance.role = validated_data.get('role')
        instance.save()
        r = validated_data.pop('role')
        user = User.objects.filter(email=curr_email).update(**validated_data)
        return instance

    
    