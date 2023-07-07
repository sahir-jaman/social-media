from rest_framework import serializers
from .models import User

class PublicUserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields=['email', 'name', 'password', 'confirm_password']
        extra_kwargs={
            'password':{'write_only': True}
        }

    def validate(self, attr):
        password = attr.get('password')
        password2 = attr.get('confirm_password')
        if password != password2:
            return serializers.ValidationError("password not matched")
        return attr

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class PrivateUserLogin_with_otp_Serializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=200)
    class Meta:
        model = User
        fields = ['email','otp']


class PrivateUserLogin_get_otp_Serializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=200)
    class Meta:
        model = User
        fields = ['email']

