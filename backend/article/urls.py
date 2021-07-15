from django.urls import path

from . import views


urlpatterns = [
    path('', views.ArticleListAPIView.as_view()),
    path('create', views.ArticleCreateAPIView.as_view()),
    path('<int:pk>', views.ArticleRetrieveAPIView.as_view()),
    path('<int:pk>', views.ArticleDestroyAPIView.as_view()),
    path('trending', views.ArticleTrendingListAPIView.as_view()),
]
