from django.db.models import Value
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView

from subscribe.models import AuthorSubscriber
from .models import User
from .serializers import RegistrationSerializer
from .serializers import LoginSerializer
from .serializers import ProfileSerializer
from .serializers import AuthorSerializer
from .serializers import TokenRefreshSerializer


class RegistrationAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = RegistrationSerializer


class LoginAPIView(APIView):
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')
        serializer = self.serializer_class(data={'email': email, 'password': password})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_200_OK)


class TokenRefreshView(APIView):
    serializer_class = TokenRefreshSerializer

    def post(self, request, format=None):
        email = request.data.get('email')
        token = request.data.get('token')
        serializer = self.serializer_class(data={'email': email, 'token': token})
        serializer.is_valid()
        return Response(serializer.data, status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated, )


class AuthorRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated, )
    lookup_field = 'username'
