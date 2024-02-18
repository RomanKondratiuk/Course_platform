from rest_framework import serializers

from materials.models import Course, Lesson, CourseSubscription
from materials.validators import validator_scam_url


class LessonSerializer(serializers.ModelSerializer):
    """Serializer Description"""

    # validation for material reference
    url = serializers.URLField(validators=[validator_scam_url], read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    """Serializer Description"""

    is_subscribed = serializers.SerializerMethodField()

    # creating field for lessons count
    lessons_count = serializers.SerializerMethodField()

    # creating lessons list for course
    lessons_list = LessonSerializer(many=True, source='lessons', required=False)

    # validation for material reference
    url = serializers.URLField(validators=[validator_scam_url], read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_is_subscribed(self, instance):
        # getting current user
        user = self.context['request'].user

        # checking the user's subscription to this course
        if user.is_authenticated:
            return CourseSubscription.objects.filter(user=user, course=instance).exists()
        else:
            return False

    def get_lessons_count(self, obj):
        return obj.lessons.count()


class CourseSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSubscription
        fields = '__all__'
