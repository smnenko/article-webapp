from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from . import views


urlpatterns = [
    path('create/', views.RegistrationAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('<int:pk>/', views.UserRetrieveUpdateAPIView.as_view()),
    path('<str:username>/', views.AuthorRetrieveAPIView.as_view()),
    path('token/', views.TokenRefreshView.as_view()),
]

