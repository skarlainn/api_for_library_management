from datetime import date

from rest_framework.exceptions import ValidationError


def return_book(rent_book, book):
    """Отмечает книгу как возвращенную"""
    if not rent_book.is_returned:
        rent_book.is_returned = True
        rent_book.return_date = date.today()
        if book.available_quantity < book.quantity:
            book.available_quantity += 1
            book.is_available = True
            book.save()
            rent_book.save()
        else:
            raise ValidationError("Все книги уже на месте")
    else:
        raise ValidationError(f"Книга {book.title} уже возвращена")
    return book, rent_book


def take_book(book):
    """Отмечает книгу как выданную"""
    if book.is_available:
        if book.available_quantity >= 1:
            book.available_quantity -= 1
            book.save()
        else:
            book.is_available = False
            book.save()
        return book
    else:
        raise ValidationError(f"Книга {book.title} отсутствует в наличии.")