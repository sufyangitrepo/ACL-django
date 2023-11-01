from rest_framework.viewsets import ViewSet
from rest_framework.decorators import (api_view,
                                       authentication_classes,
                                       permission_classes
                                       )
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from role.serializers import (RoleSerializer,
                              RoleUserSerializer,
                              ApplyRolesSerializer,
                              GetRoleSerializer
                              )
from role.models import (Role, RoleUser)
from common.custom_permissions import IsAllowed
from common.custom_pagination import CustomPagination, MyPageNumberPagination


class RoleView(ViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAllowed('role')]
    pagination_class = CustomPagination

    def create(self, request):
        role_serializer = RoleSerializer(data=request.data)
        role_serializer.is_valid(raise_exception=True)
        db_role = role_serializer.save()
        return Response({'role_id': db_role.id, 'msg': 'role created successfully'})

    def retrieve(self, request, pk):
        db_role = None
        try:
            db_role = Role.objects.get(id=pk)
        except Role.DoesNotExist:
            raise NotFound('role with this id not found',
                           code=status.HTTP_404_NOT_FOUND)
        if db_role:
            db_role_serialized = GetRoleSerializer(db_role)
            return Response(db_role_serialized.data)

    def list(self, request):
        db_roles = Role.objects.all()
        paginator: MyPageNumberPagination = self.pagination_class()
        result_page = paginator.paginate_queryset(db_roles, request)
        db_roles_serialized = GetRoleSerializer(result_page, many=True)
        return Response(db_roles_serialized.data)

    def partial_update(self, request, pk):
        db_role = None
        try:
            db_role = Role.objects.get(id=pk)
        except Role.DoesNotExist:
            raise NotFound('role with this id not found',
                           code=status.HTTP_404_NOT_FOUND)
        if db_role:
            db_role_serialized = RoleSerializer(
                db_role, data=request.data, partial=True)
            db_role_serialized.is_valid(raise_exception=True)
            updated_role = db_role_serialized.save()
            serialized_role = RoleSerializer(updated_role)
            return Response(serialized_role.data)

    def destroy(self, request, pk):
        db_role = None
        try:
            db_role = Role.objects.get(id=pk)
        except Role.DoesNotExist:
            raise NotFound('role with this id not found',
                           code=status.HTTP_404_NOT_FOUND)
        if db_role:
            db_role_serialized = RoleSerializer(db_role)
            db_role.delete()
            return Response({'role': db_role_serialized.data, 'msg': 'deleted successfully'})


class RoleUserView(ViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAllowed('role_user')]

    def list(self, request):
        assigned_roles = RoleUser.objects.all()
        serialized_roles = RoleUserSerializer(assigned_roles, many=True)
        return Response(serialized_roles.data)

    def destroy(self, request, pk):
        role_user = None
        try:
            role_user = RoleUser.objects.get(id=pk)
        except RoleUser.DoesNotExist:
            raise NotFound('role_user with this id not found',
                           code=status.HTTP_404_NOT_FOUND)
        if role_user:
            role_user.delete()
            return Response({'msg': 'deleted successfully'})


class ApplyRoles(ViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAllowed('role_user')]

    def create(self, request):
        serializer = ApplyRolesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        assigned_roles = serializer.save()
        serializer = RoleUserSerializer(assigned_roles, many=True)
        return Response(serializer.data)
