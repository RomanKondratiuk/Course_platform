from rest_framework import viewsets, generics

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """ Description of ViewSet for working with the course model """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonCreateApiView(generics.CreateAPIView):
    """ Creating a lesson """
    serializer_class = LessonSerializer


class LessonListApiView(generics.ListAPIView):
    """ Reading all lessons """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveApiView(generics.RetrieveAPIView):
    """ Reading one lesson """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateApiView(generics.UpdateAPIView):
    """ Updating one lesson """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyApiView(generics.DestroyAPIView):
    """ Deleting one lesson """
    queryset = Lesson.objects.all()
