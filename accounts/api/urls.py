from django.conf.urls import url
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import AuthAPIView, RegisterAPIView

urlpatterns = [
    path('', AuthAPIView.as_view(), name='login'),
    #path('<str:username>', UserDetailAPIView.as_view()),
    path('register', RegisterAPIView.as_view(), name='register'),
    # path('jwt', obtain_jwt_token),
    # path('jwt/refresh', refresh_jwt_token),
]