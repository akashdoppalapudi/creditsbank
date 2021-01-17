from django.test import SimpleTestCase
from django.urls import reverse, resolve
from creditsbank.apps.administrator.views import update, update_submission

class TestUrls(SimpleTestCase):
    def test_update_url_is_resolved(self):
        url = reverse('administrator:update')
        self.assertEquals(resolve(url).func, update)
    
    def test_update_submission_url_is_resolved(self):
        url = reverse('administrator:update-submission')
        self.assertEquals(resolve(url).func, update_submission)