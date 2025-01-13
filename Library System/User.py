from Book import Book
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def is_borrowed(self, book) -> bool:
        for mybook in self.borrowed_books:
            if book.id == mybook.id:  # if they have the same id delete it
                return True
        return False

    def return_book(self, book):
        for idx, mybook in enumerate(self.borrowed_books):
            if mybook.id == book.id:
                del self.borrowed_books[idx]  # delete the book form the list if its founded
                break

    def simple_repr(self, is_detailed=False):
        ret = f'User Name : {self.name :15} - id: {self.id}'  # ret represent basic information about User -> user name is detected by 15 char only
        if self.borrowed_books and is_detailed:
            ret += '\n\t Borrowed Books : \n\t'
            for book in self.borrowed_books:
                ret += f'\t {str(book)}\n'
        return ret

    def __repr__(self):
        return self.simple_repr(True)
