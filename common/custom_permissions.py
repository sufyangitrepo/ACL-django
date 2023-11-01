from functools import partial, wraps
from django.db.models import Q
from rest_framework.permissions import BasePermission

from role.models import RoleUser
from permission.models import Permission, PermissionRole


class IsAllowed(BasePermission):

    related_field = None

    def __init__(self, related_field) -> None:
        super().__init__()
        self.related_field = related_field

    def __call__(self):
        return self

    def has_permission(self, request, view):
        permission_value = self.get_permission(
            request.method, self.related_field)
        return self.is_allow(user=request.user,
                             permission_value=permission_value)

    def is_allow(self, user, permission_value):
        user_roles = RoleUser.objects.filter(user=user).all()
        permission = Permission.objects.filter(key=permission_value).first()
        if permission:
            has_perm = False
            for user_role in user_roles:
                permission_role = PermissionRole.objects.get_permission_role(
                    user_role.role, permission)
                if permission_role:
                    has_perm = True
                    break
            return has_perm

        return False

    def get_permission(self, key, related_field):
        action = None
        match key:
            case 'GET':
                action = 'view'
            case 'POST':
                action = 'add'
            case 'DELETE':
                action = 'delete'
            case default:
                action = 'change'
        if not related_field:
            raise Exception('related_field  if required in IsAllowed()')
        return f'{action}_{related_field}'
