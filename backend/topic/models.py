from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=32)
    quote = models.CharField(max_length=128)
    description = models.TextField(max_length=1024)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
