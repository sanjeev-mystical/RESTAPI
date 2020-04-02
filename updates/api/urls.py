from django.conf.urls import url
from django.urls import path
from .views import UpdateModelDetailApiView, UpdateModelListApiView

urlpatterns = [
    path('', UpdateModelListApiView.as_view()),
    path('<int:id>', UpdateModelDetailApiView.as_view()),

]
