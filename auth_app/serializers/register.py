from rest_framework.serializers import ModelSerializer
from auth_app.models import AppUser



class RegisterSerializer(ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'

    def create(self,validated_data):
        password = validated_data.pop('password','')
        user = AppUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user 

class GetUserSerializer(ModelSerializer):
    from role import serializers
    role_user = serializers.RoleUserSerializer(many=True)
    class Meta:
        model = AppUser
        exclude = ['is_superuser', 'user_permissions', 'groups', 'is_staff','password']

