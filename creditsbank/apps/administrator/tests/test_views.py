from django.test import TestCase, Client
from django.urls import reverse
from creditsbank.apps.administrator.models import UserCredits
from creditsbank.apps.administrator.views import encrypt
from cryptography.fernet import Fernet

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.update_url = reverse('administrator:update')
        self.update_submission_url = reverse('administrator:update-submission')
        
    def test_update_GET(self):
        response = self.client.get(self.update_url)

        self.assertTrue(response.status_code == 200 or response.status_code == 302)
        if response.status_code == 200:
            self.assertTemplateUsed(response, 'adminstrator/update.html')
    
    def test_update_submission_GET(self):
        response = self.client.get(self.update_submission_url)

        self.assertTrue(response.status_code == 200 or response.status_code == 302)
        if response.status_code == 200:
            self.assertTemplateUsed(response, 'adminstrator/update.html')

    def test_encrypt_function(self):
        msg = "This is a test case"
        key, msg_enc  = encrypt(msg)
        f = Fernet(key.encode('utf-8'))
        self.assertEquals(msg, f.decrypt(msg_enc.encode('utf-8')).decode('utf-8'))
