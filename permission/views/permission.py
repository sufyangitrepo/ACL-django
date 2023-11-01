from rest_framework.viewsets import ViewSet
from rest_framework.decorators import (api_view,
                                       authentication_classes,
                                       permission_classes)
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from permission.serializers import (PermissionRoleSerializer,
                                    PermissionSerializer,
                                    ApplyPermissionsSerializer)
from permission.models import Permission, PermissionRole
from common.custom_permissions import IsAllowed


class PermissionView(ViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAllowed('permission')]

    def list(self, request):
        permissions = Permission.objects.all()
        serializer = PermissionSerializer(permissions, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        permission = None
        try:
            permission = Permission.objects.get(id=pk)
        except Permission.DoesNotExist:
            raise NotFound(detail=f'permission id \"{pk}\" does not exisit',
                           code=status.HTTP_404_NOT_FOUND)
        if permission:
            serialized_permission = PermissionSerializer(permission)
            return Response(serialized_permission.data)

    def partial_update(self, request, pk=None):
        permission = None
        try:
            permission = Permission.objects.get(id=pk)
        except Permission.DoesNotExist:
            raise NotFound(detail=f'permission id \"{pk}\" does not exisit',
                           code=status.HTTP_404_NOT_FOUND)
        if permission:
            serialized_permission = PermissionSerializer(permission,
                                                         data=request.data,
                                                         partial=True)
            serialized_permission.is_valid(raise_exception=True)
            serialized_permission.save()
            return Response('updated successullfy')

    def destroy(self, request, pk=None):
        permission = None
        try:
            permission = Permission.objects.get(id=pk)
        except Permission.DoesNotExist:
            raise NotFound(detail=f'permission id \"{pk}\" does not exisit',
                           code=status.HTTP_404_NOT_FOUND)
        if permission:
            permission.delete()
            return Response('deleted successfully')


class RolePermissionView(ViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAllowed('permission_role')]

    def list(self, request):
        permission_roles = PermissionRole.objects.all()
        serializer = PermissionRoleSerializer(permission_roles, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        permission_role = None
        try:
            permission_role = PermissionRole.objects.get(id=pk)
        except PermissionRole.DoesNotExist:
            raise NotFound(detail=f'permission role id \"{pk}\" does not exist',
                           code=status.HTTP_404_NOT_FOUND)
        if permission_role:
            serialized_permission = PermissionRoleSerializer(permission_role)
            return Response(serialized_permission.data)


class ApplyPermissionView(ViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAllowed('permission_role')]

    def create(slef, request):
        serialized_permission = ApplyPermissionsSerializer(data=request.data)
        serialized_permission.is_valid(raise_exception=True)
        role_permissions = serialized_permission.save()
        serialed_role_permission = PermissionRoleSerializer(
            role_permissions, many=True)
        return Response(serialed_role_permission.data)
