from django.test import TestCase

from authapp.models import User
from .factories import UserFactory


class UserModelTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('custompasswd')
        self.user.save()

    def test_user_exists(self):
        self.assertTrue(User.objects.filter(email='custommail@gmail.com').exists())

    def test_user_fields(self):
        self.assertEqual(self.user.id, self.user.pk)
        self.assertEqual(self.user.email, 'custommail@gmail.com')

    def test_user_fields_length(self):
        username_max_length = self.user._meta.get_field('username').max_length
        email_max_length = self.user._meta.get_field('email').max_length
        name_max_length = self.user._meta.get_field('name').max_length
        bio_max_length = self.user._meta.get_field('bio').max_length
        refresh_token_max_length = self.user._meta.get_field('refresh_token').max_length
        self.assertEqual(username_max_length, 64)
        self.assertEqual(email_max_length, 64)
        self.assertEqual(name_max_length, 128)
        self.assertEqual(bio_max_length, 1024)
        self.assertEqual(refresh_token_max_length, 256)
