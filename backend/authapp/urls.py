from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from . import views


urlpatterns = [
    path('create/', views.RegistrationAPIView.as_view(), name='user_register'),
    path('login/', views.LoginAPIView.as_view(), name='user_login'),
    path('<int:pk>/', views.UserRetrieveUpdateAPIView.as_view(), name='user_retrieve'),
    path('token/', views.TokenRefreshView.as_view(), name='user_token'),
    path('subscribe/', views.SubscribeAPIView.as_view()),
]

