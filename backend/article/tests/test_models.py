from django.test import TestCase

from authapp.tests.factories import UserFactory
from topic.tests.factories import TopicFactory
from article.models import Article
from .factories import ArticleFactory


class ArticleModelTestCase(TestCase):

    def setUp(self):
        self.article = ArticleFactory.create(author=UserFactory())
        self.topic = TopicFactory()
        self.article.topics.set([self.topic, ])

    def test_if_exists(self):
        self.assertTrue(Article.objects.filter(title='Hello world!').exists())

    def test_article_fields(self):
        self.assertEqual(self.article.id, self.article.pk)
        self.assertEqual(self.article.title, 'Hello world!')
        self.assertEqual(self.article.content, 'My first article.')
        self.assertEqual(self.article.topics.first(), self.topic)

    def test_article_field_length(self):
        title_max_length = self.article._meta.get_field('title').max_length
        self.assertEqual(title_max_length, 128)
