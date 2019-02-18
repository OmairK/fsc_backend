from django.test import SimpleTestCase
from django.urls import reverse, resolve
from form_to_email.views import form

# Create your tests here.
class TestUrls(SimpleTestCase):
    
    def test_form_url_is_resolved(self):
        url = reverse('form')
        self.assertEquals(resolve(url).func, form)