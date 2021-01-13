from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserData(models.Model):
    #owner
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'userdata')
    #details
    course = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)