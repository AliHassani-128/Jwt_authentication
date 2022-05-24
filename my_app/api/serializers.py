from urllib import request
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(write_only=True, required=True, style={'placeholder': 'Username'})
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password', \
                                                                            'placeholder': 'Password'})
    class Meta:
        model = User
        fields = ['username', 'password']
    

    def validate(self, attrs):
        try:
            user = User.objects.get(username=attrs['username'])
        except User.DoesNotExist:
            raise serializers.ValidationError({"error":'user with this username does not exists!'})
        return {'user': user}

class UserRegisterSerializer(serializers.ModelSerializer):

    username = serializers.CharField(write_only=True, required=True, style={'placeholder': 'Username'})
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password', \
                                                                            'placeholder': 'Password'})
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],
                                           password=make_password(validated_data['password']),
                                           )
        return user

    def validate(self, attrs):
        try:
            user = User.objects.get(username=attrs['username'])
            raise serializers.ValidationError({"username":'username is repetitive'})
        except User.DoesNotExist:
            return attrs



