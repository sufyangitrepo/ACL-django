from django.db.models import Q
from rest_framework.serializers import (ModelSerializer,
                                        IntegerField,
                                        ListField, 
                                        ValidationError)
from role.models import (Role, RoleUser)
from auth_app import serializers 
from permission.serializers import PermissionRoleSerializer


class RoleSerializer(ModelSerializer):
   
    class Meta:
        model = Role
        fields = '__all__'


class GetRoleSerializer(RoleSerializer):
    permissions = PermissionRoleSerializer(many=True)
    class Meta(RoleSerializer.Meta):
        pass


class RoleUserSerializer(ModelSerializer):
    
    role = GetRoleSerializer()

    class Meta:
        model = RoleUser
        fields = '__all__'


    

class ApplyRolesSerializer(ModelSerializer):
    
    roles = ListField(child=IntegerField())

    class Meta:
        model = RoleUser
        fields = ['user','roles']

    def validate(self, attrs):
        roles = attrs.get('roles',[])
        user = attrs.get('user')
        for role in roles:
            db_role = None
            try:
                db_role = Role.objects.get(id=role)
            except Role.DoesNotExist:
                raise ValidationError(detail={'role':f'Invalid pk \"{role}\" - object does not exist.'})
            db_role_user = RoleUser.objects.filter(Q(user=user) & Q(role=db_role)) \
                .first()
            if db_role_user:
                raise ValidationError(detail={'role':f'user \"{user.id}\" - has already this role {role}'})
        return super().validate(attrs)
    
    def create(self, validated_data):
        user = validated_data.get('user')
        roles = validated_data.get('roles',[])
        assigned_role_list = []
        for role in roles:
            db_role = Role.objects.get(id=role)
            role_user = RoleUser.objects.create(user=user, role=db_role)
            role_user.save()
            assigned_role_list.append(role_user)
        return assigned_role_list
    