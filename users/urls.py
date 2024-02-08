from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentsListApiView, UserListApiView

app_name = UsersConfig.name


urlpatterns = [
    path('payments/', PaymentsListApiView.as_view(), name='payments_list'),
    path('user_list/', UserListApiView.as_view(), name='user_list'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]