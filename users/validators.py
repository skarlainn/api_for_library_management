from rest_framework.exceptions import ValidationError


class PhoneNumberValidator:
    """Проверяет номер телефона"""

    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, instance):
        if not instance.isdigit() or len(instance) != 10:
            raise ValidationError("Номер телефона должен состоять из 10 цифр и содержать только цифры")