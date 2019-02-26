from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse
from bson import Binary, Code
from bson.json_util import dumps
from tournaments.serializers import *
from tournaments.models import *

class TournamentsListITF(generics.CreateAPIView):
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

class PlayerRankingMS(generics.CreateAPIView):
    """
    Create new Player Ranking Male Singles instance
    """
    queryset = PlayerRankingsMS.objects.all()
    serializer_class = PlayerRankingsSerializerMS

class PlayerRankingMD(generics.CreateAPIView):
    """
    Create new Player Ranking Male Doubles instance
    """
    queryset = PlayerRankingsMD.objects.all()
    serializer_class = PlayerRankingsSerializerMD

class PlayerRankingFS(generics.CreateAPIView):
    """
    Create new Player Ranking Female Singles instance
    """
    queryset = PlayerRankingsFS.objects.all()
    serializer_class = PlayerRankingsSerializerFS

class PlayerRankingFD(generics.CreateAPIView):
    """
    Create new Player Ranking Female Doubles instance
    """
    queryset = PlayerRankingsFD.objects.all()
    serializer_class = PlayerRankingsSerializerFD


# Create your views here.
