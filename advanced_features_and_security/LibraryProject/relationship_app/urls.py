from django.urls import path
from .views import list_books, LibraryDetailView
import . import views


urlpatterns = [ 
    path('books/', list_books, name ='list_books'), 
    path("library/<int:pk>/", LibraryDetailView.as_view(template_name = "relationship_app/library_detail.html"), name = "This Library"),
    path('admin-view/', views.admin_view, name='admin_view'), 
    path('librarian-view/', views.librarian_view, name='librarian_view'), 
    path('member-view/', views.member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'), 
    path('books/<int:book_id>/edit_book/', views.edit_book, name='edit_book'), 
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]

