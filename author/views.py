from rest_framework import generics

from author.models import Author
from author.serializers import AuthorSerializers


class AuthorRetrieveApiView(generics.RetrieveAPIView):
    """Эндпоинт просмотра автора"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializers


class AuthorListApiView(generics.ListAPIView):
    """Эндпоинт списка авторов"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializers


class AuthorUpdateApiView(generics.UpdateAPIView):
    """Эндпоинт изменения автора"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializers


class AuthorDestroyApiView(generics.DestroyAPIView):
    """Эндпоинт удаления автора"""

    queryset = Author.objects.all()
