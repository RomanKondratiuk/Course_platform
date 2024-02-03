from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter

from users.models import Payments, User
from users.serializers import PaymentsSerializer, UserSerializer


class PaymentsListApiView(generics.ListAPIView):
    """ list of payments """
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')
    ordering_fields = ('date_of_payment',)


class UserListApiView(generics.ListAPIView):
    """list of users"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
