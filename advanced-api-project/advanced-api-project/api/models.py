from django.db import models

# Create your models here.

class Author(models.Model): #This model is supposed to hold the names of the various authors who will register their details inside it.
    name = models.CharField(max_length= 100)

    def __str__(self):
        return self.name
    
class Book(models.Model): #This model holds the details of the books of books that will be registered inside this APi.
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField
    author = models.ForeignKey(Author, on_delete= models.CASCADE, related_name= "books")

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
    

