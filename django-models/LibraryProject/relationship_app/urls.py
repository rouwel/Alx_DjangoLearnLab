from django.urls import path
from .views import list_books
from .views import Library_Detail
import relationship_app.views as view


urlpatterns = [
    path("books/", list_books, name = "list-books")
]

urlpatterns = [
    path("Library/<int:pk>/", Library_Detail.as_view(template_name = "library_detail.html"), name = "This Library")
]