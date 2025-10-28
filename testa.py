# test_library.py
from Operations import *

print(add_book("001", "Python Basics", "John Doe", "Fiction", 5))
print(add_book("002", "Data Science 101", "Jane Doe", "Non-Fiction", 3))

print(add_member("M01", "Alice", "alice@email.com"))
print(add_member("M02", "Bob", "bob@email.com"))

print(search_books("python"))
print(borrow_book("M01", "001"))
print(borrow_book("M01", "001"))
print(borrow_book("M02", "002"))

print(return_book("M01", "001"))
print(delete_member("M02"))
print(delete_book("001"))