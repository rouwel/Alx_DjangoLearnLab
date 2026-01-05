from django.urls import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path("books/", ListView.as_view(), name= "Books"),
    path("books/<int:pk>/", DetailView.as_view(), name= "Specific-book"),
    path("books/create/", CreateView.as_view(), name = "Create-Book"),
    path("books/update/", UpdateView.as_view(), name = "Update-Book"),
    path("books/delete/", DeleteView.as_view(), name = "Delete-Book")

]