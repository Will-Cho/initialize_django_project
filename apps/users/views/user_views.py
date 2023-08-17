# System
from rest_framework import viewsets, status


# Project
from config.auth import auth_requred
from config.common import create_response
from apps.users.serializers.user_serializers import UserSerializer
from apps.users.swaggers.user_swaggers import swagger_get_user


class UserViewSet(viewsets.ViewSet):
    swagger_tags = ["유저"]

    @auth_requred
    @swagger_get_user
    def get_user(self, request):
        """
        유저 자신의 정보 조회
        """
        user = request.user
        serializer = UserSerializer(user)

        return create_response(data=serializer.data, status=status.HTTP_200_OK)
