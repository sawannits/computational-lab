class LibraryItem:
    def __init__(self, item_id, title):
        self.item_id = item_id
        self.title = title
        self.issued = False
    def display(self):
        print("ID:", self.item_id)
        print("Title:", self.title)
        print("Status:", "Issued" if self.issued else "Available")
    def issue_item(self):
        if self.issued:
            print(self.title, "is already issued.")
        else:
            self.issued = True
            print(self.title, "has been issued.")
    def return_item(self):
        if self.issued:
            self.issued = False
            print(self.title, "has been returned.")
        else:
            print(self.title, "was not issued.")
class Book(LibraryItem):
    def __init__(self, item_id, title, author):
        super().__init__(item_id, title)
        self.author = author
    def display(self):
        print("\tBook")
        super().display()
        print("Author:", self.author)
class Magazine(LibraryItem):
    def __init__(self, item_id, title, issue_number):
        super().__init__(item_id, title)
        self.issue_number = issue_number
    def display(self):
        print("\tMagazine")
        super().display()
        print("Issue Number:", self.issue_number)
class Journal(LibraryItem):
    def __init__(self, item_id, title, subject):
        super().__init__(item_id, title)
        self.subject = subject
    def display(self):
        print("\tJournal")
        super().display()
        print("Subject:", self.subject)
book = Book(101, "Python Programming", "Guido van Rossum")
magazine = Magazine(102, "Tech Today", 25)
journal = Journal(103, "AI Research", "Artificial Intelligence")

book.display()
magazine.display()
journal.display()

print("\tIssue Operations")
book.issue_item()
magazine.issue_item()
journal.issue_item()
print("\tReturn Operations")
book.return_item()
journal.return_item()
print("\tUpdated Status")
book.display()
magazine.display()
journal.display()
