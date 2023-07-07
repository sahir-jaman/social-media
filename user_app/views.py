from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.renderer import UserRenderer
from authentication.models import User
from .serializers import (
    PrivateUserProfileDetailSerializer
)

# Only registered and OTP matched client can access
class PrivateUserProfileViewDetail(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, formate = None, pk = None):
        serializer = PrivateUserProfileDetailSerializer(request.user)
        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
