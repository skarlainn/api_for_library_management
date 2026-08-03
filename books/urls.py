from django.urls import path
from rest_framework.routers import DefaultRouter

from books.apps import BooksConfig

from books.views import (
    BookViewSet,
    GenreListApiView,
    GenreCreateApiView,
    GenreUpdateApiView,
    GenreRetrieveApiView,
    GenreDestroyApiView,
    RentBooksListApiView,
    RentBooksCreateApiView,
    RentBooksRetrieveApiView,
    RentBooksUpdateApiView,
    RentBooksDestroyApiView,
)

router = DefaultRouter()
router.register(r"", BookViewSet, basename="books")


app_name = BooksConfig.name

urlpatterns = [
    path("genres/", GenreListApiView.as_view(), name="genres-list"),
    path("genres/create/", GenreCreateApiView.as_view(), name="genre-create"),
    path("genres/<int:pk>/update/", GenreUpdateApiView.as_view(), name="genre-update"),
    path("genres/<int:pk>/", GenreRetrieveApiView.as_view(), name="genre-detail"),
    path("genres/<int:pk>/delete", GenreDestroyApiView.as_view(), name="genre-delete"),
    path("rent_books/", RentBooksListApiView.as_view(), name="rent-books-list"),
    path("rent_books/create/", RentBooksCreateApiView.as_view(), name="take-a-book"),
    path(
        "rent_books/<int:pk>/",
        RentBooksRetrieveApiView.as_view(),
        name="rent-books-detail",
    ),
    path(
        "rent_books/<int:pk>/return/",
        RentBooksUpdateApiView.as_view(),
        name="return-book",
    ),
    path(
        "rent_books/<int:pk>/delete/",
        RentBooksDestroyApiView.as_view(),
        name="rent-books-delete",
    ),
] + router.urls
