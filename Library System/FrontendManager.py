from Backend import BackendManager

def input_valid_int(msg, start=0, end=None):
    while True:
        inp = input(msg)

        if not inp.isdecimal():
            print('Invalid input. Try again!')
        elif start is not None and end is not None:
            if not (start <= int(inp) <= end):
                print('Invalid range. Try again!')
            else:
                return int(inp)
        else:
            return int(inp)

class FrontendManager:
    def __init__(self):
        self.backend = BackendManager()
        self.add_dummy_data()

    def print_menu(self):
        print('\nProgram Options:')
        messages = [
            'Add book',
            'Print Library Books',
            'Print Books By Prefix',
            'Add User',
            'Borrow Book',
            'Return Book',
            'Print User Borrowed',
            'Print Users',
            'Exit'
        ]
        messages = [f'{idx + 1}) {msg}' for idx, msg in enumerate(messages)]
        print('\n'.join(messages))
        msg = f'Enter your choice (from 1 to {len(messages)}): '
        return input_valid_int(msg, 1, len(messages))

    def add_dummy_data(self):
        self.backend.add_book("Python Programming", 101, 5)
        self.backend.add_book("Data Structures and Algorithms", 102, 3)
        self.backend.add_book("Clean Code", 103, 2)
        self.backend.add_book("The Pragmatic Programmer", 104, 4)
        self.backend.add_user("Alice")
        self.backend.add_user("Bob")
        self.backend.add_user("Charlie")
        self.backend.borrow_book("Alice", "Python Programming")
        self.backend.borrow_book("Bob", "Data Structures and Algorithms")
        self.backend.borrow_book("Charlie", "Clean Code")

    def add_book(self):
        print("Enter Books Info")
        name = str(input("Enter Book Name : "))
        id = int(input("Enter Book Id : "))
        Total_quantity = int(input("Enter Quantity : "))
        self.backend.add_book(name, id, Total_quantity)

    def print_books(self):
        print(f"All Books in the Library -> {self.backend.Get_all_books()}")

    def print_name_prefix(self):
        pre = str(input("Enter book name Prefix : "))
        print(self.backend.get_book_with_prefix(pre))

    def add_user(self):
        print("Enter User Info  ")
        name = str(input("Enter User Name : "))
        self.backend.add_user(name)  # Fix: Call backend.add_user
        print("User Added !!")

    def read_user_name_and_book_name(self, trials=3):
        trials += 1
        while trials > 0:
            trials -= 1
            print('Enter user name and book name')
            user_name = input('User name: ')
            if self.backend.get_User_by_Name(user_name) is None:
                print('Invalid user name!')
                continue
            book_name = input('Book name: ')
            if self.backend.get_book_by_name(book_name) is None:
                print('Invalid book name!')
                continue
            return user_name, book_name
        print('You did several trials! Try later.')
        return None, None

    def borrow_book(self):
        name, book = self.read_user_name_and_book_name()
        if name is None or book is None:
            print("Invalid input. Operation aborted.")
            return
        if self.backend.borrow_book(name, book):
            print("Book borrowed successfully!")
        else:
            print("Failed to borrow the book!")

    def return_book(self):
        name, book = self.read_user_name_and_book_name()
        if name is None or book is None:
            print("Invalid input. Operation aborted.")
            return
        if self.backend.return_book(name, book):
            print("Book returned successfully!")
        else:
            print("Failed to return the book!")

    def print_users_borrowed_book(self):
        book_name = input('Book name: ')
        if self.backend.get_book_by_name(book_name) is None:
            print('Invalid book name!')
        else:
            users_lst = self.backend.get_users_borrowd_book(book_name)  # Fix: Correct method name
            if not users_lst:
                print('\nNo one borrowed this book')
            else:
                print('\nList of users borrowed this book')
                for user in users_lst:
                    print(user)

    def print_users(self):
        users_str = '\n'.join([str(user) for user in self.backend.users])
        print(users_str)

    def run(self):
        while True:
            choice = self.print_menu()
            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.print_books()
            elif choice == 3:
                self.print_name_prefix()
            elif choice == 4:
                self.add_user()
            elif choice == 5:
                self.borrow_book()
            elif choice == 6:
                self.return_book()
            elif choice == 7:
                self.print_users_borrowed_book()
            elif choice == 8:
                self.print_users()
            elif choice == 9 :
                break