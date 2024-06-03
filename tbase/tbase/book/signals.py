
# tbase/tbase/book/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Clients



@receiver(post_save, sender=Clients)
def create_user_for_client(sender, instance, created, **kwargs):
    if created and instance.user is None:
        user = User.objects.create_user(
            username=instance.login,
            password=instance.password,
            email=instance.e_mail,
            first_name=instance.fio.split()[0],
            last_name=' '.join(instance.fio.split()[1:])
        )
        instance.user = user
        instance.save()
