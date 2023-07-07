from rest_framework import serializers
from authentication.models import User

class PrivateUserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'is_active']