from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='romakondratiuk01@gmail.com',
            first_name='Roman',
            last_name='Kondratiuk',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('roma_2001')
        user.save()
