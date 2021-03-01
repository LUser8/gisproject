from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    address = models.TextField(blank=True, null=True)
    house_number = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.BigIntegerField(blank=True, null=True)
    updated_newsletter = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'


def post_save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(post_save_profile, sender=User)
