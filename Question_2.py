# Question: Design a class Library that maintains a list of books using a dictionary. 
# Implement a method to add a new book and another method to remove a book using exception handling to manage attempts to remove non-existent books. 
# Demonstrate the use of magic methods to make the Library object iterable.

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title , author):
        self.books[title] = author

    def remove_book(self, title):
        try:
            del self.books[title]
            print(f"'{title}' has been removed successfully!")
        except KeyError:
            print(f"'{title}' not present in the Library!")

    def display_books(self):
        if self.books:
            print("Books in the Library:")
            for title, author in self.books.items():
                print(f"-'{title}' by '{author}'")
        else:
            print("Library is Empty!")


    def __iter__(self):
        return iter(self.books)
    
    def __len__(self):
        return len(self.books)
    
    

lib = Library()
lib.display_books()
lib.add_book("Rich Dad, Poor Dad", "James")
lib.add_book("Pirates of Carrabian", "Micheal")
lib.add_book("Yousef Bin Tashfeen", "Naseem Hijazi")
lib.display_books()

lib.remove_book("Pirates of Carrabian")
lib.display_books()
lib.remove_book("Micheal")

for book in lib:
    print(book)

print(f"The library has {len(lib)} books.")
