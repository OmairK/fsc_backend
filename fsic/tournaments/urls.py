from django.urls import path, include
from . import views




urlpatterns = [
    path('itf/', views.TournamentsListITF.as_view(), name ='tournaments_itf'),
    path('fsc/',views.TournamentsListFSC.as_view(), name='tournaments_fsc'),
    path('rankpms/',views.PlayerRankingMS.as_view(),name='playerRankMS'),
    path('rankpmd/',views.PlayerRankingMD.as_view(),name='playerRankMD'),
    path('rankpfs/',views.PlayerRankingFS.as_view(),name='playerRankFS '),
    path('rankpfd/',views.PlayerRankingFD.as_view(),name='playerRankFS')

]