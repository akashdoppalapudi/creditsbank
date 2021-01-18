from django.test import TestCase
from creditsbank.apps.public.models import UserData
from django.contrib.auth import get_user_model

class TestModels(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testcase', email='testcase@vvit.net', password='test@123',
                                             is_superuser=False, is_staff=False)
        self.user_data = UserData.objects.create(user=self.user, course='B.Tech', branch='ECE')

    def test_public_models(self):
        userdata = UserData.objects.get(id=1)
        self.assertEquals(userdata.user.username, 'testcase')
        self.assertEquals(userdata.branch, 'ECE')
        self.assertEquals(userdata.course, 'B.Tech')