from .models import Project
import django_filters
from django_filters.rest_framework import FilterSet


class ProjectFilter(django_filters.FilterSet):
    description=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model=Project
        fields='__all__'
        exclude=['create_date','description','name','members']   
        
        