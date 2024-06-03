
#tbase/tbase/lk/models.py
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
#from phonenumber_field.modelfields import PhoneNumberField



# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE),
#     first_name = models.CharField('Фио', max_length=200),
#     username = models.CharField('Имя_польз', max_length=30),
#     email = models.EmailField('Почта', max_length=50),
#     venue_image = models.ImageField(null=True, blank=True, upload_to="images/")
#
#     def str(self):
#         return f'{self.user.username} Profile'