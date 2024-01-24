from rest_framework import serializers

from materials.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    """Serializer Description"""
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    """Serializer Description"""
    class Meta:
        model = Lesson
        fields = '__all__'
