from django.db import models
from django.db.models import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver


NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    """Creating a model"""
    title = models.CharField(max_length=100, verbose_name='title')
    preview = models.ImageField(upload_to='course_previews/', verbose_name='preview', **NULLABLE)
    description = models.TextField(verbose_name='description')
    owner = models.ForeignKey('users.User', on_delete=CASCADE, related_name='courses', default=None)
    url = models.URLField(verbose_name='url', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


class Lesson(models.Model):
    """Creating a model"""
    title = models.CharField(max_length=100, verbose_name='title')
    preview = models.ImageField(upload_to='lesson_previews/', verbose_name='preview', **NULLABLE)
    description = models.TextField(verbose_name='description')
    url = models.URLField(verbose_name='url', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    owner = models.ForeignKey('users.User', on_delete=CASCADE, related_name='lessons', default=None, **NULLABLE)

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