from django.contrib import admin
# Register your models here
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import customuser



class BookAdmin(admin.ModelAdmin):
    # Show these fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters on the right sidebar
    list_filter = ('publication_year',)

    # Enable search by title and author
    search_fields = ('title', 'author')



class CustomUserAdmin(UserAdmin):
    model = customuser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(customuser, CustomUserAdmin)
