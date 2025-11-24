import library

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        library.add_book()
    elif choice == '2':
        library.display_books()
    elif choice == '3':
        library.issue_book()
    elif choice == '4':
        library.return_book()
    elif choice == '5':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")