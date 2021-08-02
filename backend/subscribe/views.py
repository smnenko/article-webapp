from django.db.models import Value
from django.shortcuts import render
from rest_framework import (
    generics,
    status)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authapp.models import User
from .models import AuthorSubscriber
from .serializers import (
    SubscribeSerializer,
    SubscribeStatusSerializer)


class SubscribeCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscribeSerializer
    queryset = AuthorSubscriber
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        request.data['author'] = User.objects.filter(username=request.data['author']).first().id
        request.data['subscriber'] = User.objects.filter(email=request.data['subscriber']).first().id
        obj = self.queryset.objects.filter(author=request.data['author'], subscriber=request.data['subscriber'])
        if not obj.exists():
            return super().post(request, args, kwargs)
        obj.delete()
        return Response({'message': 'Unsubscribed'}, status.HTTP_204_NO_CONTENT)


class SubscribeRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SubscribeStatusSerializer
    queryset = AuthorSubscriber
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        author = request.query_params.get('author')
        subscriber = request.query_params.get('subscriber')
        is_subscribed = self.queryset.objects.filter(author__username=author, subscriber__email=subscriber).exists()
        serializer = self.serializer_class(data={'status': is_subscribed})
        serializer.is_valid()
        return Response(serializer.data, status.HTTP_200_OK)
