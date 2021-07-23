from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=64, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField(max_length=64)
    password = serializers.CharField(min_length=8, max_length=64, write_only=True)
    access = serializers.DictField(read_only=True)
    refresh = serializers.DictField(read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if not email:
            raise serializers.ValidationError('Email is required for login')

        if not password:
            raise serializers.ValidationError('Password is required for login')

        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError('A user with that email and password not found')

        if not user.is_active:
            raise serializers.ValidationError('This user has been deactivated')

        return user.token


class TokenRefreshSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=64)
    token = serializers.CharField(max_length=256, write_only=True)
    access = serializers.DictField(read_only=True)
    refresh = serializers.DictField(read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        token = attrs.get('token')
        user = User.objects.filter(email=email).first()

        if user.refresh_token == token:
            return user.token

        raise serializers.ValidationError('User was not found. PLease re-login.')


class ProfileSerializer(serializers.ModelSerializer):
    country = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'name', 'birthday', 'country', 'bio']
