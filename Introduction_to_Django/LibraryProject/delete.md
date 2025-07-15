```python
from bookshelf.models import Book
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four") # Or use id if you prefer: Book.objects.get(id=1)
book_to_delete.delete()
print(Book.objects.all())
