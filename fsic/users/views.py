from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers import UserProfileSerializer
from .models import UserProfile
from rest_framework import generics
from django.shortcuts import get_object_or_404

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


class UpdateUserProfile(generics.RetrieveUpdateAPIView):
    """
    Update a User Profile 
    """
    
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'player_id'

    def get_object(self):
        id = self.kwargs["player_id"]
        return get_object_or_404(UserProfile,player_id=id)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)




