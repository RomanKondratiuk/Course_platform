from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE
from django.utils.translation import gettext_lazy as _
from materials.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    """ this is class of selection the role """

    MEMBER = 'member', _('member'),
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    """ This is a users model"""
    first_name = models.CharField(max_length=50, verbose_name='first_name')
    last_name = models.CharField(max_length=50, verbose_name='last_name')
    phone = models.IntegerField(verbose_name='phone_number', **NULLABLE)
    city = models.TextField(max_length=50, verbose_name='city', **NULLABLE)
    avatar = models.ImageField(upload_to='avatars/', verbose_name='avatar', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='email')
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)

    # Changing authorization from username to e-mail
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Payments(models.Model):
    """ This is a payments model"""

    PAYMENT_CHOICES = [
        ('transfer', 'transfer to account'),
        ('cash', 'cash'),
    ]

    user = models.ForeignKey(User, on_delete=CASCADE, verbose_name='user')
    date_of_payment = models.DateField(verbose_name='date_of_payment')
    paid_course = models.ForeignKey(Course, on_delete=CASCADE, **NULLABLE, verbose_name='paid course')
    paid_lesson = models.ForeignKey(Lesson, on_delete=CASCADE, **NULLABLE, verbose_name='paid lesson')
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='payment_amount')
    payment_method = models.CharField(max_length=100, choices=PAYMENT_CHOICES, verbose_name='payment_method')

    def __str__(self):
        return f"{self.user} on  {self.date_of_payment}"

    class Meta:
        verbose_name = "payment"
        verbose_name_plural = "payments"
