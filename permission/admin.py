from django.contrib import admin
from permission.models import (Permission,PermissionRole)

admin.site.register(Permission)
admin.site.register(PermissionRole)
