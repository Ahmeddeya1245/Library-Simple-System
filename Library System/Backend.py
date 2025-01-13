from Book import Book
from User import User
class BackendManager():
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, name, id, total_quantity):
        self.books.append(Book(name, id, total_quantity))  # add book by adding the struct From Class Book

    def get_book_with_prefix(self, prefix):
        return [book for book in self.books if prefix in book.name]  # add the book to list if its founded in books shelf
        # and have the prefix part in it

    def add_user(self, name):
        id = len(self.users) + 1
        self.users.append(User(name, id))

    def get_User_by_Name(self, Username): # check if user is founded
        for user in self.users:
            if Username == user.name:
                return user
        return None

    def get_book_by_name(self , name): # check if book is founded by name
        for book in self.books :
            if name == book.name :
                return book
        return None

    def borrow_book(self , User_name , book_name):
        book = self.get_book_by_name(book_name)
        user = self.get_User_by_Name(User_name)
        if book is not None and user is not None : # is this user and book founded in the db
            if book.borrow() : # can we Borrow This Book ? 
                user.borrow_book(book) # book is Borrowed 
                book.total_borrowed += 1 # increase total Borrowed by 1 every successufull time
                return True
        return False
    def return_book(self ,user_name , book_name) :
         book = self.get_book_by_name(book_name)
         user = self.get_User_by_Name(user_name)
         if book is None or user is None :
             return
         if user.is_borrowed(book) :
            book.return_copy()
            user.return_book(book)
            return True
         return False

    def get_users_borrowd_book(self , book_name):
        book = self.get_book_by_name(book_name)
        if book is None:
            return []
        return [user.name for user in self.users for borrowed_book in user.borrowed_books if book.id == borrowed_book.id]
    
    def Get_all_books(self):
        return[book.name for book in self.books]

