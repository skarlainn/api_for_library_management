from rest_framework import generics

from author.models import Author
from author.pagination import MyPagination
from author.serializers import AuthorSerializers


class AuthorCreateApiView(generics.CreateAPIView):
    """Эндпоинт создания автора"""

    serializer_class = AuthorSerializers


class AuthorRetrieveApiView(generics.RetrieveAPIView):
    """Эндпоинт просмотра автора"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializers


class AuthorListApiView(generics.ListAPIView):
    """Эндпоинт списка авторов"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    pagination_class = MyPagination


class AuthorUpdateApiView(generics.UpdateAPIView):
    """Эндпоинт изменения автора"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializers


class AuthorDestroyApiView(generics.DestroyAPIView):
    """Эндпоинт удаления автора"""

    queryset = Author.objects.all()