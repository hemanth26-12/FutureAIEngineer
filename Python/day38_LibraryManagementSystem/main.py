from Python.day38_LibraryManagementSystem.library import Library


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Save JSON")
        print("5. Load JSON")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            library.search_book()
        elif choice == "4":
            library.save_to_json()
        elif choice == "5":
            library.load_from_json()
        elif choice == "6":
            print("Thank you for using the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
