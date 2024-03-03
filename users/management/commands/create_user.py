from django.core.management import BaseCommand
from django.utils import timezone
from users.models import User
from datetime import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='test.user.@icloud.com',
            first_name='Test',
            last_name='test',
            is_staff=True,
            is_superuser=True,
            last_login=datetime(2024, 1, 1),
            username='Test'
        )

        user.set_password('test_0001')
        user.save()
