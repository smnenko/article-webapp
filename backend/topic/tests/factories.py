import factory


class TopicFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'topic.Topic'
        django_get_or_create = ('name', 'quote', 'description')

    name = 'Programming'
    quote = 'The good, the bad, the buggy.'
    description = 'Follow to see more stories about Programming on your homepage and in your Medium Daily Digest'
