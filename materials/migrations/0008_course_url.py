# Generated by Django 5.0.1 on 2024-02-15 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0007_alter_lesson_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='url'),
        ),
    ]
