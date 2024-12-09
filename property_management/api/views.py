from django.shortcuts import get_object_or_404
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, extend_schema_view
from .serializers import *
from property_app.models import *
from property_app.permissions import *


@extend_schema_view(
    list=extend_schema(
        summary='Retrieve a list of properties',
        description="Get a list of all properties with filtering, searching and ordering",
    ),
    retrieve = extend_schema(
        summary="Retrieve a property by ID",
        deprecated="Get details of a specific property by its ID."
    ),
     create=extend_schema(
        summary="Create a new property",
        description="Allows an admin user to create a new property.",
        request=PropertySerializer,
        responses={201: PropertySerializer},
    ),
    update=extend_schema(
        summary="Update an existing property",
        description="Allows an admin user to update an existing property.",
        request=PropertySerializer,
        responses={200: PropertySerializer},
    ),
     partial_update=extend_schema(
        summary="Partially update an existing property",
        description="Allows an admin user to partially update fields of an existing property.",
        request=PropertySerializer,
        responses={200: PropertySerializer},
    ),
    destroy=extend_schema(
        summary="Delete a property",
        description="Allows an admin user to delete an existing property."
    )
)
class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # permission_classes = [IsAdminOrReadOnly]
    filterset_fields = ['id', 'address']
    search_fields = ['name', 'property_type', 'address']
    ordering_fields = ['number_of_units']

    def get(self):
        return {'request': self.request}
    
    def post(self, request):
        serializer = PropertySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



@extend_schema_view(
    list=extend_schema(
        summary='Retrieve a list of units',
        description="Get a list of all units with filtering, searching and ordering",
    ),
    retrieve = extend_schema(
        summary="Retrieve a unit by ID",
        deprecated="Get details of a specific property by its ID."
    ),
     create=extend_schema(
        summary="Create a new property",
        description="Allows an admin user to create a new unit.",
        request=UnitSerializer,
        responses={201: UnitSerializer},
    ),
    update=extend_schema(
        summary="Update an existing unit",
        description="Allows an admin user to update an existing unit.",
        request=UnitSerializer,
        responses={200: UnitSerializer},
    ),
     partial_update=extend_schema(
        summary="Partially update an existing unit",
        description="Allows an admin user to partially update fields of an existing unit.",
        request=UnitSerializer,
        responses={200: UnitSerializer},
    ),
    destroy=extend_schema(
        summary="Delete a Unit",
        description="Allows an admin user to delete an existing unit."
    )
)
class UnitViewSet(ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # permission_classes = [IsAdminOrReadOnly]
    filterset_fields = ['bedrooms', 'rent']
    search_fields = ['bedrooms', 'bathrooms']
    ordering_fields = ['is_available']



