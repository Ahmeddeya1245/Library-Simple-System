Library Management System
This is a simple Library Management System implemented in Python. The system allows users to manage books, users, and borrowing/returning operations. It consists of a backend for managing data and a frontend for interacting with the system via a command-line interface.

Features
Book Management:

Add new books to the library.

Search for books by name or prefix.

Track the total quantity and borrowed copies of each book.

User Management:

Add new users to the system.

Track which books a user has borrowed.

Borrowing and Returning:

Users can borrow books if copies are available.

Users can return borrowed books.

Reporting:

List all books in the library.

List all users and their borrowed books.

Find users who have borrowed a specific book.

Project Structure
The project is organized into the following files:

Backend.py: Contains the BackendManager class, which manages books, users, and borrowing/returning operations.

Book.py: Contains the Book class, which represents a book in the library.

User.py: Contains the User class, which represents a user in the system.

FrontendManager.py: Contains the FrontendManager class, which provides a command-line interface for interacting with the system.

Main.py: The entry point of the application. It initializes and runs the FrontendManager.

How to Run the Project
Prerequisites:

Ensure you have Python 3.x installed on your system.

Clone the Repository:

bash
Copy
git clone <repository-url>
cd <repository-folder>
Run the Application:

Execute the Main.py file to start the application:

bash
Copy
python Main.py
Using the Application:

Follow the on-screen menu to perform operations such as adding books, adding users, borrowing books, returning books, and viewing reports.

Example Workflow
Add Books:

Use the "Add book" option to add new books to the library. Provide the book name, ID, and total quantity.

Add Users:

Use the "Add User" option to add new users to the system. Provide the user's name.

Borrow Books:

Use the "Borrow Book" option to allow a user to borrow a book. Provide the user's name and the book's name.

Return Books:

Use the "Return Book" option to allow a user to return a borrowed book. Provide the user's name and the book's name.

View Reports:

Use the "Print Library Books" option to view all books in the library.

Use the "Print Users" option to view all users and their borrowed books.

Use the "Print User Borrowed" option to view users who have borrowed a specific book.

Dummy Data
The system comes preloaded with dummy data for testing:

Books:

"Python Programming" (ID: 101, Quantity: 5)

"Data Structures and Algorithms" (ID: 102, Quantity: 3)

"Clean Code" (ID: 103, Quantity: 2)

"The Pragmatic Programmer" (ID: 104, Quantity: 4)

Users:

Alice (ID: 1)

Bob (ID: 2)

Charlie (ID: 3)

Code Examples
Adding a Book
python
Copy
backend.add_book("Advanced Python", 105, 10)
Borrowing a Book
python
Copy
backend.borrow_book("Alice", "Python Programming")
Returning a Book
python
Copy
backend.return_book("Alice", "Python Programming")
Listing All Books
python
Copy
print(backend.Get_all_books())
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions or feedback, please contact:

Your Name

Email: your.email@example.com

GitHub: Your GitHub Profile

Enjoy using the Library Management System! 😊
