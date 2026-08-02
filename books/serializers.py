from django.utils import timezone
from rest_framework import serializers

from author.serializers import AuthorShortSerializers
from books.models import Book, Genre, RentBooks
from books.validators import DeadlineValidator
from users.serializers import UserSerializerForRentBooks

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    author = AuthorShortSerializers(read_only=True)
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Book
        fields = "__all__"


class BookShortSerializer(serializers.ModelSerializer):
    author = AuthorShortSerializers(read_only=True)

    class Meta:
        model = Book
        fields = (
            "title",
            "author",
        )


class RentBooksSerializer(serializers.ModelSerializer):
    reader = UserSerializerForRentBooks(read_only=True)
    date_issue = serializers.DateField(read_only=True,
                                       default=timezone.now)

    class Meta:
        model = RentBooks
        fields = "__all__"
        validators = [DeadlineValidator(start_field="date_issue", end_field="deadline")]


class RentBooksUpdateSerializers(serializers.ModelSerializer):


    class Meta:
        model = RentBooks
        fields = "__all__"

