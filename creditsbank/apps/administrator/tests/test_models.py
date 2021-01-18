from django.test import TestCase
from creditsbank.apps.administrator.models import UserCredits
from django.contrib.auth import get_user_model

class TestModels(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testcase', email='testcase@vvit.net', password='test@123',
                                             is_superuser=False, is_staff=False)
        self.user_credits = UserCredits.objects.create(user=self.user, credits='This is test credits', key='This is test key')

    def test_administrator_model(self):
        usercredits = UserCredits.objects.get(id=1)
        self.assertEquals(usercredits.user.username, 'testcase')
        self.assertEquals(usercredits.credits, 'This is test credits')
        self.assertEquals(usercredits.key, 'This is test key')