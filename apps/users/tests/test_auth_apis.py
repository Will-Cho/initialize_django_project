# System
from rest_framework.test import APIClient
from rest_framework import status


# Project
from config.constants import SERVICE, SYSTEM_CODE
from utils import times
from apps.users.models import User
from apps.systems.tests import BaseAPITest


class AuthAPITest(BaseAPITest):
    assert SERVICE.DEBUG

    def setUp(self):
        """
        테스트 시작 시
        """
        now = times.get_now()
        self.timestamp = int(now.timestamp())
        user = User.objects.filter(email=self.test_user_info["email"]).first()
        if not user:
            self.testclient.post("/api/v1/auth/register/", self.test_user_info, format="json")

        response = self.testclient.post("/api/v1/auth/login/", self.test_user_login_info, format="json")
        result = response.json()
        self.refresh_token = result["data"]["refresh_token"]

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

        response = self.testclient.post("/api/v1/auth/login/", self.test_user_login_info, format="json")
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
