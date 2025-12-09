from django.contrib import admin
from .models import Author
from .models import Library
from .models import Librarian
from .models import Book

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Librarian)
