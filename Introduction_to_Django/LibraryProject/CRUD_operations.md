
```python
from bookshelf.models import Book
book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book1)
### Retrieve Operation

```python
from bookshelf.models import Book
retrieved_book = Book.objects.get(title="1984")
print(f"Title: {retrieved_book.title}")
print(f"Author: {retrieved_book.author}")
print(f"Publication Year: {retrieved_book.publication_year}")
print(f"ID: {retrieved_book.id}")
### Update Operation

```python
from bookshelf.models import Book
book_to_update = Book.objects.get(title="1984") # Or use id if you prefer: Book.objects.get(id=1)
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()
print(book_to_update.title)
### Delete Operation

```python
from bookshelf.models import Book
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four") # Or use id if you prefer: Book.objects.get(id=1)
book_to_delete.delete()
print(Book.objects.all())
