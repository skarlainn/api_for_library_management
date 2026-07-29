from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter

from .models import Book, Genre, Category
from .serializers import BookSerializer, GenreSerializer, CategorySerializer


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



class CategoryListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateApiView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveApiView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateApiView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDestroyApiView(generics.DestroyAPIView):
    queryset = Category.objects.all()
