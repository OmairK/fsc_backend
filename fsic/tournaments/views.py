from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pymongo import MongoClient
from django.http import HttpResponse
from bson import Binary, Code
from bson.json_util import dumps
from tournaments.serializers import *
from tournaments.models import *
class TournamentsListITF(ListCreateAPIView):
    
    queryset = TournamentITF.objects.all()
    serializer_class = TournamentITFSerializer 

class TournamentsListFSC(ListCreateAPIView):
    queryset = TournamentFSC.objects.all()
    serializer_class = TournamentFSCSerializer

class PlayerRankingMS(ListCreateAPIView):
    
    queryset = PlayerRankingsMS.objects.all()
    serializer_class = PlayerRankingsSerializer

class PlayerRankingMD(ListCreateAPIView):
    
    queryset = PlayerRankingsMD.objects.all()
    serializer_class = PlayerRankingsSerializer

class PlayerRankingFS(ListCreateAPIView):
    
    queryset = PlayerRankingsFS.objects.all()
    serializer_class = PlayerRankingsSerializer

class PlayerRankingFD(ListCreateAPIView):
    
    queryset = PlayerRankingsFD.objects.all()
    serializer_class = PlayerRankingsSerializer

    




# Create your views here.
