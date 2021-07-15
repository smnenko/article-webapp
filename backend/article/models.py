from django.db import models

from authapp.models import User
from topic.models import Topic


class Article(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    topics = models.ManyToManyField(to=Topic)
    title = models.CharField(max_length=128)
    content = models.TextField()
    views = models.IntegerField(null=True, blank=True)
    praises = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
