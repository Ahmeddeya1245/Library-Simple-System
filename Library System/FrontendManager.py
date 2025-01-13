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
        print('\n🎯 Library Management System Menu:')
        messages = [
            '📚 Add New Book',
            '📖 View All Library Books',
            '🔍 Search Books By Prefix',
            '👥 Register New User',
            '📝 Borrow a Book',
            '↩️ Return a Book',
            '👤 View Book Borrowers',
            '📋 View All Users',
            '🚪 Exit System'
        ]
        messages = [f'{idx + 1}) {msg}' for idx, msg in enumerate(messages)]
        print('\n'.join(messages))
        msg = f'\n🔄 Please enter your choice (1-{len(messages)}): '
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
        print("📚 Add New Book Details 📚")
        name = str(input("📖 Enter Book Name: "))
        id = int(input("🔢 Enter Book ID: "))
        Total_quantity = int(input("📦 Enter Quantity: "))
        self.backend.add_book(name, id, Total_quantity)
        print("✅ Book added successfully!")

    def print_books(self):
        print(f"📚 Library Book Collection:\n{self.backend.Get_all_books()}")

    def print_name_prefix(self):
        pre = str(input("🔍 Enter book name prefix to search: "))
        print(f"📑 Search Results:\n{self.backend.get_book_with_prefix(pre)}")

    def add_user(self):
        print("👤 New User Registration")
        name = str(input("📝 Enter User Name: "))
        self.backend.add_user(name)
        print("✅ User registered successfully!")

    def read_user_name_and_book_name(self, trials=3):
        trials += 1
        while trials > 0:
            trials -= 1
            print('📝 Please provide the following details:')
            user_name = input('👤 User name: ')
            if self.backend.get_User_by_Name(user_name) is None:
                print('❌ Invalid user name!')
                continue
            book_name = input('📖 Book name: ')
            if self.backend.get_book_by_name(book_name) is None:
                print('❌ Invalid book name!')
                continue
            return user_name, book_name
        print('⚠️ Too many failed attempts! Please try again later.')
        return None, None

    def borrow_book(self):
        name, book = self.read_user_name_and_book_name()
        if name is None or book is None:
            print("❌ Invalid input. Operation cancelled.")
            return
        if self.backend.borrow_book(name, book):
            print("✅ Book borrowed successfully!")
        else:
            print("❌ Failed to borrow the book!")

    def return_book(self):
        name, book = self.read_user_name_and_book_name()
        if name is None or book is None:
            print("❌ Invalid input. Operation cancelled.")
            return
        if self.backend.return_book(name, book):
            print("✅ Book returned successfully!")
        else:
            print("❌ Failed to return the book!")

    def print_users_borrowed_book(self):
        book_name = input('📖 Enter Book name: ')
        if self.backend.get_book_by_name(book_name) is None:
            print('❌ Invalid book name!')
        else:
            users_lst = self.backend.get_users_borrowd_book(book_name)
            if not users_lst:
                print('📢 No users have borrowed this book')
            else:
                print('📋 Users who borrowed this book:')
                for user in users_lst:
                    print(f'👤 {user}')

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
