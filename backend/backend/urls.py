from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('authapp.urls')),
    path('api/v1/topic/', include('topic.urls')),
    path('api/v1/article/', include('article.urls')),
]
