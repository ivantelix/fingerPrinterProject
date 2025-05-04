from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.roles.models import Role

class CustomUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)