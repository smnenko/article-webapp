from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView

from .models import User, AuthorSubscriber
from .serializers import RegistrationSerializer
from .serializers import LoginSerializer
from .serializers import ProfileSerializer
from .serializers import TokenRefreshSerializer
from .serializers import SubscribeSerializer


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


class SubscribeAPIView(generics.CreateAPIView):
    serializer_class = SubscribeSerializer
    queryset = AuthorSubscriber
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        request.data['author'] = User.objects.filter(email=request.data['author']).first().id
        request.data['subscriber'] = request.user.id
        obj = self.queryset.objects.filter(author_id=request.data['author'], subscriber_id=request.data['subscriber'])
        if not obj.exists():
            return super().post(request, args, kwargs)
        obj.delete()
        return Response({'message': 'Unsubscribed'}, status.HTTP_200_OK)
