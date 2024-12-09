from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from .views import *

router = DefaultRouter()
router.register('properties', PropertyViewSet)
router.register('units', UnitViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('properties/', PropertyViewSet, name='properties'),
    # path('property/<int:id>/', PropertyViewSet, name='property'),
    # path('units/', units_api, name='units'),
    # path('unit/<int:id>/', units_api, name='unit'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/swagger/', SpectacularSwaggerView.as_view(), name='swagger'),
    path('docs/redoc/', SpectacularRedocView.as_view(), name='redoc'),

]
