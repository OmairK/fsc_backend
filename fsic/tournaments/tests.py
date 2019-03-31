from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tournaments.views import *

class Test_Tournaments_Urls(SimpleTestCase):    

    def test_tournaments_itf_url_is_resolved(self):
        url = reverse('tournaments_itf')
        self.assertEquals(resolve(url).func, tournaments_itf)

    def test_tournaments_fsc_url_is_resolved(self):
        url = reverse('tournaments_fsc')
        self.assertEquals(resolve(url).func, tournaments_fsc)
    
    def test_ranking_url_is_resolved(self):
        url = reverse('playerRankMS')
        self.assertEquals(resolve(url).func , playerRankMS )
