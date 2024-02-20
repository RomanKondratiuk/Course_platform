from rest_framework import viewsets, generics, status
# from rest_framework.generics import get_object_or_404
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course, Lesson, CourseSubscription
from materials.paginators import LessonPaginator, CoursePaginator
from materials.permissions import IsOwner, IsModerator
from materials.serializers import CourseSerializer, LessonSerializer, CourseSubscriptionSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """ Description of ViewSet for working with the course model """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]
    pagination_class = CoursePaginator

    def create(self, request, *args, **kwargs):
        # Checking if a user is a moderator
        is_moderator = request.user.groups.filter(name='Moderators').exists()
        if is_moderator:
            return self.permission_denied(request)
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Checking if a user is a moderator
        is_moderator = request.user.groups.filter(name='Moderators').exists()
        if is_moderator:
            return self.permission_denied(request)
        return super().destroy(request, *args, **kwargs)


class LessonCreateApiView(generics.CreateAPIView):
    """ Creating a lesson """
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class LessonListApiView(generics.ListAPIView):
    """ Reading all lessons """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]
    pagination_class = LessonPaginator


class LessonRetrieveApiView(generics.RetrieveAPIView):
    """ Reading one lesson """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class LessonUpdateApiView(generics.UpdateAPIView):
    """ Updating one lesson """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class LessonDestroyApiView(generics.DestroyAPIView):
    """ Deleting one lesson """
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class CourseSubscriptionAPIView(APIView):
    """Creating a subscription to course updates"""

    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request):
        user = request.user

        if user.is_authenticated:
            # Getting all subscriptions for the current user
            subscriptions = CourseSubscription.objects.filter(user=user)
            subscription_serializer = CourseSubscriptionSerializer(subscriptions, many=True)

            # Getting all courses
            courses = Course.objects.all()
            course_serializer = CourseSerializer(courses, many=True, context={'request': request})

            # Returning JSON with data about courses and subscriptions
            return Response({"courses": course_serializer.data, "subscriptions": subscription_serializer.data},
                            status=status.HTTP_200_OK)
        else:
            # Return an error message if the user is not authenticated
            return Response({"message": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, course_id):
        user = request.user

        if user.is_authenticated:
            # Getting the course object from the database using get_object_or_404
            course = get_object_or_404(Course, id=course_id)

            # Retrieving subscription objects by current user and course
            subscription, created = CourseSubscription.objects.get_or_create(user=user, course=course)

            if created:
                message = 'Subscription has been created successfully.'
            else:
                subscription.delete()
                message = 'Subscription has been deleted successfully.'

            serializer = CourseSubscriptionSerializer(subscription)
            return Response({"message": message, "subscription": serializer.data}, status=status.HTTP_200_OK)
        else:
            # Return an error message if the user is not authenticated
            return Response({"message": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)
