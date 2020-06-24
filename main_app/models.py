# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#       name = models.CharField(max_length=100)
#   birthdate = models.DateField()
#   bio = models.TextField(max_length=250)

#     def __str__(self):
#         return self.username

from django.db import models
from django.contrib.auth.models import User
import requests

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

# class User(models.Model):
#   user = models.OneToOneField(User, on_delete=models.CASCADE)
#   name = models.CharField(max_length=100)
#   birthdate = models.DateField()
#   bio = models.TextField(max_length=250)


#Sarah's code
# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     causes = models.ManyToManyField(Cause)
#     purchased_items = models.ManyToManyField(Order)
#     def __str__(self):
#         return self.user
