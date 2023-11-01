from django.urls import (path, include)
from rest_framework.routers import DefaultRouter
from role.views import (RoleView,RoleUserView, ApplyRoles)


router = DefaultRouter()

router.register('roleUser', RoleUserView, basename='roleUsers')
router.register('applyRoles', ApplyRoles, basename='roleUsers')
router.register('', RoleView, basename='roles')

urlpatterns = [
    path('',include(router.urls)),
]