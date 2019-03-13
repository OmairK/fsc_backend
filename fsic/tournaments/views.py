from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse
from tournaments.serializers import *
from tournaments.models import *

class TournamentsListITF(generics.ListAPIView):
    """
    Create new ITF (International Tennis Federation) Tournament instance
    """
    queryset = TournamentITF.objects.all()
    serializer_class = TournamentITFSerializer 

class TournamentsListFSC(generics.CreateAPIView):
    """
    Create new FSC Tournament instance
    """
    queryset = TournamentFSC.objects.all()
    serializer_class = TournamentFSCSerializer

class PlayerRankingMS(generics.ListAPIView):
    """
    Create new Player Ranking Male Singles instance
    """
    queryset = PlayerRankingsMS.objects.all()
    serializer_class = PlayerRankingsSerializerMS

class PlayerRankingMD(generics.ListAPIView):
    """
    Create new Player Ranking Male Doubles instance
    """
    queryset = PlayerRankingsMD.objects.all()
    serializer_class = PlayerRankingsSerializerMD



# Create your views here.
