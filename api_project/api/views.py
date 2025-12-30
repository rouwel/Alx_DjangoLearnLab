from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
# Create your views here.

class BookList(generics.CreateAPIView):
    queryset = Book.objects.all
    serializer_class = BookSerializer
