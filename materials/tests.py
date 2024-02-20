from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from materials.models import Course, Lesson, CourseSubscription
from materials.serializers import CourseSerializer, CourseSubscriptionSerializer
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

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 0, 'next': None, 'previous': None, 'results': []}

        )

    def test_lesson_create(self):
        """ testing for creating of lesson"""

        self.client.force_authenticate(user=self.user)

        data = {
            'title': 'test2',
            'description': 'this is second lesson',
            'course': self.course.id,
            'user': self.user.id
        }

        response = self.client.post(
            reverse('materials:lesson_create'),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Lesson.objects.all().count(),
            1
        )

    def test_lesson_update(self):
        """ test for updating of lesson"""

        self.client.force_authenticate(user=self.user)

        self.lesson = Lesson.objects.create(
            title='test_lesson',
            description='first lesson',
            course=self.course,
            owner=self.user
        )

        updated_data = {
            'title': 'updated_lesson',
            'description': 'this is updated lesson',
            'course': self.course.id
        }

        response = self.client.put(
            reverse('materials:lesson_update', args=[self.lesson.id]),
            data=updated_data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.lesson.refresh_from_db()
        self.assertEqual(
            self.lesson.title,
            updated_data['title']
        )

        self.lesson.refresh_from_db()
        self.assertEqual(
            self.lesson.description,
            updated_data['description']
        )

    def test_delete_lesson(self):
        ''' test for deleting of course'''

        self.client.force_authenticate(user=self.user)

        self.lesson = Lesson.objects.create(
            title='lesson_to_delete',
            description='lesson_to_delete description',
            course=self.course,
            owner=self.user
        )

        response = self.client.delete(
            reverse('materials:lesson_delete', args=[self.lesson.id]),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        # check that the lesson has been deleted
        with self.assertRaises(Lesson.DoesNotExist):
            self.lesson.refresh_from_db()


class CourseSubscriptionAPITestCase(APITestCase):
    """testing a subscription to course updates"""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.course = Course.objects.create(title='Test Course', description='Test Description', owner=self.user)

    def test_get_course_subscriptions_authenticated(self):
        self.client.force_authenticate(user=self.user)
        # response = self.client.get(reverse('course-subscription'))
        response = self.client.get('/subscription/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_course_subscription_authenticated(self):
        self.client.force_authenticate(user=self.user)
        # response = self.client.post(reverse('course-subscription', kwargs={'course_id': self.course.id}))
        response = self.client.post('/subscription/{}/'.format(self.course.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)
        self.assertIn('subscription', response.data)

    def test_post_course_subscription_unauthenticated(self):
        # response = self.client.post(reverse('course-subscription', kwargs={'course_id': self.course.id}))
        response = self.client.post('/subscription/{}/'.format(self.course.id))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)