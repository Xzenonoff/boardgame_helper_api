from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.core.views import FileViewSet
from apps.users.views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('files', FileViewSet, basename='files')


urlpatterns = [
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
