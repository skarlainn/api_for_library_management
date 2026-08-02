from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter

from .models import Book, Genre, RentBooks
from .serializers import BookSerializer, GenreSerializer, RentBooksSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    filterset_fields = (
        "title",
        "author",
        "genre",
    )


class GenreCreateApiView(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveApiView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreListApiView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreUpdateApiView(generics.UpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDestroyApiView(generics.DestroyAPIView):
    queryset = Genre.objects.all()



class RentBooksListApiView(generics.ListAPIView):
    queryset = RentBooks.objects.all()
    serializer_class = RentBooksSerializer


class RentBooksCreateApiView(generics.CreateAPIView):
    queryset = RentBooks.objects.all()
    serializer_class = RentBooksSerializer


class RentBooksRetrieveApiView(generics.RetrieveAPIView):
    queryset = RentBooks.objects.all()
    serializer_class = RentBooksSerializer


class RentBooksUpdateApiView(generics.UpdateAPIView):
    queryset = RentBooks.objects.all()
    serializer_class = RentBooksSerializer


class RentBooksDestroyApiView(generics.DestroyAPIView):
    queryset = RentBooks.objects.all()
