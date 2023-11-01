from django.db import models
from django.db.models import Manager
from django.db.models import Q
from role.models import Role


class Permission(models.Model):
    key = models.CharField(max_length=30, unique=True)
    value = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    disabled = models.BooleanField(default=False)


class PermissionRoleManager(Manager):

    def get_permission_role(self, role, permission):
        return PermissionRole.objects.filter(
            Q(role=role) & Q(permission=permission)
        ).first()


class PermissionRole(models.Model):
    permission = models.ForeignKey(to=Permission, on_delete=models.CASCADE,
                                   related_name='role')
    role = models.ForeignKey(
        to=Role, on_delete=models.CASCADE, related_name='permissions')
    created_at = models.DateTimeField(auto_now=True)
    disabled = models.BooleanField(default=False)

    objects = PermissionRoleManager()
