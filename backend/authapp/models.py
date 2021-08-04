from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.timezone import now
from rest_framework_simplejwt.tokens import RefreshToken

from .managers import UserManager


class Country(models.Model):
    name = models.CharField(max_length=32)
    sticker = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=64, null=True, unique=True)
    email = models.EmailField(max_length=64, unique=True)
    name = models.CharField(max_length=128, null=True)
    country = models.ForeignKey(to=Country, on_delete=models.DO_NOTHING, null=True)
    bio = models.TextField(max_length=1024, null=True)
    birthday = models.DateField(default=now)
    refresh_token = models.CharField(max_length=256, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def token(self):
        refresh_token_obj = RefreshToken.for_user(self)
        self.refresh_token = str(refresh_token_obj)
        self.save()
        access_token = refresh_token_obj.access_token
        return {
            'id': self.id,
            'email': self.email,
            'access': {
                'token': str(access_token),
                'exp': access_token['exp'],
            },
            'refresh': {
                'token': str(self.refresh_token),
                'exp': refresh_token_obj['exp']
            }
        }
