# System
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from config.auth import generate_refresh_token


# Project
from config.constants import SERVICE, SYSTEM_CODE
from apps.articles.models import Article
from apps.users.models import User
from config.settings import BASE_DIR


class AuthAPITest(APITestCase):
    assert SERVICE.DEBUG

    test_user_info_01 = {
        "email": "api-test-01@test.com",
        "username": "api-tester-01",
        "password": "api-test1!-01",
    }
    test_user_info_02 = {
        "email": "api-test-02@test.com",
        "username": "api-tester-02",
        "password": "api-test1!-02",
    }
    test_article_data_01 = {
        "title": "title-01",
        "content": "content-01",
        "thumbnail": "test_thumnail_url",
        "status": "public",
    }
    test_article_data_02 = {
        "title": "title-02",
        "content": "content-02",
        "thumbnail": "test_thumnail_url",
        "status": "public",
    }

    testclient = APIClient()

    @classmethod
    def setUpTestData(cls):
        cls.user_01 = User.objects.create_user(**cls.test_user_info_01)
        cls.user_02 = User.objects.create_user(**cls.test_user_info_02)
        cls.testclient.force_authenticate(user=cls.user_01)
        cls.article_01 = Article.objects.create(user=cls.user_01, **cls.test_article_data_01)
        cls.article_02 = Article.objects.create(user=cls.user_02, **cls.test_article_data_02)

    def test_get_article_list(self):
        """
        Get Article List Test
        """
        response = self.testclient.get("/api/v1/articles/", format="json")
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result["code"], SYSTEM_CODE.SUCCESS[0])
        self.assertEqual(result["msg"], SYSTEM_CODE.SUCCESS[1])
        self.assertEqual(result["data"]["results"][0]["title"], self.test_article_data_02["title"])

    def test_get_article_list_self(self):
        """
        Get Article List Self Test
        """
        response = self.testclient.get("/api/v1/articles/self/", format="json")
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result["code"], SYSTEM_CODE.SUCCESS[0])
        self.assertEqual(result["msg"], SYSTEM_CODE.SUCCESS[1])
        self.assertEqual(result["data"]["results"][0]["title"], self.test_article_data_01["title"])

    def test_get_article(self):
        """
        Get Article Test
        """
        response = self.testclient.get(f"/api/v1/articles/{self.article_02.id}/", format="json")
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result["code"], SYSTEM_CODE.SUCCESS[0])
        self.assertEqual(result["msg"], SYSTEM_CODE.SUCCESS[1])
        self.assertEqual(result["data"]["content"], self.article_02.content)

    def test_get_article_self(self):
        """
        Get Article Self Test
        """
        response = self.testclient.get(f"/api/v1/articles/self/{self.article_01.id}/", format="json")
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result["code"], SYSTEM_CODE.SUCCESS[0])
        self.assertEqual(result["msg"], SYSTEM_CODE.SUCCESS[1])

        response = self.testclient.get(f"/api/v1/articles/self/{self.article_02.id}/", format="json")
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(result["code"], SYSTEM_CODE.ARTICLE_NOT_FOUND[0])
        self.assertEqual(result["msg"], SYSTEM_CODE.ARTICLE_NOT_FOUND[1])

    def test_post_article(self):
        """
        Post Article Test
        """
        post_article_data = {
            "title": "created-title",
            "content": "created-content",
            "thumbnail": open(f"{BASE_DIR}/apps/articles/tests/test_image.png", "rb"),
            "status": "public",
        }

        response = self.testclient.post(f"/api/v1/articles/", post_article_data, format="multipart")
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result["code"], SYSTEM_CODE.SUCCESS[0])
        self.assertEqual(result["msg"], SYSTEM_CODE.SUCCESS[1])

    def test_patch_article(self):
        """
        Patch Article Test
        """
        patch_article_data = {
            "title": "edited-title",
            "content": "edited-content",
            "thumbnail": open(f"{BASE_DIR}/apps/articles/tests/test_image.png", "rb"),
            "status": "public",
        }
        target_article_id = self.article_01.id

        response = self.testclient.patch(f"/api/v1/articles/{target_article_id}/", patch_article_data, format="multipart")
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result["code"], SYSTEM_CODE.SUCCESS[0])
        self.assertEqual(result["msg"], SYSTEM_CODE.SUCCESS[1])

        response = self.testclient.get(f"/api/v1/articles/{target_article_id}/", format="json")
        result = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result["data"]["title"], patch_article_data["title"])
        self.assertEqual(result["data"]["content"], patch_article_data["content"])

    def test_delete_article(self):
        """
        Delete Article Test
        """
        target_article_id = self.article_01.id
        response = self.testclient.delete(f"/api/v1/articles/{target_article_id}/", format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.testclient.get(f"/api/v1/articles/{target_article_id}/", format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
