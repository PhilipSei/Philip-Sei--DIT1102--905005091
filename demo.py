# demo.py
from Operations import *

def menu():
    while True:
        print("\n=== Mini Library System ===")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Search Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. View All Books")
        print("7. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            isbn = input("ISBN: ")
            title = input("Title: ")
            author = input("Author: ")
            genre = input("Genre: ")
            total = int(input("Total copies: "))
            print(add_book(isbn, title, author, genre, total))

        elif choice == "2":
            mid = input("Member ID: ")
            name = input("Name: ")
            email = input("Email: ")
            print(add_member(mid, name, email))

        elif choice == "3":
            key = input("Search keyword: ")
            print(search_books(key))

        elif choice == "4":
            mid = input("Member ID: ")
            isbn = input("Book ISBN: ")
            print(borrow_book(mid, isbn))

        elif choice == "5":
            mid = input("Member ID: ")
            isbn = input("Book ISBN: ")
            print(return_book(mid, isbn))

        elif choice == "6":
            for i, (isbn, info) in enumerate(books.items(), start=1):
                print(f"{i}. {info['title']} by {info['author']} ({info['available']} available)")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()