import sqlite3

class LibraryModel:
    def __init__(self):
        self.conn = sqlite3.connect("library.db")
        self.create_tables()

    def create_tables(self):
        c = self.conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            category TEXT,
            quantity INTEGER
        )
        """)
        c.execute("""
        CREATE TABLE IF NOT EXISTS issued(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            student TEXT,
            issue_date TEXT,
            return_date TEXT,
            status TEXT
        )
        """)
        self.conn.commit()

    def add_book(self, title, author, category, quantity):
        self.conn.execute(
            "INSERT INTO books(title,author,category,quantity) VALUES(?,?,?,?)",
            (title, author, category, quantity)
        )
        self.conn.commit()

    def books(self, key=""):
        c = self.conn.cursor()
        c.execute(
            "SELECT * FROM books WHERE title LIKE ? OR author LIKE ?",
            (f"%{key}%", f"%{key}%")
        )
        return c.fetchall()

    def issue(self, book_id, student, date):
        c = self.conn.cursor()
        c.execute("SELECT quantity FROM books WHERE id=?", (book_id,))
        b = c.fetchone()

        if not b or b[0] <= 0:
            return False

        c.execute(
            "INSERT INTO issued(book_id,student,issue_date,status) VALUES(?,?,?,'Issued')",
            (book_id, student, date)
        )
        c.execute(
            "UPDATE books SET quantity=quantity-1 WHERE id=?",
            (book_id,)
        )
        self.conn.commit()
        return True

    def issued(self):
        return self.conn.execute("""
        SELECT issued.id,books.title,issued.student,
        issued.issue_date,issued.return_date,issued.status
        FROM issued JOIN books ON issued.book_id=books.id
        """).fetchall()

    def return_book(self, issue_id, date):
        c = self.conn.cursor()
        c.execute("SELECT book_id,status FROM issued WHERE id=?", (issue_id,))
        x = c.fetchone()

        if not x or x[1] == "Returned":
            return False

        c.execute(
            "UPDATE issued SET return_date=?,status='Returned' WHERE id=?",
            (date, issue_id)
        )
        c.execute(
            "UPDATE books SET quantity=quantity+1 WHERE id=?",
            (x[0],)
        )
        self.conn.commit()
        return True
