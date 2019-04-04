from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers import UserProfileSerializer
from .models import UserProfile
from rest_framework import generics

class UserProfileSearch(generics.ListAPIView):
    """ 
    List all the user profiles. 
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CreateUserProfile(generics.CreateAPIView):
    """
    Create new User profile (Update in phase 2 with user registrations)
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer



