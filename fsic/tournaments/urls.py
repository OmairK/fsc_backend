from django.urls import path, include
from . import views




urlpatterns = [
    path('tournaments-itf/', views.TournamentsListITF.as_view(), name ='tournaments_itf'),
    path('tournaments-fsc/',views.TournamentsListFSC.as_view(), name='tournaments_fsc'),
    path('player-ranking-itf/',views.PlayerRankingMS.as_view(),name='playerRankMS'),
]
