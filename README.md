A simple and efficient Library Management System built using Python.
This project helps manage books, issue/return records, and maintains a JSON-based database.

Features
---------------------------------------------------------
   Add new books to the library

   View all available books

   Issue a book to a user

   Return a book

   Automatic fine calculation (₹20/day after free days)

   JSON file storage (no external database needed)

   User-friendly and easy to extend
   

Technologies Used
------------------------------------------------------------
  Python 

  JSON for data storage

  Datetime module for fine calculation
  

How It Works
-----------------------------------------------------------
All book and user data is stored in a JSON file (library.json or books.json).

When a user issues a book, the program saves the date.

On return, the system calculates late days and applies a fine if needed.
