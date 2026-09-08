class LibraryController:
    def __init__(self, model, view):
        self.m = model
        self.v = view

        self.v.add.config(command=self.add)
        self.v.issue.config(command=self.issue)
        self.v.ret.config(command=self.return_book)
        self.v.search_btn.config(command=self.search)

        self.show_books()
        self.show_issued()

    def add(self):
        self.m.add_book(
            self.v.title.get(),
            self.v.author.get(),
            self.v.category.get(),
            int(self.v.quantity.get())
        )
        self.v.msg("Book Added")
        self.show_books()

    def issue(self):
        ok = self.m.issue(
            int(self.v.book_id.get()),
            self.v.student.get(),
            self.v.issue_date.get()
        )
        self.v.msg("Book Issued" if ok else "Book Not Available")
        self.show_books()
        self.show_issued()

    def return_book(self):
        ok = self.m.return_book(
            int(self.v.issue_id.get()),
            self.v.return_date.get()
        )
        self.v.msg("Book Returned" if ok else "Invalid Issue ID")
        self.show_books()
        self.show_issued()

    def search(self):
        self.show_books(self.v.search.get())

    def show_books(self, key=""):
        for x in self.v.tree.get_children():
            self.v.tree.delete(x)
        for row in self.m.books(key):
            self.v.tree.insert("", "end", values=row)

    def show_issued(self):
        for x in self.v.issue_tree.get_children():
            self.v.issue_tree.delete(x)
        for row in self.m.issued():
            self.v.issue_tree.insert("", "end", values=row)

