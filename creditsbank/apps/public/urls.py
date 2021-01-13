from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'public'
urlpatterns = [
    path('', views.profile, name='profile'),
    path('login', auth_views.LoginView.as_view(template_name='public/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('change-password', auth_views.PasswordChangeView.as_view(template_name='public/changepassword.html', success_url='/public/'), name='change-password'),
]