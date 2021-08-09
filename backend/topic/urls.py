from django.urls import path

from . import views


urlpatterns = [
    path('', views.TopicListAPIView.as_view(), name='topics_list'),
    path('create', views.TopicCreateAPIView.as_view(), name='topic_create'),
    path('<int:pk>', views.TopicRetrieveAPIView.as_view(), name='topic_retrieve')
]
