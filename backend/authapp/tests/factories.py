import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'authapp.User'
        django_get_or_create = ('email', 'password')

    email = 'custommail@gmail.com'
    password = 'custompasswd'
