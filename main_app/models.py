from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.TextField(max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	sign = models.TextField(max_length=20, blank=True)
	bio = models.TextField(max_length=500, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()

class Chat(models.Model):
	users = models.ManyToManyField(User)
	start_date = models.DateField()
	recent_date = models.DateField()