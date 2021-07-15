from django.urls import path

from . import views


urlpatterns = [
    path('', views.TopicListAPIView.as_view()),
    path('create', views.TopicCreateAPIView.as_view()),
    path('<int:pk>', views.TopicRetrieveUpdateDestroyAPIView.as_view())
]
