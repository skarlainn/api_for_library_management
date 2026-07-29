from django.urls import path, include
from books.views import BookViewSet, GenreViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"", BookViewSet, basename="books")
router.register(f"genres", GenreViewSet, basename="genres")
router.register(r"categories", CategoryViewSet, basename="categories")

from books.apps import BooksConfig

app_name = BooksConfig.name

urlpatterns = [path("", include(router.urls))]
