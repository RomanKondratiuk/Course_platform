from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.utils import timezone

from materials.models import Course, Lesson
from users.models import Payments

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):

        # creating test user
        user = User.objects.create(username='roma3@example.com', first_name='Roman', last_name='Roman', email='roma3@example.com')

        # creating test course
        course = Course.objects.create(title='backend', description='this is the backend course')

        # creating test lesson
        lesson = Lesson.objects.create(title='lesson_C++', description='this is the lesson_C++', course=course)

        # creating test payment
        payment = Payments.objects.create(
            user=user,
            date_of_payment=timezone.now(),
            paid_course=course,
            paid_lesson=lesson,
            payment_amount=220.10,
            payment_method='transfer'
        )

        self.stdout.write(self.style.SUCCESS('Successfully created sample payments'))
