from django.utils.timezone import now, timedelta
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from .serializers import ArticleSerializer, ArticleTrendingSerializer
from .models import Article


class ArticleListAPIView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleTrendingListAPIView(generics.ListAPIView):
    serializer_class = ArticleTrendingSerializer
    queryset = Article.objects.filter(date_created__range=[now() - timedelta(days=7), now()]).order_by('views')


class ArticleCreateAPIView(generics.CreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated, )


class ArticleRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = (AllowAny, )


class ArticleDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = (IsAdminUser, )
