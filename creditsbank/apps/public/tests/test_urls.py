from django.test import SimpleTestCase
from django.urls import reverse, resolve
from creditsbank.apps.public.views import profile
from django.contrib.auth import views as auth_views

class TestUrls(SimpleTestCase):
    def test_profile_url_is_resolved(self):
        url = reverse('public:profile')
        self.assertEquals(resolve(url).func, profile)

    def test_login_url_is_resolved(self):
        url = reverse('public:login')
        self.assertEquals(resolve(url).func.view_class, auth_views.LoginView)

    def test_logout_url_is_resolved(self):
        url = reverse('public:logout')
        self.assertEquals(resolve(url).func.view_class, auth_views.LogoutView)

    def test_changepassword_url_is_resolved(self):
        url = reverse('public:change-password')
        self.assertEquals(resolve(url).func.view_class, auth_views.PasswordChangeView)