from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .serializers import TopicSerializer
from .models import Topic


class TopicListAPIView(generics.ListAPIView):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()


class TopicCreateAPIView(generics.CreateAPIView):
    serializer_class = TopicSerializer
    permission_classes = (IsAdminUser, )


class TopicRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
