from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.core.views import (
    CategoryViewSet,
    FileViewSet,
    GameViewSet,
    RuleViewSet,
    SessionViewSet,
)
from apps.users.views import UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register("files", FileViewSet, basename="files")
router.register("categories", CategoryViewSet, basename="categories")
router.register("games", GameViewSet, basename="games")
router.register("sessions", SessionViewSet, basename="sessions")
router.register("rules", RuleViewSet, basename="rules")


urlpatterns = [
    path("auth/", include("djoser.urls.jwt")),
    path("", include(router.urls)),
]
