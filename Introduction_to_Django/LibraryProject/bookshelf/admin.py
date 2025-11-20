from django.contrib import admin

# Register your models here
from .models import Book
admin.site.register(Book)

from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Show these fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters on the right sidebar
    list_filter = ('publication_year',)

    # Enable search by title and author
    search_fields = ('title', 'author')

# Register with custom admin configuration
admin.site.register(Book, BookAdmin)

