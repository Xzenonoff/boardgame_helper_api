from rest_framework import serializers

from apps.core.models import File


class FileListRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = '__all__'


class FileCreateSerializer(serializers.ModelSerializer):
    file = serializers.FileField(allow_empty_file=False, allow_null=False, write_only=True)

    class Meta:
        model = File
        fields = ['id', 'name', 'file', 'created_at', 'updated_at']
        read_only_fields = ['id', 'name', 'created_at', 'updated_at']
