from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse
from tournaments.serializers import *
from tournaments.models import *
import datetime


class TournamentsListITF(generics.ListAPIView):
    """
    List all ITF (International Tennis Federation) Tournaments 
    """
    duration = (datetime.date.today() - datetime.timedelta(days=60)).isoformat()
    duration = duration.split('-')
    duration = ''.join(str(q) for q in duration) 
    queryset = TournamentITF.objects.filter(start_date__gt=int(duration))
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




