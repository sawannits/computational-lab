import tkinter as tk
from tkinter import ttk, messagebox


class LibraryView:
    def __init__(self, root):
        self.root = root
        root.title("Library Management")
        root.geometry("850x550")

        n = ttk.Notebook(root)
        n.pack(fill="both", expand=True)

        self.add_tab(n)
        self.issue_tab(n)
        self.return_tab(n)
        self.search_tab(n)

    def add_tab(self, n):
        f = ttk.Frame(n)
        n.add(f, text="Add Book")

        self.title = tk.Entry(f, width=40)
        self.author = tk.Entry(f, width=40)
        self.category = tk.Entry(f, width=40)
        self.quantity = tk.Entry(f, width=40)

        for i, (text, entry) in enumerate([
            ("Title", self.title),
            ("Author", self.author),
            ("Category", self.category),
            ("Quantity", self.quantity)
        ]):
            ttk.Label(f, text=text).grid(row=i, column=0, pady=10)
            entry.grid(row=i, column=1)

        self.add = ttk.Button(f, text="Add Book")
        self.add.grid(row=4, column=1, pady=15)

    def issue_tab(self, n):
        f = ttk.Frame(n)
        n.add(f, text="Issue Book")

        self.book_id = tk.Entry(f, width=40)
        self.student = tk.Entry(f, width=40)
        self.issue_date = tk.Entry(f, width=40)

        for i, (text, entry) in enumerate([
            ("Book ID", self.book_id),
            ("Student", self.student),
            ("Issue Date", self.issue_date)
        ]):
            ttk.Label(f, text=text).grid(row=i, column=0, pady=10)
            entry.grid(row=i, column=1)

        self.issue = ttk.Button(f, text="Issue Book")
        self.issue.grid(row=3, column=1, pady=15)

    def return_tab(self, n):
        f = ttk.Frame(n)
        n.add(f, text="Return Book")

        ttk.Label(
            f,
            text="Issue ID"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        self.issue_id = tk.Entry(f, width=40)
        self.issue_id.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        ttk.Label(
            f,
            text="Return Date"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        self.return_date = tk.Entry(f, width=40)
        self.return_date.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        self.ret = ttk.Button(
            f,
            text="Return Book"
        )
        self.ret.grid(
            row=2,
            column=1,
            pady=15
        )

        self.issue_tree = ttk.Treeview(
            f,
            columns=("ID", "Book", "Student", "Issue", "Return", "Status"),
            show="headings"
        )

        for x in self.issue_tree["columns"]:
            self.issue_tree.heading(x, text=x)
            self.issue_tree.column(x, width=120)

        self.issue_tree.grid(
            row=4,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        f.grid_rowconfigure(4, weight=1)
        f.grid_columnconfigure(0, weight=1)
        f.grid_columnconfigure(1, weight=1)

    def search_tab(self, n):
        f = ttk.Frame(n)
        n.add(f, text="Search")

        self.search = tk.Entry(f, width=40)
        self.search.pack(pady=15)

        self.search_btn = ttk.Button(
            f,
            text="Search"
        )
        self.search_btn.pack()

        self.tree = ttk.Treeview(
            f,
            columns=("ID", "Title", "Author", "Category", "Qty"),
            show="headings"
        )

        for x in self.tree["columns"]:
            self.tree.heading(x, text=x)

        self.tree.pack(
            fill="both",
            expand=True,
            pady=15
        )

    def msg(self, text):
        messagebox.showinfo("Library", text)

