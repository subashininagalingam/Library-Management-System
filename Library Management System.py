# Library Management System in Python 

class Library:
    def __init__(self, book_list):
        self.books = book_list  # books stored as list of dictionaries

    def display_books(self):
        print("\n📚 Available Books:")
        if not self.books:
            print("No books available right now.")
        else:
            for idx, book in enumerate(self.books, 1):
                status = "Available" if book['handover_name'] is None else f"Borrowed by {book['handover_name']}"
                print(f"{idx}. Code: {book['code']} | Title: {book['title']} "
                      f"| Author: {book['author']} | Return Period: {book['return_period']} days | Status: {status}")

    def borrow_book(self, book_code, borrower_name):
        for book in self.books:
            if book['code'].lower() == book_code.lower():
                if book['handover_name'] is None:
                    book['handover_name'] = borrower_name
                    print(f"\n✅ You have borrowed '{book['title']}' by {book['author']}. "
                          f"Please return within {book['return_period']} days.")
                else:
                    print(f"\n❌ Book '{book['title']}' is already borrowed by {book['handover_name']}.")
                return
        print(f"\n❌ Sorry, book with code '{book_code}' is not available.")

    def return_book(self, book_code):
        for book in self.books:
            if book['code'].lower() == book_code.lower():
                if book['handover_name'] is not None:
                    print(f"\n✅ Thanks for returning '{book['title']}' by {book['author']}!")
                    book['handover_name'] = None
                else:
                    print(f"\n⚠️ Book '{book['title']}' was not borrowed.")
                return
        print(f"\n❌ No book found with code '{book_code}'.")

    def add_new_book(self, code, title, author, return_period):
        self.books.append({
            "code": code,
            "title": title,
            "author": author,
            "return_period": return_period,
            "handover_name": None
        })
        print(f"\n📖 New book '{title}' by {author} added successfully! "
              f"Code: {code}, Return Period: {return_period} days")


# Main Program
def main():
    library = Library([
        {"code": "B101", "title": "Python Basics", "author": "Guido van Rossum", "return_period": 7, "handover_name": None},
        {"code": "B102", "title": "Machine Learning", "author": "Tom Mitchell", "return_period": 10, "handover_name": None},
        {"code": "B103", "title": "Data Science", "author": "Joel Grus", "return_period": 14, "handover_name": None},
        {"code": "B104", "title": "Django Guide", "author": "Adrian Holovaty", "return_period": 12, "handover_name": None},
        {"code": "B105", "title": "C++ Programming", "author": "Bjarne Stroustrup", "return_period": 20, "handover_name": None}
    ])

    while True:
        print("\n===== Library Menu =====")
        print("1. Display Available Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Add New Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            library.display_books()
        elif choice == '2':
            book_code = input("Enter the book code you want to borrow: ")
            borrower_name = input("Enter your name: ")
            library.borrow_book(book_code, borrower_name)
        elif choice == '3':
            book_code = input("Enter the book code to return: ")
            library.return_book(book_code)
        elif choice == '4':
            code = input("Enter new book code: ")
            title = input("Enter new book title: ")
            author = input("Enter author name: ")
            return_period = input("Enter return period (days): ")
            library.add_new_book(code, title, author, return_period)
        elif choice == '5':
            print("\n👋 Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("\n⚠️ Invalid choice! Please try again.")


main()
