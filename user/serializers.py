from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone_number', 'image'],


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']

    def create(self, validated_data):
        # Extract profile data from the request
        profile_data = validated_data.pop('profile', {})
        # Create the user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Create the associated profile
        Profile.objects.create(user=user, **profile_data)
        return user
    
    def update(self, instance, validated_data):
        # Extract profile data
        profile_data = validated_data.pop('profile', {})
        profile = instance.profile

        # Update user data
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        # Update profile data
        profile.phone_number = profile_data.get('phone_number', profile.phone_number)
        profile.address = profile_data.get('address', profile.address)
        profile.save()

        return instance



    