from django.db import models
from django.contrib.auth.models import User
from django_cryptography.fields import encrypt

# Create your models here.
class UserCredits(models.Model):
    #owner
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usercredits')
    #credits
    credits = encrypt(models.CharField(max_length=200, blank=True, unique=False, default=''))
    key = encrypt(models.CharField(max_length=200, default=''))