# library_system.py

# ----- Data Structures -----
books = {}  # {ISBN: {"title": ..., "author": ..., "genre": ..., "total_copies": ..., "available": ...}}
members = []  # list of {"member_id": ..., "name": ..., "email": ..., "borrowed_books": [...]}
genres = ("Fiction", "Non-Fiction", "Sci-Fi", "History", "Romance")

# ----- Core Functions -----

def add_book(isbn, title, author, genre, total_copies):
    if isbn in books:
        return "Book already exists."
    if genre not in genres:
        return "Invalid genre."
    books[isbn] = {"title": title, "author": author, "genre": genre,
                   "total_copies": total_copies, "available": total_copies}
    return "Book added successfully."


def add_member(member_id, name, email):
    for m in members:
        if m["member_id"] == member_id:
            return "Member already exists."
    members.append({"member_id": member_id, "name": name,
                    "email": email, "borrowed_books": []})
    return "Member added successfully."


def search_books(keyword):
    result = []
    for isbn, info in books.items():
        if keyword.lower() in info["title"].lower() or keyword.lower() in info["author"].lower():
            result.append((isbn, info))
    return result if result else "No books found."


def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    if isbn not in books:
        return "Book not found."
    if genre and genre not in genres:
        return "Invalid genre."
    if title:
        books[isbn]["title"] = title
    if author:
        books[isbn]["author"] = author
    if genre:
        books[isbn]["genre"] = genre
    if total_copies:
        books[isbn]["total_copies"] = total_copies
        books[isbn]["available"] = total_copies
    return "Book updated successfully."


def delete_book(isbn):
    if isbn not in books:
        return "Book not found."
    for m in members:
        if isbn in m["borrowed_books"]:
            return "Cannot delete — book is borrowed."
    del books[isbn]
    return "Book deleted successfully."


def update_member(member_id, name=None, email=None):
    for m in members:
        if m["member_id"] == member_id:
            if name:
                m["name"] = name
            if email:
                m["email"] = email
            return "Member updated successfully."
    return "Member not found."


def delete_member(member_id):
    for m in members:
        if m["member_id"] == member_id:
            if m["borrowed_books"]:
                return "Cannot delete — member has borrowed books."
            members.remove(m)
            return "Member deleted successfully."
    return "Member not found."


def borrow_book(member_id, isbn):
    for m in members:
        if m["member_id"] == member_id:
            if len(m["borrowed_books"]) >= 3:
                return "Limit reached (max 3 books)."
            if isbn not in books:
                return "Book not found."
            if books[isbn]["available"] <= 0:
                return "No copies available."
            m["borrowed_books"].append(isbn)
            books[isbn]["available"] -= 1
            return "Book borrowed successfully."
    return "Member not found."


def return_book(member_id, isbn):
    for m in members:
        if m["member_id"] == member_id:
            if isbn in m["borrowed_books"]:
                m["borrowed_books"].remove(isbn)
                books[isbn]["available"] += 1
                return "Book returned successfully."
            else:
                return "Book not borrowed by member."
    return "Member not found."


