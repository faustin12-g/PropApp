from django.urls import path
from .views import *

urlpatterns = [
    path('', properties, name="properties"),
    path('tenants', tenants, name="tenants"),
]