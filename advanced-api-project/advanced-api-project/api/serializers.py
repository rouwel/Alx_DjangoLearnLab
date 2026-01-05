from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):  #This serializer converts all the data from the Book table. It has code that validates whether a user entered a publication date that is incorrect. 
    class Meta:
        model = Author
        fields = '__all__'

        def publicationvalid(self, value):
            current_year = date.today().year
            if value > current_year:
                raise serializers.ValidationError(
                    f"Publication year cannot be in the future ()"
                )
            return value


class AuthorSerializer(serializers.ModelSerializer):  #This serializer connects the tables books and authors using a one to many relationship.
    books = BookSerializer(many = True, read_only = True)
    class Meta:
        model = Book
        fields = ["name","books"]
