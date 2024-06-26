# LMS
Library Management System
# Library Management System

The Library Management System is a Django-based web application designed to help manage the operations of a library, including tracking books, managing members, and handling transactions such as borrowing and returning books.

## Features

- **Manage Books**: Add, update, and remove books from the library inventory. Each book includes details such as title, author, publication date, and stock quantity.
- **Manage Members**: Add, update, and remove library members. Each member includes details such as name and outstanding debt.
- **Manage Transactions**: Allow members to borrow and return books. Track transaction details such as issue date, return date, and rental fee.
- **Automatic Stock Management**: Automatically update book stock when a book is borrowed or returned to ensure accurate inventory management.
- **Outstanding Debt Tracking**: Keep track of each member's outstanding debt, which is updated when books are borrowed or returned.

## Installation

1. Clone the repository:
   
3. Install dependencies:
   
5. Apply database migrations:

6. Run the development server:

## Usage of CRUD APIS
1. Access the web application by navigating to `http://localhost:8000/admin` in your web browser
2. you can access the classes{ Books, Members, Transaction } and apply CRUD functions or by using Postman
3. Use the navigation links to manage books, members, and transactions.
4. Add new books and members as needed.
5. Allow members to borrow and return books through the transaction management Table.

## Usage of Interface

1. Access the web application by navigating to `http://localhost:8000` in your web browser.
2. Use the navigation links to manage books, members, and transactions.
3. Add new books and members as needed.
4. Allow members to borrow and return books through the transaction management interface.




