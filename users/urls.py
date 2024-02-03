from django.urls import path

from users.apps import UsersConfig
from users.views import PaymentsListApiView, UserListApiView

app_name = UsersConfig.name


urlpatterns = [
    path('payments/', PaymentsListApiView.as_view(), name='payments_list'),
    path('user_list/', UserListApiView.as_view(), name='user_list'),

]