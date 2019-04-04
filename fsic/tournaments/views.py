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
    List all ITF (International Tennis Federation) Tournaments
    """
    queryset = TournamentITF.objects.all().order_by('start_date')
    serializer_class = TournamentITFSerializer 

class TournamentsListFSC(generics.ListAPIView):
    """
    List FSC Tournaments
    """
    queryset = TournamentFSC.objects.all()
    serializer_class = TournamentFSCSerializer

class PlayerRankingMS(generics.ListAPIView):
    """
    List Player Ranking Male Singles/Doubles
    """
    queryset = PlayerRankingsMS.objects.all()
    serializer_class = PlayerRankingsSerializerMS




