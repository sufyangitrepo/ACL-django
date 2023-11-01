from django.db import models
from auth_app.models import (AppUser)


class Role(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=50)
    createt_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    disabled = models.BooleanField(default=False)


class RoleUser(models.Model):
    role = models.ForeignKey(to=Role, on_delete=models.CASCADE)
    user = models.ForeignKey(to=AppUser, on_delete=models.CASCADE, related_name='role_user')
    created_at = models.DateTimeField(auto_now=True)
