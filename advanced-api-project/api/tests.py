from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Author, Book

# Create your tests here.


class BookAPITests(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient()

        # Create sample author and book
        self.author = Author.objects.create(name="George Orwell")
        self.book = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.post("/books/", {
            "title": "Animal Farm",
            "publication_year": 1945,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.put(f"/books/{self.book.id}/", {
            "title": "Nineteen Eighty-Four",
            "publication_year": 1949,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Nineteen Eighty-Four")

    def test_delete_book(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(f"/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_year(self):
        response = self.client.get("/books/?publication_year=1949")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_title(self):
        response = self.client.get("/books/?search=1984")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "1984")

    def test_order_books_by_title(self):
        Book.objects.create(title="Animal Farm", publication_year=1945, author=self.author)
        response = self.client.get("/books/?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book["title"] for book in response.data]
        self.assertEqual(titles, sorted(titles))

    def test_permissions_required_for_create(self):
        # No login
        response = self.client.post("/books/", {
            "title": "Unauthorized Book",
            "publication_year": 2025,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
