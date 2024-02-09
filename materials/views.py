from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """ Description of ViewSet for working with the course model """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]


class LessonCreateApiView(generics.CreateAPIView):
    """ Creating a lesson """
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]


class LessonListApiView(generics.ListAPIView):
    """ Reading all lessons """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonRetrieveApiView(generics.RetrieveAPIView):
    """ Reading one lesson """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonUpdateApiView(generics.UpdateAPIView):
    """ Updating one lesson """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonDestroyApiView(generics.DestroyAPIView):
    """ Deleting one lesson """
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]

