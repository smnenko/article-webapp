from django.test import TestCase

from topic.models import Topic
from .factories import TopicFactory


class TopicModelsTestCase(TestCase):
    def setUp(self):
        self.topic = TopicFactory()

    def test_topic_exists(self):
        self.assertTrue(Topic.objects.filter(name='Programming').exists())

    def test_topic_fields(self):
        self.assertEqual(self.topic.id, self.topic.pk)
        self.assertEqual(self.topic.name, 'Programming')
        self.assertEqual(self.topic.quote, 'The good, the bad, the buggy.')
        self.assertTrue(self.topic.description.startswith('Follow to see more stories about'))

    def test_topic_fields_length(self):
        name_max_length = self.topic._meta.get_field('name').max_length
        quote_max_length = self.topic._meta.get_field('quote').max_length
        description_max_length = self.topic._meta.get_field('description').max_length
        self.assertEqual(name_max_length, 32)
        self.assertEqual(quote_max_length, 128)
        self.assertEqual(description_max_length, 1024)
