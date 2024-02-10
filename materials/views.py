from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from materials.models import Course, Lesson
from materials.permissions import IsOwner, IsModerator
from materials.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """ Description of ViewSet for working with the course model """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]

    def create(self, request, *args, **kwargs):
        # Checking if a user is a moderator
        is_moderator = request.user.groups.filter(name='Moderators').exists()
        if not is_moderator:
            return self.permission_denied(request)

        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Checking if a user is a moderator
        is_moderator = request.user.groups.filter(name='Moderators').exists()
        if not is_moderator:
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

