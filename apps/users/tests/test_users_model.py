# System
from django.test import TestCase


# Project
from apps.users.models import User


class UserModelTest(TestCase):
    test_user_data = {
        "email": "api-test@test.com",
        "password": "api-test1!",
        "username": "api-tester",
    }

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(**cls.test_user_data)

    def test_model(self):
        """
        User Model Test
        """
        user = User.objects.get(email=self.test_user_data["email"])
        self.assertEqual(self.test_user_data["email"], user.email)

    def test_max_length(self):
        """
        User Model Max Length Test
        """
        user = User.objects.get(email=self.test_user_data["email"])
        email_max_length = user._meta.get_field("email").max_length
        password_max_length = user._meta.get_field("password").max_length
        username_max_length = user._meta.get_field("username").max_length

        self.assertEqual(email_max_length, 254)
        self.assertEqual(password_max_length, 128)
        self.assertEqual(username_max_length, 150)
