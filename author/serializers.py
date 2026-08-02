from rest_framework import serializers

from author.models import Author


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class AuthorShortSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            "first_name",
            "last_name",
        )