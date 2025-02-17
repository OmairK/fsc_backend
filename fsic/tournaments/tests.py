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

class Test_FSC_Tournaments(SimpleTestCase):

    def test_event_is_in_past(self):
        pass
        


class Test_Token_Authentication(SimpleTestCase):

    def test_get_request_for_tournaments_return_200(self):
        pass

    
