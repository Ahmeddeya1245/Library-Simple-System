# Library Management System

A simple Python-based library management system that allows librarians to manage books, users, and borrowing operations.

## Features

- Book Management
  - Add new books with name, ID, and quantity
  - Search books by prefix
  - View all available books
  - Track total copies and borrowed copies

- User Management
  - Add new users
  - View all users and their borrowing history
  - Track borrowed books per user

- Borrowing Operations
  - Borrow books
  - Return books
  - View users who borrowed a specific book

## Project Structure

- `Main.py` - Entry point of the application
- `FrontendManager.py` - Handles user interface and input/output operations
- `Backend.py` - Contains core business logic and data management
- `Book.py` - Book class definition and related operations
- `User.py` - User class definition and related operations

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository or download the source files
2. Ensure all Python files are in the same directory
3. Run the application using:
```bash
python Main.py
```

### Usage

The system provides a menu-driven interface with the following options:

1. Add book
2. Print Library Books
3. Print Books By Prefix
4. Add User
5. Borrow Book
6. Return Book
7. Print User Borrowed
8. Print Users
9. Exit

### Demo Data

The system comes pre-loaded with sample data including:
- Books: "Python Programming", "Data Structures and Algorithms", "Clean Code", "The Pragmatic Programmer"
- Users: Alice, Bob, Charlie
- Some pre-configured borrowing relationships

## Class Structure

### Book Class
- Properties: name, id, total_quantity, total_borrowed
- Methods for borrowing and returning copies

### User Class
- Properties: name, id, borrowed_books
- Methods for managing borrowed books

### BackendManager Class
- Manages all data operations
- Handles book and user management
- Processes borrowing transactions

### FrontendManager Class
- Handles user interface
- Manages input validation
- Coordinates between user input and backend operations

## Error Handling

The system includes basic error handling for:
- Invalid user inputs
- Non-existent books or users
- Unavailable books (all copies borrowed)
- Invalid borrowing/returning operations

## Limitations

- Data is not persistent (resets when program closes)
- No authentication system
- Single library instance only
