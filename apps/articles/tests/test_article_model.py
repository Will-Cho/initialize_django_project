# System
from django.test import TestCase


# Project
from apps.articles.models import Article
from apps.users.models import User
from config.constants import SERVICE


class UserModelTest(TestCase):
    assert SERVICE.DEBUG
    test_user_info = {
        "email": "api-test@test.com",
        "username": "api-tester",
        "password": "api-test1!",
    }

    test_article_data = {
        "title": "title",
        "content": "content",
        "thumbnail": "test_thumnail_url",
        "status": "public",
    }

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(**cls.test_user_info)
        cls.article = Article.objects.create(user=cls.user, **cls.test_article_data)

    def test_model(self):
        """
        Article Model Test
        """
        article = Article.objects.last()
        self.assertEqual(self.test_article_data["title"], article.title)
        self.assertEqual(self.test_article_data["content"], article.content)
        self.assertEqual(self.test_article_data["status"], article.status)

    def test_max_length(self):
        """
        Article Model Max Length Test
        """
        article = Article.objects.last()
        title_max_length = article._meta.get_field("title").max_length

        self.assertEqual(title_max_length, 200)
