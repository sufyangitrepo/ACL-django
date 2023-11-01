from django.urls import path, include
from rest_framework.routers import DefaultRouter
from permission.views import (PermissionView,
                              RolePermissionView,
                              ApplyPermissionView)
from permission.utils.permissions_list import create_permissions

create_permissions()
router = DefaultRouter()

router.register('applyPermissions', ApplyPermissionView,
                basename='apply_permission')
router.register('rolePermission/', RolePermissionView,
                basename='rolePermission')
router.register('', PermissionView, basename='permission')


urlpatterns = [

    path('', include(router.urls)),
]
