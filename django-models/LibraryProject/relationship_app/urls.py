from django.urls import path
from .views import list_books, LibraryDetailView
import relationship_app.views as view


urlpatterns = [
    path("", list_books, name = "list_books"), 
    path('books/', list_books, name ='list_books'), 
    path("library/<int:pk>/", LibraryDetailView.as_view(template_name = "library_detail.html"), name = "This Library")
]

