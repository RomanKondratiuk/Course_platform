from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from materials.models import Course
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        # creating user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        self.course = Course.objects.create(
            title='test',
            description='first course',
            owner=self.user
        )

    def test_get_lesson_authenticated(self):
        """ Test for receiving a course of lessons by an authenticated user. """

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('materials:lesson_list')
        )

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
