from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from .models import UserRegistrationModel


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        UserRegistrationModel.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        UserRegistrationModel.objects.create(user=instance)
