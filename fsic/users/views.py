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


    



