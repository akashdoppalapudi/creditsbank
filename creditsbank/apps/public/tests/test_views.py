from django.test import TestCase, Client
from django.urls import reverse
from creditsbank.apps.administrator.models import UserCredits
from creditsbank.apps.public.models import UserData
from django.contrib.auth import get_user_model
from creditsbank.apps.public.views import decrypt

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile_url = reverse('public:profile')
        User = get_user_model()
        self.user = User.objects.create_user(username='testcase', email='testcase@vvit.net', password='test@123', is_superuser=False, is_staff=False)
        self.user_data = UserData.objects.create(user=self.user, course='B.Tech', branch='ECE')
        self.user_credits = UserCredits.objects.create(user=self.user, credits='gAAAAABgBEsaBA1Pcc9CzRlP2Ugp_usba-hh-5UNTQfFr3t5Z-mA6sInKU5vBowqC5lpuSZyfPnE5IoY8dZL5wKoGbtfsuKi4w==', key='rL2GpP4wGqYq4Y2rbTYuM15oYt62TTvtwRRd31NoobY=')

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

    def test_context(self):
        User = get_user_model()
        self.client.login(username='testcase', password='test@123')
        response = self.client.get(self.profile_url, follow=True)
        user = User.objects.get(username='testcase')
        self.assertEquals(response.context['course'], 'B.Tech')
        self.assertEquals(response.context['branch'], 'ECE')
        self.assertEquals(response.context['three'], 'S')