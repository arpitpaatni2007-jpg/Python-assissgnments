from inventory import LibraryInventory
from book import Book

def menu():
    lib = LibraryInventory()

    while True:
        print("\n========== Library Inventory Manager ==========")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")
        print("===============================================")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")

                lib.add_book(Book(title, author, isbn))
                lib.save()

                print("Book added successfully!")

            elif choice == "2":
                isbn = input("Enter ISBN to issue: ")
                book = lib.search_by_isbn(isbn)

                if book and book.is_available():
                    book.issue()
                    lib.save()
                    print("Book issued successfully.")
                else:
                    print("Book not available or already issued.")

            elif choice == "3":
                isbn = input("Enter ISBN to return: ")
                book = lib.search_by_isbn(isbn)

                if book:
                    book.return_book()
                    lib.save()
                    print("Book returned successfully.")
                else:
                    print("Book not found.")

            elif choice == "4":
                lib.display_all()

            elif choice == "5":
                title = input("Enter title to search: ")
                results = lib.search_by_title(title)

                if results:
                    for b in results:
                        print(b)
                else:
                    print("No matching books found.")

            elif choice == "6":
                print("Exiting program...")
                break

            else:
                print("Invalid choice, try again.")

        except Exception as e:
            print("An error occurred:", e)


if __name__ == "__main__":
    menu()
