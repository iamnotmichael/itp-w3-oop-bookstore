class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.authors = []
        self.books = []

    def get_books(self):
        return self.books
    
    def get_authors(self):
        return self.authors
        
    def add_book(self,book):
        self.books.append(book)
        self.authors.append(book.author)
    
    def search_books(self,title=None,author=None):
        book_list = []
        if title != None:
            for book in self.books:
                if title.lower() in book.title.lower():
                    book_list.append(book)
            return book_list
        if author != None:
            for book in self.books:
                if author == book.author:
                    book_list.append(book)
            return book_list


class Author(object):
    AUTHORID = 1
    AUTHORS = []
    def __init__(self, name, nat):
        self.name = name
        self.nationality = nat
        self.id = self.AUTHORID
        Author.AUTHORID += 1
        
    def get_books(self):
        for self.name in Book.BOOKS:
            return Book.BOOKS[self.name]


class Book(object):
    BOOKID = 1
    BOOKS = {}
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.id = self.BOOKID
        Book.BOOKID += 1
        if author.name in Book.BOOKS:
            Book.BOOKS[author.name].append(self)
        else:
            Book.BOOKS.update({author.name:[self]})