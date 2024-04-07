from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from djoser.views import UserCreateView, TokenCreateView, TokenRefreshView
from djoser.serializers import TokenCreateSerializer
