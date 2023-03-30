from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='some@words.ru', password='pass')
        self.assertEqual(user.email, 'some@words.ru', ':(')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='some@words.ru')
        with self.assertRaises(TypeError):
            User.objects.create_user(email='', password='pass')

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@user.ru', password='pass')
        self.assertEqual(admin_user.email, 'super@user.ru', ':(')
        self.assertTrue(admin_user.is_active)
        self.assertFalse(admin_user.is_staff)
        self.assertFalse(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_superuser(email='super@user.ru', password='pass', is_superuser=False)

