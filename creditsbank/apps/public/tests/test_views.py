from django.test import TestCase, Client
from django.urls import reverse
from creditsbank.apps.public.models import UserData
from creditsbank.apps.public.views import decrypt

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile_url = reverse('public:profile')

    def test_profile_GET(self):
        response = self.client.get(self.profile_url)

        self.assertTrue(response.status_code == 200 or response.status_code == 302)
        if response.status_code == 200:
            self.assertTemplateUsed(response, 'public/profile.html')

    def test_decrypt_function(self):
        key = "EFxaZz98wFff8X6yTBS9-OHbul_0bSLoo1LCUDqc14I="
        enc = "gAAAAABgBAUs6uCy9OAwGJwYzPQ6IsbNoGCZo3Yb3l0VluOB1nFeDkxaku0_4DbEfvfOLaeDDmN3b4XJrDA5n9OM7fpLD-ojZg21vVDhXz4fdVuLNRtxi1I="
        msg = "This is a test case"

        self.assertEquals(msg, decrypt(key, enc))
