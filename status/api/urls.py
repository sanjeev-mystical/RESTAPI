from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from .views import StatusAPIView, StatusApiDetailView #StatusDeleteAPIView

urlpatterns = [
    path('', StatusAPIView.as_view()),
    path('<int:id>/', StatusApiDetailView.as_view(), name='detail'),  #api/status/id
]
