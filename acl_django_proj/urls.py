from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth_app.urls')),
    path('role/', include('role.urls')),
    path('permission/', include('permission.urls')),
    path('', include('book.urls'))
]
