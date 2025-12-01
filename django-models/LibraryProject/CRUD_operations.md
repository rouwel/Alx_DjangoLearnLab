from bookshelf.models import Book 
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949) 
Book.objects.get(title="1984") 
output : <Book: 1984 by George Orwell>
Book.objects.all()
output : <QuerySet [<Book: 1984 by George Orwell>]>
book.title = "Nineteen Eighty-Four"
book.save()
book.delete()
output : (1, {'bookshelf.Book': 1})
