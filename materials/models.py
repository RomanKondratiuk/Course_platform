from django.db import models
from django.db.models import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    """Creating a model"""
    title = models.CharField(max_length=100, verbose_name='title')
    preview = models.ImageField(upload_to='course_previews/', verbose_name='preview', **NULLABLE)
    description = models.TextField(verbose_name='description')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='owner', **NULLABLE)
    url = models.URLField(verbose_name='url', **NULLABLE)
    price = models.PositiveIntegerField(verbose_name='price', null=True)

    def __str__(self):
        return self.title

    def get_subscribed_users(self):
        return [subscription.user for subscription in self.subscriptions.all() if subscription.user is not None]


    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


class Lesson(models.Model):
    """Creating a model"""
    title = models.CharField(max_length=100, verbose_name='title')
    preview = models.ImageField(upload_to='lesson_previews/', verbose_name='preview', **NULLABLE)
    description = models.TextField(verbose_name='description')
    url = models.URLField(verbose_name='url', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lessons', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'


@receiver(post_save, sender=Lesson)
def set_lesson_owner(sender, instance, created, **kwargs):
    """
    A signal that automatically sets the owner of a lesson equal to the owner of the corresponding course,
    only if the lesson is created for the first time (not when updating).
    """
    if created and not instance.owner:
        instance.owner = instance.course.owner
        instance.save()


class CourseSubscription(models.Model):
    """Subscription_to_the_course"""

    course = models.ForeignKey(Course, on_delete=CASCADE, related_name='subscriptions')
    user = models.ForeignKey('users.User', on_delete=CASCADE, null=True)
    # valid_subscription = models.BooleanField(default=False)


class CoursePayment(models.Model):
    name = models.ForeignKey(Course, on_delete=CASCADE, verbose_name='name_of_product', default=4, **NULLABLE)
    price_amount = models.CharField(verbose_name='payment_price', **NULLABLE)
    payment_link = models.URLField(max_length=400, verbose_name='link_to_payment', **NULLABLE)
    payment_id = models.CharField(max_length=255, verbose_name='id_of_payment', **NULLABLE)

    class Meta:
        verbose_name = 'course payment'
        verbose_name_plural = 'course payments'

    def __str__(self):
        return self.payment_id
