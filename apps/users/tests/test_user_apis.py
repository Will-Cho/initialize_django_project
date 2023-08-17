# System
from rest_framework.test import APITestCase, APIClient
from rest_framework import status


# Project
from config.constants import SERVICE, SYSTEM_CODE
from apps.users.models import User


class UserAPITest(APITestCase):
    assert SERVICE.DEBUG

    test_user_info = {
        "email": "api-test@test.com",
        "username": "api-tester",
        "password": "api-test1!",
    }

    testclient = APIClient()

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(**cls.test_user_info)
        cls.testclient.force_authenticate(user=cls.user)

    def test_get_user(self):
        response = self.testclient.get("/api/v1/users/", format="json")
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result["code"], SYSTEM_CODE.SUCCESS[0])
        self.assertEqual(result["msg"], SYSTEM_CODE.SUCCESS[1])
        self.assertEqual(result["data"]["email"], self.test_user_info["email"])
