from django.db import models

from authapp.models import User


class AuthorSubscriber(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='author')
    subscriber = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='subscriber')
