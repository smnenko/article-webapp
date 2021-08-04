from django.urls import path

from . import views


urlpatterns = [
    path('create/', views.ArticleCreateAPIView.as_view()),
    path('<int:pk>/', views.ArticleRetrieveAPIView.as_view()),
    path('<int:pk>/edit/', views.ArticleUpdateAPIView.as_view()),
    path('<int:pk>/', views.ArticleDestroyAPIView.as_view()),
    path('trending/', views.ArticleTrendingListAPIView.as_view()),
    path('latest/', views.ArticleLatestListAPIView.as_view()),
    path('latest/<str:username>/', views.ArticleUserLatestListAPIView.as_view()),
]
