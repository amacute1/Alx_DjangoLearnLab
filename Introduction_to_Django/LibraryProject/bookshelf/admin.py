# bookshelf/admin.py
from django.contrib import admin
from .models import Book

# Define the admin class for Book model
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view (table columns)
    list_display = ('title', 'author', 'publication_year')

    # Add filters on the right sidebar in the admin list view
    list_filter = ('publication_year', 'author')

    # Enable search functionality for these fields
    search_fields = ('title', 'author')

# Register your Book model with the custom admin class
admin.site.register(Book, BookAdmin)