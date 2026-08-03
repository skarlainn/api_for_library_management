from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAdminUser

from users.permissions import IsOwner
from .models import Book, Genre, RentBooks
from .pagination import MyPagination
from .serializers import (
    BookSerializer,
    GenreSerializer,
    RentBooksSerializer,
    RentBooksUpdateSerializers,
)
from .services import take_book, return_book


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    pagination_class = MyPagination
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("title", "author__last_name", "genre__name")

    def get_permissions(self):
        if self.action in ("list", "retrieve"):
            permission_classes = [AllowAny]
        elif self.action in ("update", "destroy", "partial_update", "create"):
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]  # ← добавить else
        return [permission() for permission in permission_classes]


class GenreCreateApiView(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminUser]


class GenreRetrieveApiView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AllowAny]


class GenreListApiView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = MyPagination
    permission_classes = [AllowAny]


class GenreUpdateApiView(generics.UpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminUser]


class GenreDestroyApiView(generics.DestroyAPIView):
    queryset = Genre.objects.all()
    permission_classes = [IsAdminUser]


class RentBooksListApiView(generics.ListAPIView):
    queryset = RentBooks.objects.all()
    serializer_class = RentBooksSerializer
    pagination_class = MyPagination
    permission_classes = [IsAdminUser, IsOwner]  # ← исправлено

    def get_queryset(self):
        if IsAdminUser().has_permission(self.request, self):
            return RentBooks.objects.all()
        return RentBooks.objects.filter(user=self.request.user)  # ← исправлено


class RentBooksCreateApiView(generics.CreateAPIView):
    queryset = RentBooks.objects.all()
    serializer_class = RentBooksSerializer

    def perform_create(self, serializer):
        data = serializer.save(user=self.request.user)
        take_book(data.book)
        data.save()


class RentBooksRetrieveApiView(generics.RetrieveAPIView):
    queryset = RentBooks.objects.all()
    serializer_class = RentBooksSerializer
    permission_classes = [IsAdminUser, IsOwner]  # ← исправлено


class RentBooksUpdateApiView(generics.UpdateAPIView):
    queryset = RentBooks.objects.all()
    serializer_class = RentBooksUpdateSerializers
    permission_classes = [IsAdminUser, IsOwner]  # ← исправлено

    def perform_update(self, serializer):
        data = serializer.save()
        book = data.book
        return_book(data, book)
        data.save()


class RentBooksDestroyApiView(generics.DestroyAPIView):
    queryset = RentBooks.objects.all()
    permission_classes = [IsAdminUser]