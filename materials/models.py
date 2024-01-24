from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    preview = models.ImageField(upload_to='course_previews/', verbose_name='preview', **NULLABLE)
    description = models.TextField(verbose_name='description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    preview = models.ImageField(upload_to='lesson_previews/', verbose_name='preview', **NULLABLE)
    description = models.TextField(verbose_name='description')
    url = models.URLField(verbose_name='url')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'
