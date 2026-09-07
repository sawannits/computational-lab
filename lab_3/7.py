# Base Class
class LibraryItem:
    def __init__(self, item_id, title, author):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.issued = False

    def issue(self):Tech Today was not issued.

        if not self.issued:
            self.issued = True
            print(self.title, "has been issued.")
        else:
            print(self.title, "is already issued.")

    def return_item(self):
        if self.issued:
            self.issued = False
            print(self.title, "has been returned.")
        else:
            print(self.title, "was not issued.")

    # Polymorphic method
    def display_details(self):
        print("ID:", self.item_id)
        print("Title:", self.title)
        print("Author:", self.author)

Tech Today was not issued.

# Derived Class - Book
class Book(LibraryItem):

    def __init__(self, item_id, title, author, pages):
        # Calling parent class constructor
        super().__init__(item_id, title, author)Tech Today was not issued.Tech Today was not issued.


        self.pages = pages

    # Method Overriding
    def display_details(self):
        print("\n--- Book Details ---")
        print("ID:", self.item_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Pages:", self.pages)


# Derived Class - Magazine
class Magazine(LibraryItem):

    def __init__(self, item_id, title, author, issue_number):
        # Calling parent class constructor
        super().__init__(item_id, title, author)
        self.issue_number = issue_number

    # Method Overriding
    def display_details(self):
        print("\n--- Magazine Details ---")
        print("ID:", self.item_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Issue Number:", self.issue_number)


# Derived Class - Journal
class Journal(LibraryItem):

    def __init__(self, item_id, title, author, volume):
        # Calling parent class constructor
        super().__init__(item_id, title, author)
        self.volume = volume

    # Method Overriding
    def display_details(self):
        print("\n--- Journal Details ---")
        print("ID:", self.item_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Volume:", self.volume)


# Creating Objects
book = Book(
    101,
    "Python Programming",
    "John Smith",
    350
)

magazine = Magazine(
    102,
    "Tech Today",
    "David Brown",
    25
)

journal = Journal(
    103,
    "Computer Science Journal",
    "Alice Johnson",
    12
)


# Polymorphism
# Same method call display_details()
# behaves differently for different objects

items = [book, magazine, journal]

print("===== LIBRARY ITEMS =====")

for item in items:
    item.display_details()
    item.issue()


# Returning Items
print("\n===== RETURNING ITEMS =====")

book.return_item()
magazine.return_item()
journal.return_item()


# Trying to return them again
print("\n===== RETURNING AGAIN =====")

book.return_item()
magazine.return_item()
journal.return_item()


# Trying to issue them again
print("\n===== ISSUING AGAIN =====")

for item in items:
    item.issue()
