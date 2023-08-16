# System
from rest_framework import viewsets, status
from django.db import IntegrityError


# Project
from apps.users.models import User
from apps.users.serializers.auth_serializers import LoginSerializer, RegisterSerializer
from apps.users.swaggers.auth_swaggers import swagger_register, swagger_login
from config.auth import generate_access_token, generate_refresh_token
from config.constants import SYSTEM_CODE
from config.exception import raise_exception
from config.response import create_response
from utils import times


class AuthViewSet(viewsets.ViewSet):
    swagger_tags = ["인증"]

    @swagger_register
    def register(self, request):
        """
        회원가입
        성공 시, access_token, refresh_token을 발급
        """

        serializer = RegisterSerializer(data=request.data)

        if not serializer.is_valid():
            raise_exception(code=SYSTEM_CODE.INVALID_FORMAT)

        data = serializer.validated_data

        try:
            user = User.objects.create_user(**data)

        # 이미 가입된 계정인 경우
        except IntegrityError:
            raise_exception(code=SYSTEM_CODE.EMAIL_ALREADY_USE, status=status.HTTP_409_CONFLICT)

        user_data = {
            "access_token": generate_access_token(user),
            "refresh_token": generate_refresh_token(user),
        }

        return create_response(data=user_data, status=status.HTTP_201_CREATED)

    @swagger_login
    def login(self, request):
        """
        로그인
        성공 시, access_token, refresh_token을 발급
        """
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            raise_exception(code=SYSTEM_CODE.INVALID_FORMAT)

        data = serializer.validated_data

        email = data.get("email")
        password = data.get("password")

        user = User.objects.filter(email=email).first()
        # 기존 가입 유저 검사
        if not user:
            raise_exception(code=SYSTEM_CODE.EMAIL_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)

        # 패스워드 확인
        if not user.check_password(password):
            raise_exception(code=SYSTEM_CODE.EMAIL_PASSWORD_MISMATCH, status=status.HTTP_401_UNAUTHORIZED)

        user_data = {
            "access_token": generate_access_token(user),
            "refresh_token": generate_refresh_token(user),
        }

        user.last_login = times.get_now()
        user.save()

        return create_response(data=user_data, status=status.HTTP_200_OK)
