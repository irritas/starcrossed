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
    image = models.ImageField(upload_to='profile_image', blank=True)

class Photo(models.Model):
        url = models.CharField(max_length=200)
        user = models.ForeignKey(User, on_delete=models.CASCADE)

        def __str__(self):
            return f"Photo for user_id: {self.user_id} @{self.url}"

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

