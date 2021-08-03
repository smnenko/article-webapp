from django.urls import path

from . import views


urlpatterns = [
    path('', views.SubscribeAPIView.as_view()),
    path('<str:author_username>/', views.SubscribeRetrieveAPIView.as_view())
]
