from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

#ogni volta che uno user viene salvato, invia un segnale che viene ricevuto


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("Created: ", created)
    if created:
        Profile.objects.create(user=instance)
