from .views import list_books
from .views import Library_Detail
from django.urls import path

urlpatterns = [
    path("books/", list_books, name = "list-books")
]

urlpatterns = [
    path("Library/", Library_Detail.as_view, name = "This Library")
]