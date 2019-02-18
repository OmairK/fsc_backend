from django.urls import path, include
from . import views




urlpatterns = [
    path('itf/', views.TournamentsListITF, name ='tournaments_itf'),
    path('fsc/',views.TournamentsListFSC.as_view(), name='tournaments_fsc'),
    path('rankpms/',views.PlayerRankingMS.as_view(),name='playerRank'),
    path('rankpmd/',views.PlayerRankingMD.as_view(),name='playerRank'),
    path('rankpfs/',views.PlayerRankingFS.as_view(),name='playerRank'),
    path('rankpfd/',views.PlayerRankingFD.as_view(),name='playerRank')

]