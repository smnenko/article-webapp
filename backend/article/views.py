from django.utils.timezone import now, timedelta
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from authapp.permissions import IsAuthor
from authapp.models import User
from .serializers import ArticleSerializer
from .serializers import ArticleRetrieveSerializer
from .serializers import ArticleTrendingSerializer
from .serializers import ArticleLatestSerializer
from .models import Article


class ArticleTrendingListAPIView(generics.ListAPIView):
    serializer_class = ArticleTrendingSerializer
    queryset = Article.objects.filter(date_created__range=[now() - timedelta(days=7), now()]).order_by('views')


class ArticleLatestListAPIView(generics.ListAPIView):
    serializer_class = ArticleLatestSerializer
    queryset = Article.objects.all().order_by('-date_created')[:10]


class ArticleUserLatestListAPIView(generics.ListAPIView):
    queryset = Article
    serializer_class = ArticleLatestSerializer

    def get_queryset(self):
        return Article.objects.filter(author__username=self.kwargs['username']).order_by('-date_created')


class ArticleCreateAPIView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated, )


class ArticleRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ArticleRetrieveSerializer
    queryset = Article.objects.all()
    permission_classes = (AllowAny, )


class ArticleUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ArticleRetrieveSerializer
    queryset = Article.objects.all()
    permission_classes = (IsAuthor, )


class ArticleDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated, IsAuthor)

    def get_queryset(self):
        return Article.objects.filter(author=User.objects.filter(email=self.request.query_params.get('author')))
