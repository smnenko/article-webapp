from django.contrib import admin

from .models import AuthorSubscriber


@admin.register(AuthorSubscriber)
class AuthorSubscriber(admin.ModelAdmin):
    pass

