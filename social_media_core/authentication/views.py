import random
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .renderer import UserRenderer
from .models import User
from .serializers import (
    PublicUserRegistrationSerializer, PrivateUserLogin_with_otp_Serializer, PrivateUserLogin_get_otp_Serializer
)

# generate jwt token:
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# generating random 6 degit value
def generate_unique_id():
    while True:
        unique_id = random.randint(100000, 999999)
        # Check if the generated unique_id already exists in the database
        # You need to replace 'YourModel' with your actual model name
        if not User.objects.filter(otp=unique_id).exists():
            return unique_id

# Random people can enter and register
class PublicUserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, formate=None):
        serializer =PublicUserRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'Token': token, 'msg':'Registration succesful'}, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


# after getting the otp this task execute
class PrivateUserLoginView_with_otp(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, formate =None):
        serializer = PrivateUserLogin_with_otp_Serializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            # checking if the email exist in the database or not.
            email = serializer.data.get('email')
            otp = serializer.data.get('otp')
            # theUser = serializer.save()
            # token = get_tokens_for_user(user)
            try:
                user = User.objects.get(email=email)
                exists = True
            except User.DoesNotExist:
                exists = False
                user=None

            if exists and otp!=None:
                is_valid = True if email== email and otp == otp else False
                if is_valid:
                    token = get_tokens_for_user(user)
                    return Response({'Token': token, "success": "User Logged in Successfully"})
                else:
                    return Response({"msg": "Email or OTP not matched"})

            else:
                return Response({"Error":"Email or OTP not matched"})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# getting the OTP code using authenticated email
class PrivateUserLogin_get_otp(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, formate =None):
        serializer = PrivateUserLogin_get_otp_Serializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            # checking if the email exist in the database or not.
            email = serializer.data.get('email')
            new_otp = generate_unique_id()
            try:
                user = User.objects.get(email=email)
                exists = True
            except User.DoesNotExist:
                exists = False
                user=None

            if exists:
                # Create an instance of my model and assign the generated id
                model_instance = User.objects.get(email=email)
                model_instance.otp = new_otp
                model_instance.save()
                return HttpResponse(f"Auto-generated ID: {new_otp}")
            else:
                return Response({"Error":"There is no existing user found for this email"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

