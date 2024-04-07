from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from .pagination import *
from .serializers import *
from .permissions import *

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['post', 'get']
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ['username']
    ordering = ['id']
    pagination_class = LimitPageNumberPagination

    def get_serializer_class(self):
        return UserSerializer

    def get_queryset(self):
        return User.objects.all()

    @action(detail=False, methods=['get'])
    def me(self, request):
        return Response(self.get_serializer(self.request.user).data)
