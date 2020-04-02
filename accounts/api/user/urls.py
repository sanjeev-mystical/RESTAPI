from django.conf.urls import url
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import UserDetailAPIView, UserStatusAPIView

urlpatterns = [
    path('<str:username>', UserDetailAPIView.as_view(), name='detail'),
    path('<str:username>/status/', UserStatusAPIView.as_view(), name='status-list'),
    # path('register', RegisterAPIView.as_view()),
    # path('jwt', obtain_jwt_token),
    # path('jwt/refresh', refresh_jwt_token),
]