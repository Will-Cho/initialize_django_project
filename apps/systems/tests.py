# System
from rest_framework.test import APITestCase, APIClient
from rest_framework import status


# Project
from config.constants import SERVICE, SYSTEM_CODE
from utils import times
from apps.users.models import User


class BaseAPITest(APITestCase):
    assert SERVICE.DEBUG

    testclient = APIClient()

    test_user_info = {
        "email": "api-test@test.com",
        "password": "api-test1!",
        "username": "api-tester",
    }

    test_user_login_info = {
        "email": "api-test@test.com",
        "password": "api-test1!",
    }

    user = User.objects.filter(email=test_user_info["email"]).first()
    if not user:
        testclient.post("/api/v1/auth/register/", test_user_info, format="json")

    testclient.force_authenticate(user=user)

    response = testclient.post("/api/v1/auth/login/", test_user_login_info, format="json")
    result = response.json()
    refresh_token = result["data"]["refresh_token"]
    testclient.force_authenticate(user=user)

    def setUp(self):
        """
        테스트 시작 시
        """

    def tearDown(self):
        """
        테스트 종료 시
        """
        pass
