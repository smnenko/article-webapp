from django.utils.timezone import now, timedelta
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response

from .serializers import ArticleSerializer
from .serializers import ArticleTrendingSerializer
from .serializers import ArticleLatestSerializer

from .models import Article
from authapp.models import User
from topic.models import Topic


class ArticleTrendingListAPIView(generics.ListAPIView):
    serializer_class = ArticleTrendingSerializer
    queryset = Article.objects.filter(date_created__range=[now() - timedelta(days=7), now()]).order_by('views')


class ArticleLatestListAPIView(generics.ListAPIView):
    serializer_class = ArticleLatestSerializer
    queryset = Article.objects.all().order_by('-date_created')[:10]


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
