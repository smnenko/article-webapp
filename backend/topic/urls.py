from django.urls import path

from . import views


urlpatterns = [
    path('', views.TopicListAPIView.as_view()),
    path('create/', views.TopicCreateAPIView.as_view()),
    path('<str:name>/', views.TopicRetrieveAPIView.as_view())
]
