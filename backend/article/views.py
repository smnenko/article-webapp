from django.utils.timezone import now, timedelta
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from .serializers import ArticleSerializer
from .serializers import ArticleTrendingSerializer
from .serializers import ArticleLatestSerializer

from .models import Article


class ArticleTrendingListAPIView(generics.ListAPIView):
    serializer_class = ArticleTrendingSerializer
    queryset = Article.objects.filter(date_created__range=[now() - timedelta(days=7), now()]).order_by('views')


class ArticleLatestListAPIView(generics.ListAPIView):
    serializer_class = ArticleLatestSerializer
    queryset = Article.objects.all().order_by('-date_created')[:10]


class ArticleCreateAPIView(generics.CreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated, )


class ArticleRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = (AllowAny, )


class ArticleUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = (IsAdminUser, )


class ArticleDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = (IsAdminUser, )
