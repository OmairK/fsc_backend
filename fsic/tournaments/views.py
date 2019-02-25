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
    
    queryset = TournamentITF.objects.all()
    serializer_class = TournamentITFSerializer 

class TournamentsListFSC(generics.CreateAPIView):
    queryset = TournamentFSC.objects.all()
    serializer_class = TournamentFSCSerializer

class PlayerRankingMS(generics.CreateAPIView):
    
    queryset = PlayerRankingsMS.objects.all()
    serializer_class = PlayerRankingsSerializerMS

class PlayerRankingMD(generics.CreateAPIView):
    
    queryset = PlayerRankingsMD.objects.all()
    serializer_class = PlayerRankingsSerializerMD

class PlayerRankingFS(generics.CreateAPIView):
    
    queryset = PlayerRankingsFS.objects.all()
    serializer_class = PlayerRankingsSerializerFS

class PlayerRankingFD(generics.CreateAPIView):
    
    queryset = PlayerRankingsFD.objects.all()
    serializer_class = PlayerRankingsSerializerFD

    




# Create your views here.
