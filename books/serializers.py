from rest_framework import serializers

from books.models import Book, Genre, RentBooks
from author.serializers import AuthorSerializers

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializers(read_only=True)
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Book
        fields = "__all__"


class RentBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentBooks
        field = "__all__"