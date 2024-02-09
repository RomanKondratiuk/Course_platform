from rest_framework import serializers

from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    """Serializer Description"""

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    """Serializer Description"""

    # creating field for lessons count
    lessons_count = serializers.SerializerMethodField()

    # creating lessons list for course
    lessons_list = LessonSerializer(many=True, source='lessons', required=False)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, obj):
        return obj.lessons.count()
