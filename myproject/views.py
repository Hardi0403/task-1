from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

def populate_database():
    authors = [
        Author(name='J.R.R. Tolkien'),
        Author(name='J.K. Rowling'),
        Author(name='George Orwell'),
    ]
    Author.objects.bulk_create(authors)

    books = [
        Book(title='The Lord of the Rings', author=authors[0], publication_year=1954),
        Book(title='Harry Potter and the Sorcerer\'s Stone', author=authors[1], publication_year=1997),
        Book(title='1984', author=authors[2], publication_year=1949),
    ]
    Book.objects.bulk_create(books)

def access_books_with_authors():
    books = Book.objects.select_related('author').all()

    for book in books:
        print(f"Book: {book.title}")
        print(f"Author: {book.author.name}")