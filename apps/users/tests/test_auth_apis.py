# System
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from config.auth import generate_refresh_token


# Project
from config.constants import SERVICE, SYSTEM_CODE
from utils import times
from apps.users.models import User


class AuthAPITest(APITestCase):
    assert SERVICE.DEBUG

    test_user_info = {
        "email": "api-test@test.com",
        "username": "api-tester",
        "password": "api-test1!",
    }

    testclient = APIClient()

    @classmethod
    def setUpTestData(cls):
        now = times.get_now()
        cls.timestamp = int(now.timestamp())
        cls.user = User.objects.create_user(**cls.test_user_info)
        cls.refresh_token = generate_refresh_token(cls.user)
        cls.testclient.force_authenticate(user=cls.user)

    def tearDown(self):
        """
        테스트 종료 시
        """
        pass

    def test_register_success(self):
        """
        Register API Success Test
        """

        request_body = {
            "email": f"test-{self.timestamp}@test.com",
            "password": f"test-{self.timestamp}",
            "username": f"tester-{self.timestamp}",
        }

        response = self.testclient.post("/api/v1/auth/register/", request_body, format="json")
        result = response.json()

        user = User.objects.filter(email=request_body["email"]).first()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result["code"], SYSTEM_CODE.SUCCESS[0])
        self.assertEqual(result["msg"], SYSTEM_CODE.SUCCESS[1])
        self.assertIsInstance(user, User)

    def test_login_success(self):
        """
        Login API Success Test
        """

        response = self.testclient.post("/api/v1/auth/login/", self.test_user_info, format="json")
        result = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result["code"], SYSTEM_CODE.SUCCESS[0])
        self.assertEqual(result["msg"], SYSTEM_CODE.SUCCESS[1])

    def test_refresh_token(self):
        """
        Refresh Token API Success Test
        """

        request_body = {"refresh_token": self.refresh_token}
        response = self.testclient.post("/api/v1/auth/refresh/", request_body, format="json")
        result = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result["code"], SYSTEM_CODE.SUCCESS[0])
        self.assertEqual(result["msg"], SYSTEM_CODE.SUCCESS[1])
