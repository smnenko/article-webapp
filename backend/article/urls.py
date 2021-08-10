from django.urls import path

from . import views


urlpatterns = [
    path('create/', views.ArticleCreateAPIView.as_view()),
    path('<int:pk>/', views.ArticleRetrieveAPIView.as_view()),
    path('<int:pk>/edit/', views.ArticleUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.ArticleDestroyAPIView.as_view(), name='article_delete'),
    path('trending/', views.ArticleTrendingListAPIView.as_view()),
    path('latest/', views.ArticleLatestListAPIView.as_view(), name='article_latest'),
    path('latest/<str:username>/', views.ArticleUserLatestListAPIView.as_view()),
]
