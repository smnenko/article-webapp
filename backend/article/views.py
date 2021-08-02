from django.db.models import Count
from django.utils.timezone import now, timedelta
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from authapp.models import User
from .serializers import ArticleSerializer
from .serializers import ArticleTrendingSerializer
from .serializers import ArticleLatestSerializer
from .models import Article


class ArticleTrendingListAPIView(generics.ListAPIView):
    serializer_class = ArticleTrendingSerializer
    queryset = Article.objects.filter(date_created__range=[now() - timedelta(days=7), now()]).order_by('views')


class ArticleLatestListAPIView(generics.ListAPIView):
    serializer_class = ArticleLatestSerializer
    queryset = Article.objects.all().order_by('-date_created')

    def get_queryset(self):
        options = {}
        queryset = Article.objects.all()
        topics = [int(i) for i in self.request.query_params.getlist('topic[]')] or None
        content = self.request.query_params.get('content') or None
        if topics and len(topics) > 1:
            queryset.annotate(c=Count('topics')).filter(c=len(topics))
            for topic in topics:
                queryset = queryset.filter(topics__id=topic)
            if content:
                return queryset.filter(content__icontains=content)

        if topics:
            options['topics__id'] = topics[0]

        if content:
            options['content__icontains'] = content
        return queryset.filter(**options).order_by('-date_created')


class ArticleUserLatestListAPIView(generics.ListAPIView):
    serializer_class = ArticleLatestSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Article.objects.filter(author=User.objects.filter(pk=pk).first()).order_by('-date_created')


class ArticleCreateAPIView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        request.data['author'] = User.objects.filter(email=request.data['author']).first().pk
        return super().post(request, *args, **kwargs)


class ArticleRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = (AllowAny, )


class ArticleUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = (IsAdminUser, )


class ArticleDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Article.objects.filter(author_id=self.kwargs.get('user_id'))
