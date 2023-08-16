# System
from rest_framework.test import APITestCase, APIClient
from rest_framework import status


# Project
from config.constants import SERVICE, SYSTEM_CODE
from utils import times
from apps.users.models import User
from apps.systems.tests import BaseAPITest


class UserAPITest(BaseAPITest):
    assert SERVICE.DEBUG

    def test_get_user(self):
        response = self.testclient.get("/api/v1/users/", format="json")
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result["code"], SYSTEM_CODE.SUCCESS[0])
        self.assertEqual(result["msg"], SYSTEM_CODE.SUCCESS[1])
        self.assertEqual(result["data"]["email"], self.test_user_info["email"])
