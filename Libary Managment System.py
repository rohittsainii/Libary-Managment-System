import tkinter as tk
import sys

class Library:
    def __init__(self):
        self.books = {}

    def add(self, code, book_name, author_name):
        if code in self.books:
            return "Book Already Exists"
        else:
            self.books[code] = {"Book Name": book_name, "Author Name": author_name}
            return "Your Book has Successfully Added"

    def remove(self, code):
        if code in self.books:
            del self.books[code]
            return "Book Successfully Deleted"
        else:
            return "Book not Found"

    def search(self, code):
        if code in self.books:
            return self.books[code]
        else:
            return "Book not Found"

    def display(self):
        if self.books:
            return [f"Book Code: {code}, Book Name: {book_info['Book Name']}, Author Name: {book_info['Author Name']}" for code, book_info in self.books.items()]
        else:
            return "No Books Added in the Book Shelf"

def add_book():
    code = int(code_entry.get())
    book_name = book_name_entry.get()
    author_name = author_name_entry.get()
    result_text.set(library.add(code, book_name, author_name))

def remove_book():
    code = int(code_entry.get())
    result_text.set(library.remove(code))

def search_book():
    code = int(code_entry.get())
    result_text.set(library.search(code))

def display_books():
    result_text.set("\n".join(library.display()))

def exit_library():
    sys.exit()

library = Library()

# GUI setup
root = tk.Tk()
root.title("Library Management System")

code_label = tk.Label(root, text="Code:")
code_label.grid(row=0, column=0)

code_entry = tk.Entry(root)
code_entry.grid(row=0, column=1)

book_name_label = tk.Label(root, text="Book Name:")
book_name_label.grid(row=1, column=0)

book_name_entry = tk.Entry(root)
book_name_entry.grid(row=1, column=1)

author_name_label = tk.Label(root, text="Author Name:")
author_name_label.grid(row=2, column=0)

author_name_entry = tk.Entry(root)
author_name_entry.grid(row=2, column=1)

add_button = tk.Button(root, text="Add Book", command=add_book)
add_button.grid(row=3, column=0)

remove_button = tk.Button(root, text="Remove Book", command=remove_book)
remove_button.grid(row=3, column=1)

search_button = tk.Button(root, text="Search Book", command=search_book)
search_button.grid(row=4, column=0)

display_button = tk.Button(root, text="Display All Books", command=display_books)
display_button.grid(row=4, column=1)

exit_button = tk.Button(root, text="Exit Library", command=exit_library)
exit_button.grid(row=5, column=0, columnspan=2)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.grid(row=6, column=0, columnspan=2)

root.mainloop()

