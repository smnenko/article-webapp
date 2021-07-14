from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('user/create', views.RegistrationAPIView.as_view()),
    path('user/login', views.LoginAPIView.as_view()),
    path('user/<int:pk>', views.UserDetailAPIView.as_view()),
]

