from django.db.models import Q
from rest_framework.serializers import (ModelSerializer,
                                        ListField, 
                                        IntegerField, 
                                        ValidationError)
from rest_framework import status
from permission.models import (Permission, PermissionRole)


class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class PermissionRoleSerializer(ModelSerializer):
    permission = PermissionSerializer()
    class Meta:
        model = PermissionRole
        fields = '__all__'


class ApplyPermissionsSerializer(ModelSerializer):
    permissions = ListField(child=IntegerField())
    
    class Meta:
        model = PermissionRole
        fields = ['role','permissions'] 

    def validate(self, attrs):
        permission_list = attrs.get('permissions', [])
        role = attrs.get('role')
        for permission_id in permission_list:
            db_permission = None 
            try:
                db_permission = Permission.objects.get(id=permission_id)
            except Permission.DoesNotExist:
                raise ValidationError(
                    detail=f'permission id \"{permission_id}\" does not exist',
                    code=status.HTTP_400_BAD_REQUEST
                    )
        
            existing_permission_role = PermissionRole.objects.filter(Q(role=role) & Q(permission=db_permission)) \
                .first()
            if existing_permission_role:
                raise ValidationError(
                    detail=f'role id \"{role.id}\" has already permission {permission_id}')
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        permission_list = validated_data.get('permissions', [])
        role = validated_data.get('role')
        created_pemission_list = []
        for permission_id in permission_list:
            db_permission =  Permission.objects.get(id=permission_id)
            permission_role = PermissionRole.objects.create(role=role,
                                                            permission=db_permission
                                                            )
            permission_role.save()
            created_pemission_list.append(permission_role)

        return created_pemission_list
        