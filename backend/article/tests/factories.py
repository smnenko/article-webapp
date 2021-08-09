import factory


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'article.Article'
        django_get_or_create = ('author', 'title', 'content')

    title = 'Hello world!'
    content = 'My first article.'
