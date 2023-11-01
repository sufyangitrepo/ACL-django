from django.urls import path, include
from rest_framework.routers import DefaultRouter
from book.views import BookView

route = DefaultRouter()
route.register('', BookView, basename='books')

urlpatterns = [
    path('book/', include(route.urls))
]
