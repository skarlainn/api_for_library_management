from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny

from author.models import Author
from author.pagination import MyPagination
from author.serializers import AuthorSerializers


class AuthorCreateApiView(generics.CreateAPIView):
    """Эндпоинт создания автора"""

    serializer_class = AuthorSerializers
    permission_classes = [
        IsAdminUser,
    ]


class AuthorRetrieveApiView(generics.RetrieveAPIView):
    """Эндпоинт просмотра автора"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    permission_classes = [
        AllowAny,
    ]


class AuthorListApiView(generics.ListAPIView):
    """Эндпоинт списка авторов"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    pagination_class = MyPagination
    permission_classes = [
        AllowAny,
    ]


class AuthorUpdateApiView(generics.UpdateAPIView):
    """Эндпоинт изменения автора"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializers

    permission_classes = [
        IsAdminUser,
    ]


class AuthorDestroyApiView(generics.DestroyAPIView):
    """Эндпоинт удаления автора"""

    queryset = Author.objects.all()
    permission_classes = [
        IsAdminUser,
    ]
