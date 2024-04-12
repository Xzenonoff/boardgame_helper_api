from django_filters import rest_framework as filters

from apps.core.models import File


# class FileFilter(filters.FilterSet):
#     name = filters.CharFilter(field_name='name', lookup_expr='icontains')
#
#     class Meta:
#         model = File
#         fields = ['name']
