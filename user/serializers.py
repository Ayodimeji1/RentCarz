from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="profile.role", read_only=True)  # For Option 2

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role', 'phone_number', 'image']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create user and assign role
        role = validated_data.pop('role', 'customer')  # Default to customer
        user = User.objects.create_user(**validated_data)
        if hasattr(user, 'profile'):  # For Option 2
            user.profile.role = role
            user.profile.save()
        else:  # For Option 1
            user.role = role
            user.save()
        return user
