from rest_framework.viewsets import ModelViewSet
from book.serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from common.custom_pagination import CustomPagination
from common.custom_permissions import IsAllowed
from book.models import Book


class BookView(ModelViewSet):
    serializer_class = BookSerializer
    pagination_class = CustomPagination
    queryset = Book.objects.all()

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAllowed('book')]
