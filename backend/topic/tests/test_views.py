from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from .factories import TopicFactory


class TopicViewTestCase(APITestCase):
    def setUp(self):
        self.topic = TopicFactory()

    def test_output(self):
        resp = self.client.get(reverse('topics_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['results'][0]['name'], self.topic.name)
        self.assertEqual(resp.data['results'][0]['quote'], self.topic.quote)
        self.assertEqual(resp.data['results'][0]['description'], self.topic.description)

    def test_permissions(self):
        data = {
            'name': 'Android dev',
            'quote': 'Building little green robots.',
            'description': 'Follow to see more stories about Android Dev on '
                           'your homepage and in your Article Web App Daily Digest'
        }
        resp = self.client.put(reverse('topic_create'), data)
        self.assertEqual(resp.status_code, 401)
