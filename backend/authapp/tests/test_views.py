from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from .factories import UserFactory


class BaseTestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('custompasswd')
        self.user.save()


class UserLoginTestCase(BaseTestCase):

    def test_login(self):
        data = {
            'email': 'custommail@gmail.com',
            'password': 'custompasswd'
        }
        resp = self.client.post(reverse('user_login'), data)
        self.assertIn('access', resp.data)
        self.assertIn('refresh', resp.data)
        self.assertIn('email', resp.data)
        self.assertIn('id', resp.data)

    def test_login_email_is_null_error(self):
        data = {
            'password': 'custompasswd'
        }
        resp = self.client.post(reverse('user_login'), data)
        self.assertIn('email', resp.data)
        self.assertEqual(resp.data['email'][0].code, 'null')

    def test_login_email_is_blank_error(self):
        data = {
            'email': '',
            'password': 'custompasswd'
        }
        resp = self.client.post(reverse('user_login'), data)
        self.assertIn('email', resp.data)
        self.assertEqual(resp.data['email'][0].code, 'blank')

    def test_login_email_is_invalid_error(self):
        data = {
            'email': 'ascqwcqaw',
            'password': 'custompasswd'
        }
        resp = self.client.post(reverse('user_login'), data)
        self.assertIn('non_field_errors', resp.data)
        self.assertEqual(resp.data['non_field_errors'][0].code, 'invalid')

    def test_user_is_invalid_with_wrong_password_error(self):
        data = {
            'email': 'custommail@gmail.com',
            'password': 'vwevwverve'
        }
        resp = self.client.post(reverse('user_login'), data)
        self.assertIn('non_field_errors', resp.data)
        self.assertEqual(resp.data['non_field_errors'][0].code, 'invalid')

    def test_login_inactive_user(self):
        self.user.is_active = False
        self.user.save()
        data = {
            'email': 'custommail@gmail.com',
            'password': 'custompasswd'
        }
        resp = self.client.post(reverse('user_login'), data)
        self.assertIn('non_field_errors', resp.data)
        self.assertEqual(resp.data['non_field_errors'][0].code, 'invalid')
        self.user.is_active = True
        self.user.save()


class TokenViewTestCase(BaseTestCase):

    def test_refresh_token_updated(self):
        token = self.user.token
        refresh_token_old = self.user.refresh_token
        data = {
            'email': self.user.email,
            'token': refresh_token_old
        }
        resp = self.client.post(reverse('user_token'), data)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('refresh', resp.data)
        refresh_token_new = resp.data['refresh']['token']
        self.assertNotEqual(refresh_token_old, refresh_token_new)
