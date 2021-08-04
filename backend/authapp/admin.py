from django.contrib import admin

from .models import Country
from .models import User
from .models import AuthorSubscriber


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_active')
    exclude = ('password', )


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(AuthorSubscriber)
class AuthorSubscriber(admin.ModelAdmin):
    pass
