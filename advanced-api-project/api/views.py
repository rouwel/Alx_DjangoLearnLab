from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer,AuthorSerializer
from .models import Book, Author
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.

class ListView(generics.ListAPIView): #View used to list all book instances.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DetailView(generics.RetrieveAPIViewAPIView): #View used to retrieve one specific book instance by its id.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CreateView(generics.CreateAPIView): #View used to create a book instance. It provides a message that shows the user that the book instance has been created successfully.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
        return print (f"Book '{serializer.instance.title}'created successfully.")

class UpdateView(generics.UpdateAPIView): #View used to update a book instance wit new information.
    queryset = Book.objects.all()
    serializer_class =BookSerializer
    permission_classes = [IsAuthenticated]

class DeleteView(generics.DestroyAPIView): #View used to delete a book instance from the database.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


