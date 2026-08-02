from django.urls import path, include
from books.views import (
    BookViewSet,
    GenreListApiView,
    GenreCreateApiView,
    GenreUpdateApiView,
    GenreRetrieveApiView,
    GenreDestroyApiView,
    CategoryListApiView,
    CategoryCreateApiView,
    CategoryRetrieveApiView,
    CategoryUpdateApiView,
    CategoryDestroyApiView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"", BookViewSet, basename="books")

from books.apps import BooksConfig

app_name = BooksConfig.name

urlpatterns = [
    path("genres/", GenreListApiView.as_view(), name="genres-list"),
    path("genres/create/", GenreCreateApiView.as_view(), name="genre-create"),
    path("genres/<int:pk>/update/", GenreUpdateApiView.as_view(), name="genre-update"),
    path("genres/<int:pk>/", GenreRetrieveApiView.as_view(), name="genre-detail"),
    path("genres/<int:pk>/delete", GenreDestroyApiView.as_view(), name="genre-delete"),
    path("categories/", CategoryListApiView.as_view(), name="categories-list"),
    path("categories/create/", CategoryCreateApiView.as_view(), name="category-create"),
    path("categories/<int:pk>/", CategoryRetrieveApiView.as_view(), name="category-detail"),
    path("categories/<int:pk>/update/", CategoryUpdateApiView.as_view(), name="category-update"),
    path("categories/<int:pk>/delete/", CategoryDestroyApiView.as_view(), name="category-delete"),
] + router.urls