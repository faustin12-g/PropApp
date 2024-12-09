from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        Group,
        related_name='core_user_set',  # Unique related_name for your custom user
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='core_user_permissions_set',  # Unique related_name for your custom user
        blank=True
    )
