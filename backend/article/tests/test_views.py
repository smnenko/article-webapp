from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from authapp.tests.factories import UserFactory
from topic.tests.factories import TopicFactory
from .factories import ArticleFactory


class BaseTestCase(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('custompasswd')
        self.user.save()
        self.article = ArticleFactory(author=self.user)
        self.article.topics.set([TopicFactory(), ])


class ArticleLatestListAPIView(BaseTestCase):

    def test_response(self):
        resp = self.client.get(reverse('article_latest'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['results'][0]['id'], self.article.id)
        self.assertEqual(resp.data['results'][0]['content'], self.article.content + '...')
        self.assertEqual(resp.data['results'][0]['topics'][0]['id'], self.article.topics.first().id)

    def test_filter(self):
        requests_data = {
            'first_data': {'topic': self.article.topics.first().id, 'content': 'first'},
            'second_data': {'content': 'first'},
            'third_data': {'topic': self.article.topics.first().id}
        }
        for data in requests_data.values():
            resp = self.client.get(reverse('article_latest'), data=data)
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.data['results'][0]['id'], self.article.id)

    def test_delete(self):
        client = APIClient()
        resp = client.delete(reverse('article_delete', args=[self.article.id]))
        self.assertEqual(resp.status_code, 401)
        client.force_authenticate(user=self.user)
        resp = client.delete(reverse('article_delete', args=[self.article.id]))
        self.assertEqual(resp.status_code, 403)
        resp = client.delete(
            f"http://localhost:8000/api/v1/article/{self.article.id}/delete/?author={self.user.email}",
            args=[self.article.id])
        self.assertEqual(resp.status_code, 204)
