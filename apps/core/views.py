import dropbox
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .serializers import *
from .services import generate_download_url, create_file, file_delete
from .filters import *


class FileViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering = ['name']
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']

    def get_queryset(self):
        return File.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return FileCreateSerializer
        return FileListRetrieveSerializer

    def create(self, request):
        file = create_file(self.request.data.get('file'))
        serializer = FileCreateSerializer(file)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'])
    def download_file(self, request, *args, **kwargs):
        download_url = generate_download_url(self.get_object().file)
        return Response({"download_url": download_url})

    def destroy(self, request, pk):
        try:
            file_delete(self.get_object())
            return Response(status=status.HTTP_204_NO_CONTENT)
        except dropbox.exceptions.ApiError as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
