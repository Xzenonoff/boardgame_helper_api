from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Game Helper API",
        default_version='v1',
        description="Game Helper API",
    ),
    public=False,
    permission_classes=[permissions.IsAuthenticated,],
    url='http://127.0.0.1:8000/',
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'), name='API V1'),
    re_path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
