from django.urls import path

from . import views


urlpatterns = [
    path('', views.SubscribeRetrieveAPIView.as_view()),
    path('create/', views.SubscribeCreateAPIView.as_view())
]
