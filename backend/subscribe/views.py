from django.db.models import Value
from django.shortcuts import render
from rest_framework import (
    generics,
    status)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authapp.models import User
from . import utils
from .models import AuthorSubscriber
from .serializers import (
    SubscribeSerializer,
    SubscribeStatusSerializer)


class SubscribeAPIView(APIView):
    serializer_class = SubscribeSerializer
    queryset = AuthorSubscriber
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        author, subscriber = utils.get_author_subscriber_ids_from_request(request)
        obj = self.queryset.objects.filter(author_id=author, subscriber_id=subscriber)

        if obj.exists():
            return Response({'message': 'You are already subscribed for this user'}, status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data={'author': author, 'subscriber': subscriber})
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        author, subscriber = utils.get_author_subscriber_ids_from_request(request)
        obj = self.queryset.objects.filter(author_id=author, subscriber_id=subscriber)
        if obj.exists():
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'Subscription is not found'}, status.HTTP_400_BAD_REQUEST)


class SubscribeRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SubscribeStatusSerializer
    queryset = AuthorSubscriber
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        author = kwargs.get('author_username')
        subscriber = request.query_params.get('subscriber')
        is_subscribed = self.queryset.objects.filter(author__username=author, subscriber__email=subscriber).exists()
        serializer = self.serializer_class(data={'status': is_subscribed})
        serializer.is_valid()
        return Response(serializer.data, status.HTTP_200_OK)
