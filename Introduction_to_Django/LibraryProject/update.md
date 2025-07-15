
```python
from bookshelf.models import Book
book_to_update = Book.objects.get(title="1984") # Or use id if you prefer: Book.objects.get(id=1)
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()
print(book_to_update.title)
