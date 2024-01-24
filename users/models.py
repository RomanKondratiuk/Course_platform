from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """ This is the model for users"""
    first_name = models.CharField(max_length=50, verbose_name='first_name')
    last_name = models.CharField(max_length=50, verbose_name='last_name')
    phone = models.IntegerField(verbose_name='phone_number', **NULLABLE)
    city = models.TextField(max_length=50, verbose_name='city', **NULLABLE)
    avatar = models.ImageField(upload_to='avatars/', verbose_name='avatar', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='email')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
