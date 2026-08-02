from rest_framework import serializers

from books.models import Book, Genre, RentBooks
from author.serializers import AuthorShortSerializers

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class BookShortSerializer(serializers.ModelSerializer):
    author = AuthorShortSerializers(read_only=True)

    class Meta:
        model = Book
        fields = (
            "title",
            "author",
        )


class BookSerializer(serializers.ModelSerializer):
    author = AuthorShortSerializers(read_only=True)
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Book
        fields = "__all__"


class RentBooksSerializer(serializers.ModelSerializer):
    book = BookShortSerializer(read_only=True)

    class Meta:
        model = RentBooks
        fields = "__all__"