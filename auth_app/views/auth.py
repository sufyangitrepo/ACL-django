from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.decorators import (api_view,
                                       authentication_classes,
                                       permission_classes)
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.pagination import PageNumberPagination
from ..models import AppUser
from auth_app.serializers import (RegisterSerializer, GetUserSerializer)
from common.custom_permissions import IsAllowed


class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        db_user = serializer.save()
        return Response({'id': db_user.id, 'msg': 'user created successfully'})


class UsersView(ViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAllowed('user')]

    def retrieve(self, request, pk):
        user = None
        try:
            user = AppUser.objects.get(id=pk)
        except AppUser.DoesNotExist:
            raise NotFound(detail=f'user \"{pk}\" not found ',
                           code=status.HTTP_404_NOT_FOUND)
        if user:
            user_serializer = GetUserSerializer(user)
            return Response(user_serializer.data)

    def list(self, request):
        users = AppUser.objects.all()
        user_serializer = GetUserSerializer(users, many=True)
        return Response(user_serializer.data)


# @api_view(['GET'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated, IsAllowed('users')])
# def show(request):
#     return Response('show')
