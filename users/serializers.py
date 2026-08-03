from rest_framework import serializers

from users.models import User
from users.validators import PhoneNumberValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "is_superuser",
            "is_staff",
            "groups",
            "user_permissions",
        )
        validators = [
            PhoneNumberValidator(field_name="phone"),
        ]


class UserSerializerForRentBooks(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "phone",
        )
